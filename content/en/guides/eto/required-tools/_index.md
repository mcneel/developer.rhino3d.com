+++
aliases = [ ]
authors = [ "callum", "curtis" ]
categories = [ "Eto" ]
keywords = [ "rhino", "developer", "eto", "ui", "ux" ]
languages = [ "C#", "Python" ]
sdk = "eto"
type = "guides"
title = "Required Tools"
description = "Getting set up with Eto tools"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]

+++

# Inside Rhino

## Scripting in the Script Editor (Rhino or GH) {{% recommended-label %}}

The script editor offers very quick ways to write, test, build and publish plugins with Eto UIs from Rhino or Grasshopper (As of Rhino 8). It is recommended to use this when learning.

## Working from a C# Rhino Plugin

If you are not familiar with Rhino, or setting up Rhino plugins, it is advised to read this guide on creating your first plugin before diving into Eto.

- [Your First Plugin Windows](../../rhinocommon/your-first-plugin-windows/)
- [Your First Plugin Mac](../../rhinocommon/your-first-plugin-mac/)

One you have a working plugin, it would be best to create a new command you can use for debugging.

# Outside of Rhino
If you wish to work on eto outside of Rhino, you'll need to install some tools.

Open up your command line and run the following line.

```
dotnet new install Eto.Templates
```

# Workflow Recommendations

## Feedback loop
The shorter the loop between `Code Written` → `File Saved` → `UI Updated`, the quicker and easier it will be for you to try, experiment and learn.

## Hot Reload in C#

Hot reload makes this much much easier and quicker as you can change your UI without having to recompile, and re-run a command, which gets repetative and tiring very quickly.

Within Rhino, Hot Reload is only available on Windows, and works best with Visual Studio.

Outside of Rhino, Hot Reload works on both platformss as of net8.0 onwards, for Mac this means Visual Studio Code.

### Extending Hot Reload (Advanced)
This section is a little more advanced, is not mandatory, and can be safely skipped without impacting any of the other guides.

The below code can be copied into a new file in your project, and will automatically call any private or internal `InitializeControls` method on any Eto.Forms. Meaning if you set up your form/dialog correctly, you can have Hot Reload update the entire form allowing for very quick experimentations.

 <!-- TODO : Add Video. -->

``` cs
using System;
using System.Collections.Concurrent;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

#if NET
[assembly: System.Reflection.Metadata.MetadataUpdateHandler(typeof(Eto.HotReloadService))]

namespace Eto;

public static class HotReloadService
{
	static event Action<Type[]> Update; 

	public static void Initialize()
	{
		Eto.Style.Add<Container>(null, container =>
		{
			var initializeControls = container.GetType().GetMethod("InitializeControls", BindingFlags.NonPublic | BindingFlags.Instance | BindingFlags.DeclaredOnly);
			if (initializeControls == null)
				return;

			void DoUpdate(Type[]? types)
			{
				try

				{
					if (types.Contains(container.GetType()))
					{
						initializeControls?.Invoke(container, null);
					}
				}
				catch
				{
				}
			};
			container.Load += (sender, e) => Update += DoUpdate;
			container.UnLoad += (sender, e) => Update -= DoUpdate;
		});
	}

	internal static void ClearCache(Type[]? updatedTypes)
    {
    }

    internal static void UpdateApplication(Type[]? updatedTypes)
    {
		Application.Instance?.Invoke(() => Update?.Invoke(updatedTypes));
    }
}

#endif
```