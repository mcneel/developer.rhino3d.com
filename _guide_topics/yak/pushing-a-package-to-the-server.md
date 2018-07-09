---
# title: Creating a Grasshopper Plug-In Package
description: >
  This is a step by step guide to pushing a package to the Yak server.
authors: ['Will Pearson']
author_contacts: ['will']
sdk: ['Yak']
languages: # empty
platforms: ['Windows']
categories: ['Step By Step']
order: 2
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="alert alert-info" role="alert">
<strong>Note:</strong> Yak is cross-platform. Not everything is hooked up on the
Mac side yet, however. So, for now, this guide is aimed at <strong>Windows users
only</strong>.
</div>

## Authentication

Before you can push a package to the server, you need to authorize the Yak CLI
tool using your Rhino Account.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" login
```

A browser tab should open asking you to log in to Rhino Accounts (assuming you
are not already logged in). The next window will ask you to give "Yak" access to
your account.

- **View basic info about you**: This scope is used to retrieve your name,
  locale and profile picture. This information will be used in the future, when
  the package database has a graphical interface.
- **Verify your identity**: Used for authentication when querying package
  ownership.

Once you've accepted, the browser window will close itself. Yak has retrieved an
OAuth token from Rhino Accounts and has stored this on your computer.

- Mac - `~/.mcneel/yak.yml`
- Windows - `%APPDATA%\McNeel\yak.yml`

<div class="alert alert-info" role="alert">
<strong>Note:</strong> For security, the OAuth token is valid for a limited time
only. Don't be surprised if the Yak CLI tool requires you to log in again after
30 days or so.
</div>

## Push!

Now that you're logged in, it's possible to push a package to the server. I'll
use the package created in the
[previous guide](../creating-a-grasshopper-plugin-package) as an example.

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" push marmoset-1.0.0.yak
```

Currently (v0.2), this command doesn't produce any output on success.

You can check that your package has been successfully pushed by searching for
it. You should see the name and version number of the package that you just
pushed. 🤞

```commandline
> "C:\Program Files\Rhino 6\System\Yak.exe" search --all --prerelease marmoset

marmoset (1.0.0)
```

## Troubleshooting

There are a few reasons why pushing a package might not work.

- Invalid `manifest.yml`

  _The error message should be self explanatory. Fix it up and try again! You
  can also try validating the YAML syntax itself with a
  [linter](http://www.yamllint.com)._

- The package name already exists, but you're not an **owner**.

  _Only package **owners** are permitted to push new versions of their packages.
  When a user pushes the first version of a package, they become its **owner**.
  In the future it will be possible to grant **ownership** to other users.
  Package names are case-insensitive._

- The package version already exists.

  _In order to prevent disruption to others who are using one of your packages,
  it's not possible to delete or overwrite versions. Roll the version number and
  let your users know that there's something new for them to try!_

  ---

  ## Related Topics

  - [Yak Guides and Tutorials]({{ site.baseurl }}/guides/yak/)
  - [Creating a Grasshopper Plug-in Package]({{ site.baseurl }}/guides/yak/creating-a-grasshopper-plugin-package/)
  - [Creating a Rhino Plug-in Package]({{ site.baseurl }}/guides/yak/creating-a-rhino-plugin-package/)
