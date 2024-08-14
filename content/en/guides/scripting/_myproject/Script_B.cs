// #! csharp
using System;
using System.IO;

using Rhino;

var id = new Guid("E73D16E6-A2D4-4917-93E7-AEBEAC2F38F5");
string pluginFile = Rhino.PlugIns.PlugIn.PathFromId(id);
string pluginPath = Path.GetDirectoryName(pluginFile);
string dataFile = Path.Combine(pluginPath, "shared", "data.json");

Console.WriteLine(dataFile);
Console.WriteLine(File.Exists(dataFile));