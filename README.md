# developer-rhino3d-com

This repo contains the content that gets generated to create http://mcneel.github.io/developer-rhino3d-com.  The system uses Jekyll,
in combination with GitHub pages, to generate and publish the site.

## Getting Started

Detailed instructions about pre-reqs, etc go here.

#### Testing and authoring gh pages locally with Jekyll

##### clone the ```https://github.com/mcneel/developer-rhino3d-com.git``` repo:  
 - notice that 'gh-pages' is the only branch.  Everithing commited to this branch is automatically published.
 - find the docs [here](http://mcneel.github.io/developer-rhino3d-com).  

##### Requirements: (instead of following the links below I installed with [homebrew](http://brew.sh/))
 - [Ruby](http://www.ruby-lang.org/en/downloads/) probably already on your mac.  
 - [RubyGems](http://rubygems.org/pages/download)  
 - [NodeJS](https://nodejs.org/)  - click the large Install button to download the package.

##### Install Jekyll  
 ```bash
   sudo gem install jekyll
 ```

##### Using Jekyll: serving / building

Open Terminal and cd to the folder that contains the cloned developer-rhino3d-com.git repository.

  - launch webserver:  
    ```jekyll serve```

    Once Jekyll has served the page it will print out:
    ```http://127.0.0.1:4000/developer-rhino3d-com``` (for example).  Local changes to the repository should be reflected upon a page-refresh of the locally served page.

  - build w/o plugins.  gh pages doesn't allow plugins:  
    ```jekyll build --safe```
