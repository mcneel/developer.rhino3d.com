using System;
using System.IO;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Net;
using System.Linq;
using System.Collections.Generic;

namespace Launch
{
  public static class ShellHelper
  {
    public static string Bash(this string cmd)
    {
      var escapedArgs = cmd.Replace("\"", "\\\"");

      var process = new Process()
      {
        StartInfo = new ProcessStartInfo
        {
          FileName = "/bin/bash",
          Arguments = $"-c \"{escapedArgs}\"",
          RedirectStandardOutput = true,
          UseShellExecute = false,
          CreateNoWindow = true,
        }
      };

      process.Start();
      string result = process.StandardOutput.ReadToEnd();
      process.WaitForExit();

      return result;
    }
  }

  class Launch
  {
    public static string HugoExe
    {
      get
      {
        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
        {
          return "hugo.exe";
        } else
        {
          return "hugo";
        }
      }
    }

    public static string RepoRootPath
    {
      get {
#if DEBUG
        string pathToExe = System.IO.Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
        return Path.GetFullPath(Path.Combine(pathToExe, "..", "..", "..", "..", "..", "..", ".."));
#elif RELEASE
        string pathToExe = System.IO.Path.GetDirectoryName(System.Diagnostics.Process.GetCurrentProcess().MainModule.FileName);
        return Path.GetFullPath(Path.Combine(pathToExe, "..", "..", "..", ".."));
#endif
      }
    }

    public static string Url { get; set; }

    public static string RequiredHugoVersion
    {
      get
      {
        string requiredHugoVersion = "";

        string pathToForestrySettingsFile = Path.GetFullPath(Path.Combine(RepoRootPath, ".forestry", "settings.yml"));

        string line;

        System.IO.StreamReader file = new System.IO.StreamReader(pathToForestrySettingsFile);
        while ((line = file.ReadLine()) != null)
        {
          if (line.StartsWith("version: "))
          {
            string versionLine = line;
            requiredHugoVersion = versionLine.Split("version: ")[1].Trim();
          }
        }

        if (String.IsNullOrWhiteSpace(requiredHugoVersion))
        {
          Console.WriteLine("Unabled to detect HUGO_VERSION in .forestry/settings.yml");
          System.Environment.Exit(1);
        }
        else
        {
          Console.WriteLine("Required hugo version set to: {0}", requiredHugoVersion);
        }

        return requiredHugoVersion;
      }
    }

    public static string ParseHugoVersionNumber(string version)
    {
      string parsedVersion = "";

      if (version.StartsWith("Hugo Static Site Generator v"))
      {
        // Hugo Static Site Generator v0.71.1-A301F6B2/extended darwin/amd64 BuildDate: 2020-05-25T09:16:12Z
        parsedVersion = version.Split("Hugo Static Site Generator v")[1].Substring(0,6);
      }
      else
      {
        // hugo v0.83.1+extended darwin/amd64 BuildDate=unknown
        parsedVersion = version.Split("hugo v")[1].Substring(0,6);
      }

      return parsedVersion;
    }

    static bool GetHugo()
    {
      string requiredVersion = RequiredHugoVersion;

      string archive = "";
      string filename = "";
      if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
      {
        if (System.Runtime.InteropServices.RuntimeInformation.ProcessArchitecture == Architecture.Arm64) {
          archive = string.Format("hugo_extended_{0}_macOS-ARM64.tar.gz", requiredVersion);
        } else {
          archive = string.Format("hugo_extended_{0}_macOS-64bit.tar.gz", requiredVersion);
        }
        filename = "hugo.tar.gz";
      } else if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
      {
        archive = string.Format("hugo_extended_{0}_Windows-64bit.zip", requiredVersion);
        filename = "hugo.zip";
      } else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
      {        
        archive = string.Format("hugo_extended_{0}_Linux-64bit.tar.gz", requiredVersion);
        filename = "hugo.tar.gz";
      }

      string url = string.Format("https://github.com/gohugoio/hugo/releases/download/v{0}/{1}", requiredVersion, archive);

      Console.WriteLine("Looking for hugo: {0} ...", requiredVersion);

      string pathToHugo = Path.GetFullPath(Path.Combine(RepoRootPath, HugoExe));

      if (File.Exists(pathToHugo))
      {
        var proc = new Process
        {
          StartInfo = new ProcessStartInfo
          {
            FileName = pathToHugo,
            Arguments = "version",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
          }
        };

        proc.Start();
        string procOutput = "";
        while (!proc.StandardOutput.EndOfStream)
        {
          procOutput = proc.StandardOutput.ReadLine();
        }

        string localHugoVersion = ParseHugoVersionNumber(procOutput);

        Console.WriteLine("Found hugo ver: {0}", localHugoVersion);

        if (localHugoVersion == requiredVersion)
          return true;

        Console.WriteLine("hugo version mismatch detected...");
      }

      string archivePath = Path.GetFullPath(Path.Combine(RepoRootPath, filename));
      string tempPath = Path.GetFullPath(Path.Combine(RepoRootPath, "myhugo"));

      if (System.IO.Directory.Exists(tempPath))
        Directory.Delete(tempPath, true);

      Directory.CreateDirectory(tempPath);

      // Download Hugo
      using (var client = new WebClient())
      {
        Console.WriteLine("Downloading: {0} ...", filename);
        client.DownloadFile(url, Path.Combine(RepoRootPath, filename));
        Console.WriteLine("Download {0} complete.", filename);
      }

      // Decompress Hugo
      if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX) || RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
      {
        var proc = new Process
        {
          StartInfo = new ProcessStartInfo
          {
            FileName = "tar",
            Arguments = string.Format("-xvf {0} --directory {1}", archivePath, tempPath),
            UseShellExecute = false,
            RedirectStandardOutput = false,
            CreateNoWindow = true
          }
        };

        proc.Start();
        proc.WaitForExit();
      }
      else if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
      {
        System.IO.Compression.ZipFile.ExtractToDirectory(archivePath, tempPath);
      }

      File.Move(Path.GetFullPath(Path.Combine(tempPath, HugoExe)), Path.GetFullPath(Path.Combine(RepoRootPath, HugoExe)), true);

      if (System.IO.Directory.Exists(tempPath))
        Directory.Delete(tempPath, true);

      if (File.Exists(archivePath))
        File.Delete(archivePath);

      return true;
    }

    static void StopAllHugos()
    {
      if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
      {
        var proc = new Process
        {
          StartInfo = new ProcessStartInfo
          {
            FileName = "taskkill",
            Arguments = "/F /IM hugo.exe /T",
            UseShellExecute = false,
            RedirectStandardOutput = false,
            CreateNoWindow = true
          }
        };

        proc.Start();
        proc.WaitForExit();
      }
      else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX) || RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
      { 
        var grepForHugo = "ps | grep '[h]ugo'".Bash();        
        if (!string.IsNullOrEmpty(grepForHugo))
        {
          Console.WriteLine("Found previously running Hugos...");
          string[] outputLines = grepForHugo.Split(new[] { Environment.NewLine }, StringSplitOptions.None);

          outputLines = outputLines.SkipLast(1).ToArray();
          foreach (string line in outputLines)
          {
            string command = line.Split(" ")[3].Trim();
            if (command.StartsWith("hugo")) { // check to make sure this is actually a hugo command running here
              string pid = line.Split(" ")[0].Trim();
              string killCommand = "kill " + pid;
              Console.WriteLine("Killing hugo process {0}", pid);
              killCommand.Bash();
              System.Threading.Thread.Sleep(5000);
            }
          }
          Console.WriteLine("All Hugo processes stopped.");
          
        }
      }
    }

    static bool ServeHugo(string[] args)
    {
      string arguments = "";
      
      if (args.Length > 0)
      {
        foreach (string arg in args) {
          arguments += " ";
          arguments += arg;
        }
      } else
      {
        arguments = "serve";
      }

      using (var process = new Process
      {
        StartInfo = new ProcessStartInfo
        {
          FileName = HugoExe,
          Arguments = arguments,
          UseShellExecute = false,
          RedirectStandardOutput = true,
          RedirectStandardError = true,
          CreateNoWindow = true,
        }
      })
      {
        process.OutputDataReceived += (sender, args) => ConsoleOut(args.Data);
        process.ErrorDataReceived += (sender, args) => ConsoleOut(args.Data);

        process.Start();
        process.BeginOutputReadLine();
        process.BeginErrorReadLine();

        process.WaitForExit();
      }   

      return true;
    }

    static void ConsoleOut(string output)
    {
      Console.WriteLine(output);
    }

    public static void OpenBrowserToURL(string url)
    {
      try
      {
        Process.Start(url).WaitForExit();
      }
      catch
      {
        // hack because of this: https://github.com/dotnet/corefx/issues/10361
        if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
        {
          url = url.Replace("&", "^&");
          Process.Start(new ProcessStartInfo("cmd", $"/c start {url}") { CreateNoWindow = true }).WaitForExit();
        }
        else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
        {
          Process.Start("xdg-open", url).WaitForExit();
        }
        else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
        {
          Process.Start("open", url).WaitForExit();
        }
        else
        {
          throw;
        }
      }
    }

    public static bool CheckMaxFiles()
    {
      if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
      {
        var proc = new Process
        {
          StartInfo = new ProcessStartInfo
          {
            FileName = "launchctl",
            Arguments = "limit maxfiles",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true
          }
        };

        proc.Start();
        string procOutput = "";
        while (!proc.StandardOutput.EndOfStream)
        {
          procOutput = proc.StandardOutput.ReadLine();
        }

        if (procOutput.Contains("maxfiles    655360         1048576")) 
        {
          return true;
        } else {
          return false;
        }        
      } else
      {
        return true;
      }
    }

    public static Dictionary<string, string> StripNamedArgs(string[] args, string[] names)
    {
      Dictionary<string, string> results = new Dictionary<string, string>();

      foreach (string arg in args)
      {
        foreach (string name in names)
        {
          if (arg.StartsWith(name + "="))
            results[name] = arg.Split("=")[1];
        }
      }

      return results;
    }

    public static string UrlFromArgs(string[] args)
    {
      string location = "http://localhost:1313";
      string page = "";
      string language = "";
      string[] names = { "browse", "page", "language" };
      Dictionary<string, string> parameters = StripNamedArgs(args, names);

      if (parameters.ContainsKey("browse"))
        location = parameters["browse"];

      if (parameters.ContainsKey("page"))
        page = parameters["page"];

      if (parameters.ContainsKey("language"))
        language = parameters["language"];
      
      if (!string.IsNullOrWhiteSpace(page))
      {
        string root = RepoRootPath.Replace("\\", "/");
        page = page.Replace("\\", "/");
        page = page.Replace(root, "", StringComparison.InvariantCultureIgnoreCase);        
        page = page.Replace("/index.md", "/", StringComparison.InvariantCultureIgnoreCase);
        page = page.Replace("/_index.md", "/", StringComparison.InvariantCultureIgnoreCase);
        page = page.Replace(".md", "/", StringComparison.InvariantCultureIgnoreCase);

        // Special case: learn page
        if (page.EndsWith("learn.toml"))
          page = page.Replace("/learn.toml", "/", StringComparison.InvariantCultureIgnoreCase);

        // Special case: formats page
        if (page.EndsWith("formats.toml"))
          page = "/content/en/features/file-formats";

        if (page.StartsWith("/content"))
        {
          page = page.Substring(8);
        } else
        {
          return location;
        }

        if (!string.IsNullOrWhiteSpace(language))
          page = page.Replace(String.Format("/{0}", language), "", StringComparison.InvariantCultureIgnoreCase);

        char[] forwardSlash = { '/' };
        location = location.TrimEnd(forwardSlash) + "/" + page.TrimStart(forwardSlash);        
      }

      return location;
    }

    static void Main(string[] args)
    {
      Directory.SetCurrentDirectory(RepoRootPath);

      bool shouldServe = args[0].StartsWith("serve");      

      Url = UrlFromArgs(args);

      if (shouldServe)
      {
        StopAllHugos();
        GetHugo();
        if (CheckMaxFiles())
        {
          OpenBrowserToURL(Url);
          ServeHugo(args);
        }
        else
        {
          Console.WriteLine("vvvvvvvvvvvvvvvvvvv ERROR vvvvvvvvvvvvvvvvvvvv\nERROR: McNeel Developer - Hugo needs more files\nTo fix this:\n1. In VSCode, press Command+Shift+P, then Enter.\n2. Type Tasks and select Task: Run Task.\n3. From the list, select and run the hugo SetMaxFilesLimits (run once only) task - be sure to enter your password in the terminal window.\n4. Restart your computer.\n^^^^^^^^^^^^^^^^^^^ ERROR ^^^^^^^^^^^^^^^^^^^^");
        }
      } else
      {
        OpenBrowserToURL(Url);        
      }
      
    }
    
  }
}
