+++
aliases = ["/en/5/guides/yak/pushing-a-package-to-the-server/", "/en/6/guides/yak/pushing-a-package-to-the-server/", "/en/7/guides/yak/pushing-a-package-to-the-server/", "/wip/guides/yak/pushing-a-package-to-the-server/"]
authors = [ "will" ]
categories = [ "Getting Started" ]
description = "This is a step by step guide to pushing a package to the package server."
keywords = [ "developer", "yak" ]
sdk = [ "Yak" ]
title = "Pushing a Package to the Server"
type = "guides"
weight = 20
override_last_modified = "2020-11-12T12:17:36Z"

[admin]
TODO = ""
origin = ""
picky_sisters = ""
state = ""

[included_in]
platforms = [ "Windows", "Mac" ]
since = 0

[page_options]
byline = true
toc = true
toc_type = "single"

+++

See the [package server](/guides/yak/the-package-server/) guide for more information about the McNeel public package server.

{{< call-out "note" "Note" >}}
Yak is cross-platform. The examples below are for Windows.
For Mac, replace the path to the Yak CLI tool with
<code>"/Applications/Rhino {{< latest-rhino-version >}}.app/Contents/Resources/bin/yak"</code>.
{{< /call-out >}}



## Authentication

Before you can push a package to the server, you need to authorize the Yak CLI
tool using your Rhino Account.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" login
```

A browser tab should open asking you to log in to Rhino Accounts (assuming you
are not already logged in). The next window will ask you to give "Yak" access to
your account.

- **View basic info about you**: This scope is used to retrieve your name,
  locale and profile picture. This information will be used in the future, when
  the package database has a graphical interface.
- **Verify your identity**: Used for authentication when querying package
  ownership.
- **View your email address**: Your primary email address is stored so that you can be [added as an owner](../yak-cli-reference/#owner) of packages that others have published.

Once you've accepted, the browser window will close itself. Yak has retrieved an
OAuth token from Rhino Accounts and has stored this on your computer.

- Mac - `~/.mcneel/yak.yml`
- Windows - `%APPDATA%\McNeel\yak.yml`

{{< call-out "note" "Note" >}}
For security, the OAuth token is valid for a limited time
only. Don't be surprised if the Yak CLI tool requires you to log in again after
30 days or so.
{{< /call-out >}}

## Push!

Now that you're logged in, it's possible to push a package to the server. I'll
use the package created in the
[previous guide](../creating-a-grasshopper-plugin-package) as an example.

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push marmoset-1.0.0-rh6_18-any.yak
```

This command doesn't produce any output on success.

You can check that your package has been successfully pushed by searching for
it. You should see the name and version number of the package that you just
pushed. 🤞

```commandline
> "C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --all --prerelease marmoset

marmoset (1.0.0)
```

{{< call-out "note" "Note" >}}
If this is your first time, why not try pushing to the test server first?
```cmd
"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" push --source https://test.yak.rhino3d.com marmoset-1.0.0-rh6_18-any.yak

"C:\Program Files\Rhino {{< latest-rhino-version >}}\System\Yak.exe" search --source https://test.yak.rhino3d.com --all --prerelease marmoset

marmoset (1.0.0)
```
This server is wiped clean each night.
{{< /call-out >}}

## Troubleshooting

There are a few reasons why pushing a package might not work.

- Invalid `manifest.yml`

  _The error message should be self explanatory. Fix it up and try again! You
  can also try validating the YAML syntax itself with a
  [linter](http://www.yamllint.com)._

- The package name already exists, but you're not an **owner**.

  _Only package **owners** are permitted to push new versions of their packages.
  When a user pushes the first version of a package, they become its **owner**. Additional owners can be added with the [`owner`](../yak-cli-reference/#owner) command._

- The package version already exists.

  _In order to prevent disruption to others who are using one of your packages,
  it's not possible to delete or overwrite versions. Roll the version number and
  let your users know that there's something new for them to try!_

- Push something that you didn't mean to?

  _Use the [`yank` command](../yak-cli-reference/#yank) to unlist a specific version._

## Related Topics

- [The Package Server](/guides/yak/the-package-server/)
- [Creating a Grasshopper Plug-in Package](/guides/yak/creating-a-grasshopper-plugin-package/)
- [Creating a Rhino Plug-in Package](/guides/yak/creating-a-rhino-plugin-package/)
