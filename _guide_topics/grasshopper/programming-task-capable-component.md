---
title: Task capable components
description: A guide to programming multi-threaded components in Grasshopper
authors: ['Steve Baer', 'Scott Davidson']
author_contacts: ['stevebaer','scottd']
sdk: ['Grasshopper']
languages: ['Grasshopper']
platforms: ['Windows', 'Mac']
categories: ['Advanced']
origin: http://www.grasshopper3d.com/forum/topics/the-why-and-how-of-data-trees
order: 2
keywords: ['developer', 'grasshopper', 'components']
layout: toc-guide-page
---

Developer Grasshopper components that can call multiple tasks in parallel can be done in C# or in Python.

When a component implements the IGH_TaskCapableComponent interface, GH will notice and potentially call a full enumeration of SolveInstance for the component twice in consecutive passes:
1. The first pass is for collecting data and starting tasks to compute results
2. The second pass is for using the results from the tasks to set outputs.

The sample [Component_DashCurve component](https://gist.github.com/sbaer/8a52a10c1acef7dfc9fc85fc7d06a263/b6e5548cbe3d333f8e57817136f22818a6b05e97) is a good example of how to make a component task capable. The initial component code looks like this:

```C#
public class Component_DashCurve : GH_Component
  {
    public Component_DashCurve()
      : base("Dash Pattern", "Dash", "Convert a curve to a dash pattern.", "Curve", "Division")
    { }

    protected override void RegisterInputParams(GH_InputParamManager pManager)
    {
      pManager.AddCurveParameter("Curve", "C", "Curve to dash", GH_ParamAccess.item);
      pManager.AddNumberParameter("Pattern", "Pt", "An collection of dash and gap lengths.", GH_ParamAccess.list);
    }
    protected override void RegisterOutputParams(GH_OutputParamManager pManager)
    {
      pManager.AddCurveParameter("Dashes", "D", "Dash segments", GH_ParamAccess.list);
      pManager.AddCurveParameter("Gaps", "G", "Gap segments", GH_ParamAccess.list);

      pManager.HideParameter(1);
    }

    protected override void SolveInstance(IGH_DataAccess DA)
    {
      Curve crv = null;
      List<double> pattern = new List<double>();

      if (!DA.GetData(0, ref crv)) { return; }
      if (!DA.GetDataList(1, pattern)) { return; }

      if (pattern.Count == 0)
        return;

      double pattern_length = 0.0;
      for (int i = 0; i < pattern.Count; i++)
      {
        if (pattern[i] < 0.0)
        {
          AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Dash patterns cannot have negative length segments");
          pattern[i] = 0.0;
        }
        pattern_length += pattern[i];
      }

      if (pattern_length <= 1e-12)
      {
        AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Total pattern length is too short.");
        return;
      }

      crv = crv.DuplicateCurve();

      List<Curve> dashes = new List<Curve>();
      List<Curve> gaps = new List<Curve>();

      int index = -1;
      bool dash = false;

      while (true)
      {
        //toggle gap/dash flag
        dash = !dash;

        //increment
        index++;

        //limit
        if (index >= pattern.Count) { index = 0; }

        //get pattern length
        if (Math.Abs(pattern[index]) < 1e-32)
        {
          if (dash) { dashes.Add(null); }
          else { gaps.Add(null); }
        }
        else
        {
          //measure length
          double length = crv.GetLength();
          if (!RhinoMath.IsValidDouble(length)) { break; }

          //cut short if we're at the end of the curve
          if (length <= pattern[index])
          {
            if (dash) { dashes.Add(crv); }
            else { gaps.Add(crv); }
            break;
          }

          //compute normalised arc-length parameter.
          double t ;
          if (!crv.LengthParameter(pattern[index], out t)) { break; }

          Curve segment = crv.Trim(crv.Domain.Min, t);
          if (segment != null && segment.IsValid)
          {
            if (dash) { dashes.Add(segment); }
            else { gaps.Add(segment); }
          }

          crv = crv.Trim(t, crv.Domain.Max);
          if (crv == null) break;
        }
      }

      DA.SetDataList(0, dashes);
      DA.SetDataList(1, gaps);
    }

    public override GH_Exposure Exposure
    {
      get { return GH_Exposure.primary | GH_Exposure.obscure; }
    }
    public override Guid ComponentGuid
    {
      get { return new Guid("{95866BBE-648E-4e2b-A97C-7D04679E94E0}"); }
    }
    protected override System.Drawing.Bitmap Icon
    {
      get
      {
        return Properties.Resources.DashPattern_24x24;
      }
    }
  }
```


### Separate calculations into separate routine

Independent tasks should not be directly accessing IGH_DataAccess as that interface is not thread safe. A good place to start is by breaking the current flow of a component’s SolveInstance into 3 distinct steps

1. Collect input data
1. Compute results on given data
1. Set output data

Step (2) is what we are breaking into Tasks that can run on multiple threads.

Here is the transformed function before launching into multiple tasks:

```C#
public class Component_DashCurve : GH_Component
 {
   public Component_DashCurve()
     : base("Dash Pattern", "Dash", "Convert a curve to a dash pattern.", "Curve", "Division")
   { }

   protected override void RegisterInputParams(GH_InputParamManager pManager)
   {
     pManager.AddCurveParameter("Curve", "C", "Curve to dash", GH_ParamAccess.item);
     pManager.AddNumberParameter("Pattern", "Pt", "An collection of dash and gap lengths.", GH_ParamAccess.list);
   }
   protected override void RegisterOutputParams(GH_OutputParamManager pManager)
   {
     pManager.AddCurveParameter("Dashes", "D", "Dash segments", GH_ParamAccess.list);
     pManager.AddCurveParameter("Gaps", "G", "Gap segments", GH_ParamAccess.list);

     pManager.HideParameter(1);
   }

   class SolveResults
   {
     public List<Curve> Dashes { get; set; }
     public List<Curve> Gaps { get; set; }
     public GH_RuntimeMessageLevel MessageLevel { get; private set; }
     public string ErrorMessage { get; private set; }
     public void AddRuntimeMessage(GH_RuntimeMessageLevel level, string message)
     {
       MessageLevel = level;
       ErrorMessage = message;
     }
   }

   SolveResults Compute(Curve crv, List<double> pattern)
   {
     SolveResults rc = new SolveResults();
     if (pattern.Count == 0)
       return null;

     double pattern_length = 0.0;
     for (int i = 0; i < pattern.Count; i++)
     {
       if (pattern[i] < 0.0)
       {
         rc.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Dash patterns cannot have negative length segments");
         pattern[i] = 0.0;
       }
       pattern_length += pattern[i];
     }

     if (pattern_length <= 1e-12)
     {
       rc.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Total pattern length is too short.");
       return rc;
     }

     crv = crv.DuplicateCurve();

     List<Curve> dashes = new List<Curve>();
     List<Curve> gaps = new List<Curve>();

     int index = -1;
     bool dash = false;

     while (true)
     {
       //toggle gap/dash flag
       dash = !dash;

       //increment
       index++;

       //limit
       if (index >= pattern.Count) { index = 0; }

       //get pattern length
       if (Math.Abs(pattern[index]) < 1e-32)
       {
         if (dash) { dashes.Add(null); }
         else { gaps.Add(null); }
       }
       else
       {
         //measure length
         double length = crv.GetLength();
         if (!RhinoMath.IsValidDouble(length)) { break; }

         //cut short if we're at the end of the curve
         if (length <= pattern[index])
         {
           if (dash) { dashes.Add(crv); }
           else { gaps.Add(crv); }
           break;
         }

         //compute normalised arc-length parameter.
         double t;
         if (!crv.LengthParameter(pattern[index], out t)) { break; }

         Curve segment = crv.Trim(crv.Domain.Min, t);
         if (segment != null && segment.IsValid)
         {
           if (dash) { dashes.Add(segment); }
           else { gaps.Add(segment); }
         }

         crv = crv.Trim(t, crv.Domain.Max);
         if (crv == null) break;
       }
     }
     rc.Dashes = dashes;
     rc.Gaps = gaps;
     return rc;
   }

   protected override void SolveInstance(IGH_DataAccess DA)
   {
     // 1. Collect
     Curve crv = null;
     List<double> pattern = new List<double>();

     if (!DA.GetData(0, ref crv)) { return; }
     if (!DA.GetDataList(1, pattern)) { return; }

     // 2. Compute
     var solve_results = Compute(crv, pattern);

     // 3. Set
     if ( solve_results!=null )
     {
       if (!string.IsNullOrWhiteSpace(solve_results.ErrorMessage))
         AddRuntimeMessage(solve_results.MessageLevel, solve_results.ErrorMessage);
       if (solve_results.Dashes != null || solve_results.Gaps != null)
       {
         DA.SetDataList(0, solve_results.Dashes);
         DA.SetDataList(1, solve_results.Gaps);
       }
     }
   }

   public override GH_Exposure Exposure
   {
     get { return GH_Exposure.primary | GH_Exposure.obscure; }
   }
   public override Guid ComponentGuid
   {
     get { return new Guid("{95866BBE-648E-4e2b-A97C-7D04679E94E0}"); }
   }
   protected override System.Drawing.Bitmap Icon
   {
     get
     {
       return Properties.Resources.DashPattern_24x24;
     }
   }
 }
```
{: .line-numbers}

<table>
<tr>
<th>Line</th>
<th>Description</th>
</tr>
<tr>
<td>27</td>
<td>Create a public SolveResults class to hold the data for each SolveInstance iteration.</td>
</tr>
<tr>
<td>125</td>
<td>Create a Compute function that takes the input retrieved from IGH_DataAccess and returns an instance of SolveResults. </td>
</tr>
</table>
{: .multiline}

Test the component set up this way. It should run the same as it always has.

### Implement IGH_TaskCapableComponent Interface

Now, we are ready to launch multiple tasks in the component.

1. Derive from GH_TaskCapableComponent<Component_DashCurve.SolveInstance>. This is a helper intermediate class that helps handle some of the repetitive code that would be needed to implement IGH_TaskCapableComponent
1. Update SolveInstance to use tasks

```C#
    protected override void SolveInstance(IGH_DataAccess DA)
    {
      if (InPreSolve)
      {
        // First pass; collect data and construct tasks
        Curve crv = null;
        List<double> pattern = new List<double>();

        Task<SolveResults> tsk = null;
        if (DA.GetData(0, ref crv) && DA.GetDataList(1, pattern))
        {
          tsk = Task.Run(() => Compute(crv, pattern), CancelToken);
        }
        // add a null task even if data collection fails. This keeps the
        // list size in sync with the iterations
        TaskList.Add(tsk);
        return;
      }

      bool perform_compute;
      SolveResults solve_results = GetSolveResults(DA, out perform_compute);
      if( perform_compute )
      {
        // same old, same old
        // 1. Collect
        Curve crv = null;
        List<double> pattern = new List<double>();

        if (!DA.GetData(0, ref crv)) { return; }
        if (!DA.GetDataList(1, pattern)) { return; }
        // 2. Compute
        solve_results = Compute(crv, pattern);
      }

      // 3. Set
      if ( solve_results!=null )
      {
        if (solve_results.Dashes != null || solve_results.Gaps != null)
        {
          DA.SetDataList(0, solve_results.Dashes);
          DA.SetDataList(1, solve_results.Gaps);
        }
      }
    }
```

The final code for this revision [can be seen here](https://gist.github.com/sbaer/8a52a10c1acef7dfc9fc85fc7d06a263/5785b4032c8ea94a735ac934244f98192ff597e9)
