# developer-rhino3d-com

This repo contains the contents of http://developer.rhino3d.com

The site is hosted on [GitHub Pages](https://pages.github.com/) which uses a static site generator called [Jekyll](http://jekyllrb.com/).


## Getting Started

These instructions cover running this project locally on both Mac OS X and Windows so that you can preview changes before pushing them to GitHub Pages.

First, navigate somewhere safe and clone the repository.

```
git clone https://github.com/mcneel/developer-rhino3d-com.git
```

If you are not comfortable using git on the command-line, then try [GitHub for Mac](https://mac.github.com/) and [GitHub for Windows](https://windows.github.com/). There's also the [git cheat sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf).

**IMPORTANT:** The site is branch-aware and automatically deployed by [Travis CI](https://travis-ci.org/mcneel/developer-rhino3d-com). **DO NOT PUSH TO THE `gh-pages` BRANCH!**

The `master` branch represents the current (_stable_) version of the site.  Changes to the `master` branch will be built by Travis and deployed to http://developer.rhino3d.com.  Other branches can be defined in `_config.yml` (under `version_branches`) and will be built and deployed into a subpath with the same name.  For example, if you push to the `wip` branch (representing RhinoWIP) then this site will be deployed to http://developer.rhino3d.com/wip.


### Mac OS X

Mac OS X Yosemite ships with Ruby and RubyGems, however it's [not wise](https://github.com/mcneel/developer-rhino3d-com/pull/2#issuecomment-112601698) to mess around with this installation. Instead, install your own Ruby using [Homebrew](http://brew.sh).

#### Install Homebrew and Ruby

As per the Homebrew website, install via the following one-liner (which will prompt you to install the Xcode Command Line Tools, if you don't already have them).

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Then we can brew Ruby.

```
brew install ruby
```

Now close and reopen the Terminal window to make sure the system knows about the new version of Ruby.

#### Install Jekyll

The [GitHub Pages Ruby Gem](https://github.com/github/pages-gem) provides the same version of Jekyll as exists on the GitHub Pages servers. This ensures we aren't accidentally using features that have either been deprecated or simply don't exist yet!

```
gem install github-pages
```

You can now serve your local copy of this site by running the following commands, remembering to replace `CLONE_DIRECTORY` with the location to which you checked out this repository.

```
cd CLONE_DIRECTORY
./script/server
```

Navigate to http://localhost:4000 in your browser to view the site.

(NOTE: The */api* folder generation is excluded locally to speed things up.)


### Windows

While **[Jekyll](http://jekyllrb.com/docs/windows/)** is not officially supported in Windows, it does work.  These instructions are based on the official _unofficial_ guide to [installing Jekyll on Windows](http://jekyll-windows.juthilo.com/).

#### Install Ruby and Ruby DevKit

Go to http://rubyinstaller.org/downloads/ and download the installer for Ruby 2.1.X that matches your system architecture (x86/x64).

At the "Installation Destination and Optional Tasks" dialog, make sure to check the **"Add Ruby executable to your PATH"** box.

Then, from the same page download the Development Kit that corresponds to your Ruby installation. Jekyll won't be fully functional without this.

Run the self extracting archive, entering the path `C:\RubyDevKit` when prompted.

To initialize and install the DevKit, open up a command prompt and roll up your sleeves...

```
cd C:\RubyDevKit
ruby dk.rb init
ruby dk.rb install
```

#### Install Jekyll and serve

As with OS X, install the GitHub Pages Ruby Gem, navigate to the clone directory and run jekyll.

```
gem install github-pages
cd CLONE_DIRECTORY
jekyll serve
```

## Next Steps

Once you have cloned or forked this repository and are able to build it locally, please read the following guides:

- [How This Site Works](http://developer.rhino3d.com/guides/general/how_this_site_works/)
- [Developer Docs Style Guide](http://developer.rhino3d.com/guides/general/developer_docs_style_guide/)
