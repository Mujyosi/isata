#!/bin/bash

# Exit early on errors
set -euo pipefail

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Install Python 3 virtual env
VIRTUALENV=venv

if [ ! -d "$VIRTUALENV" ]; then
  python -m venv "$VIRTUALENV"
fi

if [ ! -f "$VIRTUALENV/bin/pip" ]; then
  curl -sS --retry 5 https://bootstrap.pypa.io/get-pip.py | "$VIRTUALENV/bin/python"
fi

# Update pip if necessary
"$VIRTUALENV/bin/pip" install --upgrade pip

# Install the requirements
"$VIRTUALENV/bin/pip" install -r requirements.txt

# Run a glorious Python 3 server
"$VIRTUALENV/bin/python" app.py
