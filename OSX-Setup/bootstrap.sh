#!/usr/bin/env bash
#
# (c) 2018, Bharath <bhrth.dsra1@gmail.com>
# This module is part of the automation setup project of new OSX machines
# done on the top of the following Gist:
#
# https://gist.github.com/codeinthehole/26b37efa67041e1307db
#
# Bootstrap script for setting up a new OSX machine
#
# This should be idempotent so it can be run multiple times.
#
# Some apps don't have a cask and so still need to be installed by hand. These
# include:
#
# - Twitter (app store)
# - Postgres.app (http://postgresapp.com/)
#
# Notes:
#
# - If installing full Xcode, it's better to install that first from the app
#   store before running the bootstrap script. Otherwise, Homebrew can't access
#   the Xcode libraries as the agreement hasn't been accepted yet.
#
# Reading:
#
# - http://lapwinglabs.com/blog/hacker-guide-to-setting-up-your-mac
# - https://gist.github.com/MatthewMueller/e22d9840f9ea2fee4716
# - https://news.ycombinator.com/item?id=8402079
# - http://notes.jerzygangi.com/the-best-pgp-tutorial-for-mac-os-x-ever/

echo "Starting bootstrapping"

# Check for Homebrew, install if we don't have it
if test ! $(which brew); then
    echo "Installing homebrew..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# Update homebrew recipes
brew update

# Install GNU core utilities (those that come with OS X are outdated)
brew tap homebrew/dupes
brew install coreutils
brew install gnu-sed --with-default-names
brew install gnu-tar --with-default-names
brew install gnu-indent --with-default-names
brew install gnu-which --with-default-names
brew install gnu-grep --with-default-names

# Install GNU `find`, `locate`, `updatedb`, and `xargs`, g-prefixed
brew install findutils

PACKAGES=(
    # Code searching tool
    the_silver_searcher
    ## Autotools setup ##
    # Automate producing configure scripts for software packages
    autoconf
    # Automate producing Makefiles
    automake
    # lightweight Linux distribution made specifically to run Docker containers
    docker
    # Multimedia tool for transcoding, multimedia libraries providing and format support (...)
    ffmpeg
    # Tool to write multilingual programs.
    gettext
    # Tool for Creating, editing, and getting information about GIF images.
    gifsicle
    # Version Control System
    git
    # Tool for feature branches creation
    git-flow
    # Tool for gitlog visualisation
    tig
    # Graph Visualization Software tools
    graphviz
    # Command-line wrapper for git that makes you better at GitHub.
    hub
    # Display, convert, and edit raster image and vector image files
    imagemagick
    # Command-line JSON processor.
    jq
    # Postgresql Database
    postgresql
    # Python
    python
    # Python3
    python3
    # pypy
    pypy
    # rename multiple files via command line
    rename
    # installs an SSH key on a server as an authorized key
    ssh-copy-id
    # Send terminal notifications to user
    terminal-notifier
    # Tree package for MacOSX
    tree
    # Vim Editor
    vim
    # Retrieving files over HTTP(S)/FTP(S)
    wget
    # For Data Transfer
    curl
    # Http load testing and benchmarking utility
    siege
    # Oh-my-Zsh
    zsh
    # a cd line tool to jump into buffered paths
    autojump
)

echo "Installing packages..."
brew install ${PACKAGES[@]}

echo "Cleaning up..."
brew cleanup


CASKS=(
    dropbox
    flux
    google-chrome
    google-drive
    gpgtools
    iterm2
    macvim
    skype
    slack
    vagrant
    virtualbox
    vlc
)