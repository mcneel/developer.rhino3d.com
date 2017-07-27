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
order: 1
keywords: ['developer', 'yak']
layout: toc-guide-page
---

<div class="bs-callout">

<strong>Note</strong>: Yak is cross-platform. Not everything is hooked up on the Mac side
yet, however. So, for now, this guide is aimed at <strong>Windows users only</strong>.

</div>

## Authentication

Before you can push a package to the server, you need to authorize the Yak CLI
tool using your Rhino Account.

```commandline
> "C:\Program Files\Rhino WIP\System\Yak.exe" login
```

A browser tab should open asking you to log in to Rhino Accounts (assuming you
are not already logged in). The next window will ask you to give "Yak" access to
your account.

- **View basic info about you**: This scope is used to retrieve your name,
  locale and profile picture. This information will be used in the future, when
  the package database has a graphical interface.
- **Verify your identity**: Used for authentication when querying package
  ownership.

## Push!
