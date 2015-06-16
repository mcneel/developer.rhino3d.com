# developer-rhino3d-com

This repo contains the contents of http://mcneel.github.io/developer-rhino3d-com

The site is hosted on [GitHub Pages](https://pages.github.com/) using [Jekyll](http://jekyllrb.com/) a static site generator.  

## Getting Started

These instructions cover running this project locally on the OS X and on Windows. Running on OS X is a bit more straight forward. These instructions are in flux with the Windows version.

If you are not proficient with command-line git, GitHub has clients for [OS X](https://mac.github.com/) and [Windows](https://windows.github.com/).  [Sourcetree](https://www.sourcetreeapp.com/) is a more full-featured (but also more complicated) client.

![OS X Instructions](https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/images/mac_logo_small.png) 

#### Authoring & Testing this site locally on your Mac

##### clone the ```https://github.com/mcneel/developer-rhino3d-com.git``` repo:  
 - notice that 'gh-pages' is the only branch.  Everything committed to this branch is automatically published.
 - find the docs [here](http://mcneel.github.io/developer-rhino3d-com).  

##### Requirements:
 - [Ruby](http://www.ruby-lang.org/en/downloads/) probably already on your mac.  
 - [RubyGems](http://rubygems.org/pages/download)  
 - [GitHub Pages Gem](https://github.com/github/pages-gem)

##### Using Jekyll: serving / building

Open Terminal and cd to the folder that contains the cloned developer-rhino3d-com.git repository.

  - launch webserver:  
    ```jekyll serve```

    Once Jekyll has served the page it will print: ```http://127.0.0.1:4000/developer-rhino3d-com```. 
    Local changes to the repository should be reflected upon a page-refresh of the locally served page.

![Windows Instructions](https://github.com/mcneel/developer-rhino3d-com/blob/gh-pages/images/win_logo_small.png) 
#### Authoring & Testing this site locally on Windows

**[Jekyll](http://jekyllrb.com/docs/windows/)** is the main tools to compile and serve the website.  While not officially supported in Windows, it does work.  These instructions are an based on, but updated from the original instructions to [install Jekyll on Windows](http://jekyll-windows.juthilo.com/)

##### Install Ruby: 2.1.6 (x86 or x64) - http://rubyinstaller.org/downloads/

Use Ruby 2.1.X installers. These provide a stable language and a extensive list of packages (gems) that are compatible and updated.

When at the "Installation Destination and Optional Tasks" dialog, make sure to check the **"Add Ruby executable to your PATH"** box.
 
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
These insturcutions were written using Python 2.7. Python is required for ```pygments.rb``` used by the Liquid templating engine.
  1. Download and install the appropriate Python for Windows.
  2. Add the Python directory to the Windows Environment Path.
 
##### Install Jekyll and Git-pages
  1. Using the Commandline in Windows
  2. Type: ```gem install jekyll```
  3. After a minute it should go through a large install process
  4. Type: ```gem install git-pages```

##### Using Jekyll: serving / building

Open command line and cd to the folder that contains the cloned developer-rhino3d-com.git repository.

  - launch webserver:  
    ```jekyll serve```

    Once Jekyll has served the page it will print:
    ```http://127.0.0.1:4000/developer-rhino3d-com```.  Local changes to the repository should be reflected upon a page-refresh of the locally served page.








