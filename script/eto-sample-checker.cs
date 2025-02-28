// #! csharp
using System;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

using Eto.Forms;

using Rhino.UI;

using Rhino.Runtime.Code;
using Rhino.Runtime.Code.Execution;
using Rhino.Runtime.Code.Languages;
using Rhino.Runtime.Code.Diagnostics;

string etoFolder = "";

var etoFolderDialog = new SelectFolderDialog()
{
    Title = "Choose your eto folder",
};

var result = etoFolderDialog.ShowDialog(RhinoEtoApp.MainWindowForDocument(__rhino_doc__));
if (result != DialogResult.Ok)
    throw new Exception("Please choose the eto folder!");

var directory = etoFolderDialog.Directory;
if (!directory.EndsWith("eto"))
    throw new Exception("Please choose the ETO folder");

var files = Directory.EnumerateFiles(directory, "_index.md", SearchOption.AllDirectories);
foreach(var file in files)
{
    var lines = File.ReadAllText(file);
    int startIndex = 0;
    for(int i = 0; i < 1000; i++) // 1000 code samples would be very unlikely
    {
        if (startIndex > lines.Length) break;

        int firstIndex = lines.IndexOf("```", startIndex);
        if (firstIndex < 0) continue;   

        startIndex = firstIndex + 4;

        if (firstIndex + 4 > lines.Length) break;
        int secondIndex = lines.IndexOf("```", firstIndex + 4);
        if (secondIndex < 0) break; // Cannot be any more code

        startIndex = secondIndex + 4;

        var code = lines.Substring(firstIndex, secondIndex - firstIndex);
        
        var linesSoFar = lines.Substring(0, Math.Min(startIndex, lines.Length));
        int lineCount = linesSoFar.Count(l => l == '\n');

        var langCapture = Regex.Match(code, @"```[ ]*([cspy]+)[ ]*(?<compile>[no\-compile]+)?");
        if (langCapture.Groups.Count < 2)
        {
            Console.WriteLine($"Could not parse line {lineCount} in file");
            continue;
        }

        bool noCompile = langCapture.Groups.TryGetValue("compile", out var compileGroup) && compileGroup.Length > 0;
        if (noCompile)
            continue;

        // TODO : A bit flimsy
        var lang = langCapture.Groups[1].Value.Replace(" ", "").ToLowerInvariant();
        int endOfDeclationIndex = code.IndexOf(lang) + 3;
        int noCompileIndex = code.IndexOf("no-compile");
        if (noCompileIndex > 0)
            endOfDeclationIndex = noCompileIndex + 10;

        code = code.Substring(endOfDeclationIndex);
        
        LanguageSpec spec = LanguageSpec.Any;
        if (lang.Contains("py"))
            spec = LanguageSpec.Python3;
        else if (lang.Contains("cs"))
            spec = LanguageSpec.CSharp9;

        try
        {
            var sc = new SourceCode(spec, code);
            Code codeObject = sc.CreateCode();
            codeObject.Inputs.Add("__rhino_doc__", typeof(Rhino.RhinoDoc));

            var context = new BuildContext();
            if (!codeObject.TryBuild(context, out Diagnosis diagnosis))
            {
                Console.WriteLine($"FAIL --- {file} @ line {lineCount}");
                foreach(var diagnostic in diagnosis)
                {
                    Console.WriteLine(diagnostic.Message);
                }
                Console.WriteLine("\t---");
            }
        }
        catch (CodeLanguageNotFoundException cnfe)
        {
            Console.WriteLine($"FAIL --- {file} unknown lang : {spec}");
        }
        catch (CompileException ce)
        {
            foreach(var d in ce.Diagnosis)
                Console.WriteLine(d.Message);
        }
    }

    Console.WriteLine($"PASS --- {file}");
}
