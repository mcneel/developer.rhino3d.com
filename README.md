# developer.rhino3d.com

This repo contains the contents of https://developer.rhino3d.com.

Pull requests are welcome! :tada: Please read our guide on [Contributing](https://github.com/mcneel/developer.rhino3d.com/blob/main/CONTRIBUTING.md).

If you want to build the site yourself, to test your changes before opening a pull request, then please check out the [Getting Started](#getting-started) section below.

## Getting Started

These instructions cover running this project locally on both Windows and macOS so that you can preview changes:

1. Clone\* this repository:

    ```sh
    git clone https://github.com/mcneel/developer.rhino3d.com.git
    ```

2. Download, install, and launch [Visual Studio Code](https://code.visualstudio.com/) and open the root folder of the repository.

3. **(macOS only)** In *Visual Studio Code*, press `Command`+`Shift`+`P`, followed by `enter` to bring up the *Command Palette*, then type `Tasks` and select `Tasks: Run Task`, followed by `hugo SetMaxFilesLimits (run once only)` and press `enter`. *Restart your computer*. (This step only has to be run once if you have never used hugo before on this computer.)

4. In *Visual Studio Code*'s left-hand sidebar, navigate to the (file) *Explorer* section, open the *content/en/guides/general/how-this-site-works/index.md* file.

5. In *Visual Studio Code's* left-hand sidebar, navigate to *Run and Debug* > *Hugo: Serve* ...

    ![VSCode hugo serve](static/images/vscode-hugo-serve.png)

Press the green triangle to start the process. It will take a few seconds and then your web browser should open to the *How This Site Works* guide, ready for editing. Changes made to the *index.md* file in Visual Studio Code should appear in your browser immediately. Note that your web browser might show an error, in which case you'll need to refresh the page once VS Code has finished setting up the server on port 1313.

\* If you are not comfortable using git on the command-line, then check out the [git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf) or try [GitHub Desktop](https://desktop.github.com).

## What next?

Once you have cloned or forked this repository and are able to build it locally, please check out the following guides:

* [How This Site Works](https://developer.rhino3d.com/guides/general/how-this-site-works/)
* [Developer Docs Style Guide](https://developer.rhino3d.com/guides/general/developer-docs-style-guide/)
