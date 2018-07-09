#!/usr/bin/env bash
set -e

# Install homebrew if not already installed
if ! type brew >/dev/null 2>&1; then
  /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" \
  </dev/null
fi

# Install python3.6 if not already installed
if ! type python3 >/dev/null 2>&1; then
    brew install python3
fi

# pip3 is baked into python3 :)
if ! type virtualenv >/dev/null 2>&1; then
    pip3 install virtualenv
fi

# Create a virtual environment for the project
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install all dependencies
pip3 install -r requirements.txt

echo "Set up complete!"
