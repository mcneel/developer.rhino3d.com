---
title: Creating and deploying plugin toolbars
description: This guide covers the creation and deployment of plugin toolbars.
author: dale@mcneel.com
apis: ['RhinoCommon']
languages: ['C#']
platforms: ['Windows']
categories: ['Advanced']
order: 1
keywords: ['RhinoCommon', 'Rhino', 'Toolbar', 'Plugin']
layout: toc-guide-page
---

# {{ page.title }}

{{ page.description }}

## Question

How can I create one or more toolbars for my plugin, and how can I deploy these toolbars with my plugin?

## Answer

If you want to create Rhino-style toolbars, then use Rhino's **Toolbar** command. You can save your custom toolbars in your own Rhino User Interface (RUI) file. For details on creating toolbars, see the Rhino help file.

If you give your custom RUI file the exact same name as the plug-in RHP file and install it in the folder containing the RHP file, then Rhino will automatically stage it to a writable location and open it the first time your plugin loads.

## More Information

The first time a plug-in is loaded, Rhino looks for an RUI file with the same name as the plug-in. If it is found, it is copied to the following location and opened:
```
"%APPDATA%\McNeel\Rhinoceros\<version>\Plug-ins\[plug-in name] ([plug-in UUID)\settings" 
```
It is copied, or staged, to ensure that the file is writable and to provide a way to revert to the original, or default, RUI file if needed.

You can revert to the original, or default, RUI file by deleting the RUI file in %APPDATA% folder and then and restarting Rhino, which will cause the file to be staged again, as the file no longer exists.

Note, there is additional code in Rhino that saves the name of RUI files closed by the user. If a user closes an RUI and the RUI file is associated with a plug-in, the file name goes on a list so that Rhino does not automatically open the RUI file in the future. The logic is if the user closed the file, we don't want to keep loading it every time Rhino starts.

If you uninstall the plugin and manually close the RUI file you are telling Rhino you no longer want to auto-load the RUI file which is why it does not open when you re-install. If you were to uninstall and delete the %APPDATA% RUI file then re-install the RUI file would open.

Also note, if you update your plug-in, Rhino will not re-stage the RUI file because it already exists. You can get Rhino to re-stage the RUI file by deleting it in %APPDATA% and restarting which will cause Rhino to copy the file again since it no longer exists. This can be done prograqmatically by adding the following code to your plugin object's **OnLoad** override.

## Example

```cs
/// <summary>
/// Called when the plugin is being loaded.
/// </summary>
protected override LoadReturnCode OnLoad(ref string errorMessage)
{
  // Get the version number of our plugin, that was last used, from our settings file.
  var plugin_version = Settings.GetString("PlugInVersion", null);

  if (!string.IsNullOrEmpty(plugin_version))
  {
    // If the version number of the plugin that was last used does not match the
    // version number of this plugin, proceed.
    if (0 != string.Compare(Version, plugin_version, StringComparison.OrdinalIgnoreCase))
    {
      // Build a path to the user's staged RUI file.
      var sb = new StringBuilder();
      sb.Append(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData));
      sb.Append("\\McNeel\\Rhinoceros\\5.0\\Plug-ins\\");
      sb.AppendFormat("{0} ({1})", Name, Id);
      sb.Append("\\settings\\");
      sb.AppendFormat("{0}.rui", Assembly.GetName().Name);

      var path = sb.ToString();

      // Verify the RUI file exists.
      if (File.Exists(path))
      {
        try
        {
          // Delete the RUI file.
          File.Delete(path);
        }
        catch
        {
          // ignored
        }
      }

      // Save the version number of this plug-in to our settings file.
      Settings.SetString("PlugInVersion", Version);
    }
  }

  // After successfully loading the plugin, if Rhino detects a plugin RUI
  // file, it will automatically stage it, if it doesn't already exist.

  return LoadReturnCode.Success;
}
```


