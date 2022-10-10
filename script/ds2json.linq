<Query Kind="Program">
  <Reference>D:\src\acormier.com\rnd\ConsoleApplication3\packages\Newtonsoft.Json.10.0.1\lib\net20\Newtonsoft.Json.dll</Reference>
  <NuGetReference>morelinq</NuGetReference>
  <Namespace>MoreLinq</Namespace>
</Query>

void Main()
{
  //var rss = @"Z:\src_osx\mcneel.com\osx\trunk\src4\rhino4\Plug-ins\ironpython\plugin\rhinoscriptsyntax\Scripts\rhinoscript";
  //var rss = @"d:\\src\mcneel\rhino\src4\rhino4\Plug-ins\ironpython\plugin\rhinoscriptsyntax\Scripts\rhinoscript";
  var rss = @"S:\\rhino8\src4\rhino4\Plug-ins\ironpython\plugin\rhinoscriptsyntax\Scripts\rhinoscript";
  //var data = @"Z:\mcneel.com\RhinoDocsMainGhpSite\developer-rhino3d-com\_data";
  var data = @"S:\\developer.rhino3d.com\data";
  var filename = "rhinoscriptsyntax.json";
  
  Func<string, string> indentLeft = txtToIndent => {
    if (string.IsNullOrWhiteSpace(txtToIndent)) return "";
    var lines = txtToIndent.Split(new [] {Environment.NewLine}, StringSplitOptions.None);
    var min = lines.Where(ln => !string.IsNullOrWhiteSpace(ln)).Select(ln => ln.AsEnumerable().TakeWhile(char.IsWhiteSpace).Count()).Min();
    return lines.Select(ln => string.IsNullOrWhiteSpace(ln) ? ln : ln.Substring(min)).Aggregate((c,n) => c + Environment.NewLine + n).Trim();
  };
  
  Func<string, string> signatureFromDeclaration = dec => Regex.Match(dec, "(?<=def ).*(?=:)").Success ? Regex.Match(dec, "(?<=def ).*(?=:)").Value : "";
  
  var q = "\"\"\"";
  var p1 = @"(?<desc>.*)";
  var p2 = @"Parameters:(?<argsDesc>.*)"; 
  var p3 = @"Returns:(?<return>.*)";
  var p4 = @"Example:(?<example>.*)";
  var p5 = @"See Also:(?<links>.*)";
  Func<string, string, string, string, bool, DocStringStruct> parseDocString = (moduleName, name, signature, docString, isWellFormed) => {
    var prms = p2;
    var hasArguments = true;
    if (!Regex.Match(docString, q + p1 + prms + q, RegexOptions.Singleline).Success) {
	  prms = "";
	  hasArguments = false;
	}
    var success_level = 6;
    var m = Regex.Match(docString, q + p1 + prms + p3 + p4 + p5 + q, RegexOptions.Singleline);
    if (!m.Success) {m = Regex.Match(docString, q + p1 + prms + p3 + p4 + q, RegexOptions.Singleline); success_level = 5;}
    if (!m.Success) {m = Regex.Match(docString, q + p1 + prms + p3 + p5 + q, RegexOptions.Singleline); success_level = 4;}
    if (!m.Success) {m = Regex.Match(docString, q + p1 + prms + p3 + q, RegexOptions.Singleline); success_level = 3;}
    if (!m.Success) {m = Regex.Match(docString, q + p1 + prms + q, RegexOptions.Singleline); success_level = 2;}
    if (!m.Success) {m = Regex.Match(docString, q + p1 + q, RegexOptions.Singleline); success_level = 1;}
    var ds = new DocStringStruct() {ModuleName = moduleName, Name = name, Signature = signature, DocString = docString};
    if (m.Success) {
      ds.Arguments = Enumerable.Empty<string>();
      ds.Description = indentLeft(m.Groups["desc"].Value);
	  ds.HasArguments = hasArguments;
      ds.ArgumentDesc = hasArguments ? indentLeft(m.Groups["argsDesc"].Value) : "";
      ds.Returns = indentLeft(m.Groups["return"].Value);
      ds.Example = indentLeft(m.Groups["example"].Value).Split(new [] {Environment.NewLine}, StringSplitOptions.None).SkipWhile (a => string.IsNullOrWhiteSpace(a));
      ds.ExampleString = indentLeft(m.Groups["example"].Value);
      ds.SeeAlso = m.Groups["links"].Value
	    .Split(new [] {Environment.NewLine}, StringSplitOptions.RemoveEmptyEntries)
		.Select (a => a.Trim())
		.Where(a => !string.IsNullOrWhiteSpace(a))
		.Select(a => new SeeAlso{ModuleName="", FunctionName=a});
      ds.SuccessLevel = success_level;
      ds.IsDocStringWellFormed = success_level >= 3;
    }
	//ds.Dump();
    return ds;
  };
  
  Func<string, Match> matchFuncSig = s => Regex.Match(s, @"^def (?<fn>.[^(]*)\(.*\):");
  var _fn = "top_of_file_before_1st_func";
  Func<string, string> funcName = s => matchFuncSig(s).Success ? _fn = matchFuncSig(s).Groups["fn"].Value : _fn;
  
  var new_funcs = Directory.GetFiles(rss)
    .Where(fn => Path.GetExtension(fn).Equals(".py") && !Path.GetFileName(fn).StartsWith("__"))
    .SelectMany(fn => File.ReadAllLines(fn)
                    .SkipWhile(ln => !matchFuncSig(ln).Success)
                    .Select(ln => 
                      Tuple.Create<string, string, string>(
                        Path.GetFileNameWithoutExtension(fn),
                        funcName(ln),
                        ln
                      )
                    )
    )
    .Where (t => !Regex.Match(t.Item2, "^[a-z_].*").Success) // funcions starting in lower case or a _ are not part of the API
    .GroupBy(
      t => Tuple.Create<string, string>(t.Item1, t.Item2),
      t => t.Item3
    )
    .Select(g => parseDocString(
                  g.Key.Item1, // module name
                  g.Key.Item2, // func name
                  signatureFromDeclaration(g.First()), 
                  g.SkipUntil(ln => !ln.Contains("\"\"\"")).TakeUntil(ln => ln.Trim().Equals("\"\"\"")).Aggregate ((c,n) => c + Environment.NewLine + n),
                  g.Where (x => x.Contains("\"\"\"")).Count() == 2 && g.Any(ln => ln.Trim().Equals("Parameters:")) && g.Any(ln => ln.Trim().Equals("Returns:"))
                 )
    );
	
    // map SeeAlso function to it's module name
	var modFuncDict = new_funcs.ToDictionary (dss => dss.Name, dss => dss.ModuleName);
	new_funcs = new_funcs
	  .Select (dss => new DocStringStruct {
	    ModuleName = dss.ModuleName,
		Name = dss.Name,
		Arguments = dss.Arguments,
		Signature = dss.Signature,
		Description = dss.Description,
		HasArguments = dss.HasArguments,
		ArgumentDesc = dss.ArgumentDesc,
		Returns = dss.Returns,
		Example = dss.Example,
		ExampleString = dss.ExampleString,
		SeeAlso = dss.SeeAlso.Select(seeAlso => 
		  new SeeAlso{
		    ModuleName = modFuncDict.SingleOrDefault (kvp => kvp.Key == seeAlso.FunctionName).Value, 
			FunctionName = seeAlso.FunctionName}
		),
		DocString = dss.DocString,
		SuccessLevel = dss.SuccessLevel,
		IsDocStringWellFormed = dss.SeeAlso.All (sa => modFuncDict.ContainsKey(sa.FunctionName))
		  ? dss.IsDocStringWellFormed
		  : false
		}
	  );
		
	//new_funcs.Dump();
	IEnumerable<ModuleFunctions> mfs = new_funcs
      .GroupBy (ds => ds.ModuleName, ds => ds)
      .OrderBy (g => g.Key)
      .Select (x => new ModuleFunctions {ModuleName = x.Key, functions = x.Select (z => z)});
	 
	//mfs.Dump();
  	var json = Newtonsoft.Json.JsonConvert.SerializeObject(mfs, Newtonsoft.Json.Formatting.Indented);
  	File.WriteAllText(Path.Combine(data, filename), json);
}

struct SeeAlso {
  public string ModuleName;
  public string FunctionName;
}

struct ModuleFunctions {
  public string ModuleName;
  public IEnumerable<DocStringStruct> functions;
}

// Define other methods and classes here
struct DocStringStruct {
  public string ModuleName;
  public string Name;
  public IEnumerable<string> Arguments;
  public string Signature;
  public string Description;
  public bool HasArguments;
  public string ArgumentDesc;
  public string Returns;
  public IEnumerable<string> Example;
  public string ExampleString;
  public IEnumerable<SeeAlso> SeeAlso;
  public string DocString;
  public int SuccessLevel;
  public bool IsDocStringWellFormed;
}