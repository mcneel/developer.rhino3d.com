# developer-rhino3d-com

This repo contains the contents of http://mcneel.github.io/developer-rhino3d-com

The site is hosted on [GitHub Pages](https://pages.github.com/) and we are using [Jekyll](http://jekyllrb.com/) as our static site generator.  Jekyll is what runs under GitHub Pages but we also chose it because it seems to be the standard among [many](https://staticsitegenerators.net/).  Jekyll was first conceived for blog sites but also well suited for documentation sites.  The idea is to create the structure using a combination of html and markdown files and have the content, [guides]({{ '/guides' | prepend: site.baseurl }}) and [samples]({{ '/samples' | prepend: site.baseurl }}) (for now), be in markdown (and LaTeX?) only if possible for maximum portability in case we later switch platform.  [Liquid](https://github.com/Shopify/liquid/wiki) is the template engine in Jekyll and we'll also use [Bootstrap](http://getbootstrap.com/).  

## Getting Started

These instructions cover running this project on the Mac OSX client and on Windows. Running on Mac OS X is a bit more straight forward. This process requires use of the command-line.  
The windows setup instruction works to emulate the same process we use to develop our Google App website.
If you are not proficient with command-line git, GitHub has a [client for OS X](https://mac.github.com/).

#### Testing and authoring gh pages locally on your Mac

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
