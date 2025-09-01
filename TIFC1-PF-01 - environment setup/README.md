# Introduction

This module has been designed to provide you with not only an introduction to Python, but also use methods for sharing information and learning which you will encounter in the modern IT workplace. i.e. using online guides and examples to extrapolate solutions to your own problems.

Specifically, we're going to use the following industry standard platforms:
- Git - version control software, used for managing and tracking changes and contributors to code bases, and projects.
- GitHub - provides online repositories (*like file shares*), which allow you to create, store, change, merge, and collaborate on files or code. **Although commonly used together, Git and GitHub are separate tools, for example Git can be used with other repository providers or private repo's**.
- Visual Studio Code (VSCode/VSC) - Out of the box it's just a text editor, with a few cool features such as an integrated terminal, developed by Microsoft. But through a huge range of extensions and plugins, it's functionality can be massively expanded. It is available on Windows, Mac, Linux, through a browser, and more. It supports pretty much every language you can think of through plugins, as well as integrates with many industry standard tools and technologies. 

    Its' flexibility has resulted in VSC becoming the most popular coding environment in the industry. Other options exist, some are specialised for a single language, such as pyCharm, and if you have a strong preference for an alternative then it's not a huge problem. But you may find yourself swapping between a few different windows to match VSC's functionality.

## Installation

You have a couple of options for following this module, you can view and navigate the documentation via GitHub [from here](https://github.com/Generation-UK-I/AWS-IRE4-python). 

If you do it this way you will only view the nicely formatted resources, and examples. You will only need to install Visul Studio Code from below, however, you will need to create and manage your own files.

Alternatively, you can install Git, and download the entire module to your own computer and have a local copy with the correct structure, which you can edit yourself.

This way is more flexible, offers you more control, but is a bit more more technically challenging. It can also be a bit more confusing as you'll see the raw **markdown** files in VSC, and will need to open them in a preview pane, and manage your windows.

### Python

If you do not have Python installed download it [from here](https://www.python.org/downloads/).

    If you get weird behaviour where it pushes you to the Windows Store to install behaviour click start and search for `Manage App Execution Aliases`. Look for Python, and toggle it off.

### Git
---
#### Quick and easy, basic functionality:

Type the following into your command prompt or PowerShell
`winget install --id Git.Git -e --source winget`

---
#### Guided Installer, provides more options:

[Download here](https://git-scm.com/downloads)

*Also provides Git Bash, a handy Bash terminal for Windows*

---
### VSCode

[Download here](https://code.visualstudio.com/)

*Do **NOT** download **Visual Studio**, which is a development environment for making .NET and C++ applications - ensure you get **Visual Studio Code**.*

---
### GitHub
We are going to use GitHub, but we only need public repositories for the purpose of this module. However, it is recommended that you create your own GitHub account (using your personal email), because we will use it to create and host your portfolio of skills and evidence.

---
If you are not downloading the repository it is strongly recommended that you create a new directory for your Python work, and sub-directories for the different topics, as it's likely you'll need to find and return to earlier examples of code as we work our way through.

---
If you want a local copy of the resources, after installing Git, enter the following command to clone the entire repository:

`git clone https://github.com/Generation-UK-I/AWS-IRE4-python.git`

## Setting up Visual Studio Code

There are a couple of extensions we need to install to configure our VSC installation:

1. Python plugin - *look for the one from Microsoft*
1. Live Preview - *look for the one from Microsoft*