# developer-rhino3d-com

This repo contains the contents of http://mcneel.github.io/developer-rhino3d-com

The site is hosted on [GitHub Pages](https://pages.github.com/) and we are using [Jekyll](http://jekyllrb.com/) as our static site generator.  Jekyll is what runs under GitHub Pages but we also chose it because it seems to be the standard among [many](https://staticsitegenerators.net/).  Jekyll was first conceived for blog sites but also well suited for documentation sites.  The idea is to create the structure using a combination of html and markdown files and have the content, [guides]({{ '/guides' | prepend: site.baseurl }}) and [samples]({{ '/samples' | prepend: site.baseurl }}) (for now), be in markdown (and LaTeX?) only if possible for maximum portability in case we later switch platform.  [Liquid](https://github.com/Shopify/liquid/wiki) is the template engine in Jekyll and we'll also use [Bootstrap](http://getbootstrap.com/).  

## Getting Started

These instructions cover running this project on the Mac OSX client and on Windows. Running on Mac OS X is a bit more straight forward. These instructions are a in flux with the Windows version.

If you are not proficient with command-line git, GitHub has a [client for OS X](https://mac.github.com/).

![Mac Instructions](https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/images/mac_logo_small.png) 
#### Testing and authoring gh pages locally on your Mac OS X.

##### clone the ```https://github.com/mcneel/developer-rhino3d-com.git``` repo:  
 - notice that 'gh-pages' is the only branch.  Everything committed to this branch is automatically published.
 - find the docs [here](http://mcneel.github.io/developer-rhino3d-com).  

##### Requirements: (instead of following the links below I installed with [homebrew](http://brew.sh/))
 - [Ruby](http://www.ruby-lang.org/en/downloads/) probably already on your mac.  
 - [RubyGems](http://rubygems.org/pages/download)  
 - [GitHub Pages Gem](https://github.com/github/pages-gem)

##### Install GitHub Pages Gem  
 ```bash
   https://github.com/github/pages-gem
 ```

(these instructions need work/updating)

##### Using Jekyll: serving / building

Open Terminal and cd to the folder that contains the cloned developer-rhino3d-com.git repository.

  - launch webserver:  
    ```jekyll serve```

    Once Jekyll has served the page it will print:
    ```http://127.0.0.1:4000/developer-rhino3d-com``` (for example).  Local changes to the repository should be reflected upon a page-refresh of the locally served page.

  - build w/o plugins.  gh pages doesn't allow plugins:  
    ```jekyll build --safe```


![Windows Instructions](https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/images/win_logo_small.png) 
#### Testing and authoring gh pages locally on your Windows computer before pushing them to GitHub web.

**[Jekyll](http://jekyllrb.com/docs/windows/)** is the main tools to compile and serve the website.  While not officially supported in Windows, it does work. There are many prodcuts to install to prepare the computer for Jekyll. These instructiosn are an based on, but updated from the original instructions to [install Jekyll on Windows](http://jekyll-windows.juthilo.com/)

##### Install Ruby: 2.1.6 (x86 or x64) - http://rubyinstaller.org/downloads/

We recommend you use Ruby 2.1.X installers. These provide a stable language and a extensive list of packages (gems) that are compatible and updated.

  1. **Important** - This file may downloaded as a blocked application in Windows.  
   1. Move the exe out of the downloads folders. 
   2. Right-click and go to propterties.
   3.  If it is activated, click on Unblock.
  2.  Start the installer.
  3. When at the "Installation Destination and Optional Tasks" dialog, make sure to check the **"Add Ruby executable to your PATH"** box.
 
##### Install Ruby DevKit - http://rubyinstaller.org/downloads/

  1. On Ruby page under the Development Kit heading along the left column of the page, find the kit that corresponds to your operating system and Ruby installation.  For Ruby v2.0.0 the file will begin with ```DevKet-mingw64```.
  2. Download the self extracting archive.
  3. When executing the tile, it will ask for a directory. Enter a path with no spaces, for instance ```C:\rubydevkit\```
 
##### Initialize the DevKit and bind it to Ruby

  1. Open the Commandline as Administrator in Windows
  2. Navigate to the RubyDevKit folder  ```C:\rubydevkit\```
  3. Type the command to initialize 
    ```ruby dk.rb init```
  4. A message should apear that reads  
    ```Intialization complete!...```

##### Install Python - https://www.python.org/
These insturcutions were written using Python 2.7. As of February, 2015, there is a new Python 3.x available.  Python is required for ```pygments.rb``` used by the Liquid templating engine.
  1. Downlaod the appropriate Python for Windows.
  2. Install Python.
  3. Add the Python directory to the Windows Environment Path.
 
##### Install Jekyll
  1. Using the Commandline in Windows
  2. Type: ```gem install jekyll```
  3. After a minute it should go through a large install process

##### Install Git-Pages
  1. Using the Commandline in Windows
  2. Type: ```gem install git-pages```
  3. After a minute it should go through a large install process

##### Using Jekyll: serving / building

Open Terminal and cd to the folder that contains the cloned developer-rhino3d-com.git repository.

  - launch webserver:  
    ```jekyll serve```

    Once Jekyll has served the page it will print:
    ```http://127.0.0.1:4000/developer-rhino3d-com``` (for example).  Local changes to the repository should be reflected upon a page-refresh of the locally served page.








