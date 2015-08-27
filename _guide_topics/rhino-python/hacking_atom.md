---
layout: bootstrap
title: Hacking and Testing latest Atom rhino-python package
author: alain@mcneel.com
categories: ['General']
platforms: ['Mac']
apis:
languages: ['Markdown', 'Kramdown', 'YAML']
keywords: ['hacking', 'atom', 'rhino-python']
TODO: 0
origin: unset
order: 1
---

# Running and Testing the Atom rhino-python package from source.
## Specifically, running from the "settings" branch of the source to test the search paths configuration.

I updated the rhino-python Atom package to support configuring the Python search path which I plan to deploy when we release MR5.1.  The document describes how to install and run it from source so some of you can test and give feedback.  

  - open a terminal window pointing to the directory where you want to clone the rhino-python package and type:
    ```
    git clone https://github.com/mcneel/rhino-python.git
    ```
    ```
    cd rhino-python
    ```
  - switch to the branch that implements the search paths configuration.
  ```
  git checkout settings
  ```
  - create a link so that the package will be loaded from the git repo when Atom is run in dev mode:
  ```
  apm link -d
  ```
  - install the package dependencies
  ```
  apm install
  ```
  - to launch Atom in dev mode cd to where your python files are and type:
  ```
  atom -d .
  ```
  - You are now running the rhino-python package from source.  You are specifically running from the "settings" git branch where the python search paths configuration is implemented.

  - Rename Rhinoceros.app to something else to back it up then rename RhinoWIP.app to Rhinoceros.app (this is a temporary step that won't be required in he future).

  - Launch the RhinoWIP (renamed) and type the command: `StartAtomEditorListener`.  Getting and setting the Python search path values is done by Rhino so it has to be running and listening for Atom requests.  

  - Switch back to Atom and press the <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>s</kbd> keys to open the "Rhino Python Search Paths" window.

# Notes on the Rhino Python Search Paths toolbar:
  - when the window is 1st opened only the add ( <kbd>+</kbd> ) button is enabled.
  - click on a path to select it and the other nav buttons become enabled.
  - the "open selected path in Atom" button is not implemented yet.
  - None of the changes made in the UI are saved until the <kbd>save</kbd> button is clicked which sends the save request to Rhino.
  - Clicking the <kbd>revert</kbd> button discards all changes made since the last save by sending a request to Rhino for the last saved search paths.

Please send all feedback to [Alain](mailto:alain@mcneel.com).
