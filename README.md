# developer-rhino3d-com

[![Build Status](https://travis-ci.org/mcneel/developer-rhino3d-com.svg?branch=5)](https://travis-ci.org/mcneel/developer-rhino3d-com)

This repo contains the contents of http://developer.rhino3d.com

The site is hosted on [GitHub Pages](https://pages.github.com/) which uses a static site generator called [Jekyll](http://jekyllrb.com/).


## Getting Started

These instructions cover running this project locally on both macOS and Windows so that you can preview changes before pushing them to GitHub Pages.

First, navigate somewhere safe and clone the repository.

```
git clone https://github.com/mcneel/developer-rhino3d-com.git
```

If you are not comfortable using git on the command-line, then try [GitHub for Mac](https://mac.github.com/) and [GitHub for Windows](https://windows.github.com/). There's also the [git cheat sheet](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf).

**IMPORTANT:** The site is branch-aware and automatically deployed by [Travis CI](https://travis-ci.org/mcneel/developer-rhino3d-com). **DO NOT PUSH TO THE `gh-pages` BRANCH!**

The current (_stable_) version Rhino is defined in the `stable:` field in the `_config.yml` file.  The `n` branch that corresponds to the stable release is built and deployed to http://developer.rhino3d.com.  

The `master` branch represents the WIP version of the site.  Changes to the `master` branch will be built by Travis and deployed to http://developer.rhino3d.com/wip.  

Branches are defined in `_config.yml` (under `version_branches`) and will be built and deployed into a subpath with the same name; for example: the `5` branch is built and deployed to http://developer.rhino3d.com/5.

### macOS

macOS ships with Ruby and RubyGems, however it's [not wise](https://github.com/mcneel/developer-rhino3d-com/pull/2#issuecomment-112601698) to mess around with this installation. Instead, install your own Ruby using [Homebrew](http://brew.sh) (and optionally [rbenv](#install-ruby-the-rbenv-way)).

#### Install Homebrew

As per the Homebrew [website](http://brew.sh), install via the following one-liner (which will prompt you to install the Xcode Command Line Tools, if you don't already have them).

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### Install Ruby (the easy way)

**Note**: Since OS X 10.11 (El Capitan) we've seen failures during the `gem install` step (`ERROR: While executing gem ... (Errno::EINVAL)`) on machines that didn't previously have homebrew installed. Using [rbenv](#install-ruby-the-rbenv-way) seems to solve this.

Simply _brew_ Ruby.

```
brew install ruby
```

Now close and reopen the Terminal window to make sure the system knows about the new version of Ruby and skip to [installing Jekyll](#install-jekyll).

#### Install Ruby (the rbenv way)

This is a slightly more advanced method for installing ruby which allows you to easily switch between ruby versions.

Install [rbenv](https://github.com/rbenv/rbenv) and [ruby-build](https://github.com/rbenv/ruby-build) using homebrew:
```
brew install rbenv ruby-build
```

Run `rbenv init` which will prompt you to add `eval "$(rbenv init -)"` to `~/.bash_profile`. Do this.

Install ruby (2.3.0 will do, for now):

```
rbenv install 2.3.0
```

Check that everything worked as expected:

1. `ruby -v` – should return something like `ruby 2.3.0p0 (2015-12-25 revision 53290) [x86_64-darwin15]`
2. `which ruby` – should return something like `/Users/will/.rbenv/shims/ruby` (**not `/usr/bin/ruby` or `/usr/local/bin/ruby`**)

#### Install Jekyll

The [GitHub Pages Ruby Gem](https://github.com/github/pages-gem) provides the same version of Jekyll as exists on the GitHub Pages servers. This ensures we aren't accidentally using features that have either been deprecated or simply don't exist on GitHub's servers yet!

```
gem install github-pages
```

You can now serve your local copy of this site by running the following commands, remembering to replace `CLONE_DIRECTORY` with the location to which you checked out this repository.

```
cd CLONE_DIRECTORY
script/server
```

Navigate to http://localhost:4000 in your browser to view the site.

**Note**: The `api` directory is excluded when previewing the site locally which speeds things up a bit!


### Windows

While [Jekyll](http://jekyllrb.com/docs/windows/) is not officially supported in Windows, it does work.  These instructions are based on the official _unofficial_ guide to [installing Jekyll on Windows](http://jekyll-windows.juthilo.com/).

Optionally, you can follow the directions found on [Setting up your GitHub Pages site locally with Jekyll - Windows](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#platform-windows) to use Bundler to install Jekyll.

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

As with macOS, install the GitHub Pages Ruby Gem, navigate to the clone directory and run jekyll.

```
gem install github-pages
cd CLONE_DIRECTORY
jekyll serve
```

## Next Steps

Once you have cloned or forked this repository and are able to build it locally, please read the following guides:

- [How This Site Works](http://developer.rhino3d.com/guides/general/how-this-site-works/)
- [Developer Docs Style Guide](http://developer.rhino3d.com/guides/general/developer-docs-style-guide/)
