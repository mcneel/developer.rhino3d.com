+++
title = "RhinoCode Command Line Interface"
description = "Provides information on using rhinocode command line utility that shipped with rhino"
authors = ["ehsan"]

[included_in]
platforms = [ "Windows", "Mac" ]
since = 8

[page_options]
byline = true
toc = true
toc_type = "single"
block_webcrawlers = false
+++

<style>
    .main-content img { zoom: 50%; }
    code {
        background-color: #efefef;
        padding-left: 5px;
        padding-right: 5px;
        border-radius: 3px;
    }

    .language-plaintext {
        font-size: .9em;
    }
</style>

Rhino3D (>=8.11) ships `rhinocode` command line utility (cli) that provides access to Rhino's scripting infrastructure. This utility communicates with a script server that is running inside of Rhino.

{{< call-out "note" "Note" >}}
For performance reasons, the script server is not started on Rhino launch. You can use the `StartScriptServer` command to start the server. Add it to Rhino startup commands to force starting server when starting Rhino
{{< /call-out >}}

`rhinocode` can provide information about running instances of Rhino, run scripts of any supported language in a Rhino instance, and build projects created in Rhino script editor into Rhino and Grasshopper plugins.

To run `rhinocode`:

- Make sure script server is started by running `StartScriptServer` in Rhino.

On Windows:
- Add `%PROGRAMFILES%\Rhino 8\System` to user or system `PATH` environment variable. Then open a terminal and run `rhinocode`

On macOS:
- Depending on the type of shell you are using, add `/Applications/Rhino 8.app/Contents/Resources/bin` to the `PATH` environment variable. Then reload the terminal and run `rhinocode`

If, for whatever reason, you do not want to modify the `PATH` environment variable, navigate to Rhino installation folder inside terminal and run `.\rhinocode` from there.


Test running `rhinocode` by specifying `-V` argument to get the version. Under current implementation, the version matches version of Rhino that ships this utility:

```text
$ rhinocode -V
8.11.24224
```

## Overview

Running `rhinocode --help` would print out an overview of subcommands and their descriptions (Actual message might be different from below depending on the utility version):


```text
$ rhinocode --help
Usage:  rhinocode [<OPTIONS>] <COMMAND> <ARGUMENTS>

RhinoCode command line interface

Commands:
  list                   List all running instances of Rhino3D
  command                Run given command in Rhino3D
  script                 Run given script in Rhino3D
  project                Manage and publish Rhino3D projects

Options:
  -V, --version                   Print version of this utility
  -v, --verbose                   Enable verbose reporting
  -r, --rhino <RHINO-ID>          Use this instance of Rhino3D (get id from list command)
  -d, --debug                     Debug outputs
  -t, --trace                     Trace outputs

Run 'rhinocode COMMAND --help' for more information on a command
```

You can get further help in each individual subcommand by adding the `--help` flag:

```text
$ rhinocode script --help
Usage:  rhinocode script <PATH>

Run given script in Rhino3D

Arguments:
  <PATH>                   Full path of script to be executed

Examples:
  > rhinocode script C:\path\to\script.py
```

## Listing Rhino Instances

Use `list` subcommand to list all running instance of Rhino. Each instance has a Process ID (PID) and a unique identifier (ID). The report also shows the name and path of any document that is open inside the Rhino instance to better help identifying each Rhino:

You can use ID with `--rhino` option to run a subcommand on that specific Rhino instance.

```text
$ rhinocode list
       PID ID                             DOC                  PATH
     75029 rhinocode_remotepipe_75029     Sphere.3dm           C:\path\to\rhinofiles\Sphere.3dm
```

Add `--json` flag to get results in JSON. This can be used to parse the results of this command easier in your custom integrations:

```text
$ rhinocode list --json
[
  {
    "pipeId": "rhinocode_remotepipe_75029",
    "processId": 75029,
    "processName": "Rhinoceros",
    "processVersion": "8.11.24224.1000",
    "processAge": 103,
    "activeDoc": {
      "title": "Sphere.3dm",
      "location": "C:\\path\\to\\rhinofiles\\Sphere.3dm"
    },
    "activeViewport": "Perspective",
    "$meta": {
      "version": "1.0"
    },
    "$type": "status"
  }
]
```
## Running Rhino Commands

Use `command` subcommand to run a rhino command in an instance of Rhino. This example runs the `Circle` command in Rhino with a few arguments to draw a circle:

```text
$ rhinocode command "_circle 0 0 0 20"
```

If you have multiple instance of Rhino running, you can specify which instance to run the command on using `--rhino` option:

```text
$ rhinocode --rhino rhinocode_remotepipe_75029 command "_circle 0 0 0 20"
```

## Running Scripts

Use `command` subcommand to run a rhino command in an instance of Rhino:

```text
$ rhinocode script C:\path\to\scripts\foo.py
$ rhinocode script C:\path\to\scripts\foo.cs
$ rhinocode script C:\path\to\scripts\foo.py2
```

If you have multiple instance of Rhino running, you can specify which instance to run the command on using `--rhino` option:

```text
$ rhinocode --rhino rhinocode_remotepipe_75029 script C:\path\to\scripts\foo.py
```

## Working With Projects

{{< call-out "note" "Note" >}}
- `project` command builds projects without requiring a running instance of Rhino. It can be used is build scripts in you CI/CD pipeline.
- See [Creating Rhino Projects](/guides/scripting/projects-create) and [Creating Rhino and Grasshopper Plugins](/guides/scripting/projects-publish) for more information on creating projects in Rhino script editor.
{{< /call-out >}}

Use `project` subcommand to work with projects created in the Rhino script editor.

### Build a Project

The `build` subcommand build Rhino and Grasshopper plugins from a project. The project file only stores references to scripts, Grasshopper definitions, and language libraries so these resources can be updated outside of the project without affecting the project file itself. The most recent state of these references is used when building a project.

```text
$ rhinocode project build C:\path\to\projects\MyTools.rhproj
  0% - Preparing project
 10% - Preparing build path
 20% - Preparing plugin assembly
 50% - Preparing grasshopper plugin assembly
 60% - Adding shared resources
 90% - Creating yak package
100% - Complete
```

You can furthur customize the build by providing these options:

- Build Version `--buildversion <BUILD-VERSION>`
- Build Target `--buildtarget <BUILD-TARGET>`
- Build Path `--buildpath <BUILD-PATH>`

See `rhinocode project --help` for more information and examples on each of these options:

```text
Options:
  -bv, --buildversion <BUILD-VERSION>  Build version formatted as <major>.<minor>
                                       with optional <patch>, <prerelease>, and <build> numbers
                                       formatted as <major>.<minor>.<patch>-<prerelease>+<build>
                                       Examples: 0.1
                                                 0.1.1234
                                                 0.1.1234-beta
                                                 0.1.1234+8989
                                                 0.1.1234-beta+8989

  -bt, --buildtarget <BUILD-TARGET>    Target Rhino version formatted as <major>.<minor>
                                       with optional <operating-system>
                                       formatted as <major>.<minor>-<operating-system>
                                       Examples: 8.*
                                                 8.10
                                                 8.8-macOS
                                                 8.9-mac

  -bp, --buildpath <BUILD-PATH>        Absolute or relative build path
                                       Examples: .\mybuild
                                                 C:\path\to\mybuild
```

The build folder (depends on build target) will contain the generated plugins as well as a yak package that packs the plugins and other resources:

- YAK Package: `mytools-0.1.18292.8990-rh8-any.yak`
- Rhino Plugin containing commands: `MyTools.rhp`
- Rhino Toolbar Definition: `MyTools.rui`
- Grasshopper plugin containing components: `MyTools.Components.gha`

Use `yak` command line utility that is shipped with Rhino to push the `.yak` package to your desired package server.

{{< call-out "note" "Note" >}}
See [Pushing a Package to the Server](/guides/yak/pushing-a-package-to-the-server) on how to publish `.yak` files to package server
{{< /call-out >}}

To get a more verbose report during the build process use the `-d|--debug` or `-t|--trace` options:

```text
rhinocode -t project build C:\path\to\projects\MyTools.rhproj
```
