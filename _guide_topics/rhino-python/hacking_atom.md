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

# Running and Testing the Atom rhino-python package from source

I updated the rhino-python Atom package to support configuring the Python search path which I plan to deploy when we release MR5.1.  The document describes how to install and run it from source so some of you can test and give feedback.  

  - open a terminal window pointing to the directory where you want to clone the rhino-python package and type:
    ```
    git clone https://github.com/mcneel/rhino-python.git
    ```
  - create a link so that the package will be loaded from the git repo when Atom is run in dev mode:
  ```
  cd rhino-python
  ```
  ```
  apm link -d
  ```
  - to launch Atom in dev mode cd to where your python files are and type:
  ```
  atom -d .
  ```
  - You are now running the rhino-python package from source.
  - To run the from the dev branch that implements the Python search path config switch to a terminal window that points to the rhino-python source directory and type:
  ```
  git checkout settings
  ```
  - Swith back to the Atom window that was opened from your Python files directory and reload it by pressing the <kbd>ctrl</kbd> + <kbd>alt</kbd> +
   <kbd>cmd</kbd> + <kbd>l</kbd> keys.
  - Launch the latest RhinoWIP and type the command: `StartAtomEditorListener`.  Getting and setting the Python search path values is done by Rhino so it has to be running and listening for Atom requests.
  - Switch back to Atom and press the <kbd>ctrl</kbd> + <kbd>alt</kbd> + <kbd>s</kbd> keys to open the "Rhino Python Search Paths" window.

# notes on the Rhino Python Search Paths toolbar:
  - when the window is 1st opened only the add ( <kbd>+</kbd> ) button is enabled.
  - click on a path to select it and the other nav buttons become enabled.
  - the "open selected path in Atom" button is not implemented yet.
  - None of the changes made in the UI are saved until the <kbd>save</kbd> button is clicked which sends the save request to Rhino.
  - Clicking the <kbd>revert</kbd> button discards all changes made since the last save by sending a request to Rhino for the last saved search paths.

Please send all feedback to [Alain](mailto:alain@mcneel.com).
