#!/usr/bin/env bash
set -euo pipefail

# Creates a .venv in the project root and installs dependencies from requirements.txt
# Usage: ./create_venv.sh [--python /path/to/python]
# If --python is not provided this script uses the system 'python3' command.

PYTHON_CMD=python3
if [ "$#" -ge 2 ] && [ "$1" = "--python" ]; then
  PYTHON_CMD=$2
fi

VENV_DIR=".venv"
REQ_FILE="requirements.txt"

if [ ! -f "$REQ_FILE" ]; then
  echo "requirements.txt not found in $(pwd). Create one or run pip freeze in an existing venv first." >&2
  exit 1
fi

echo "Creating virtual environment in $VENV_DIR using $PYTHON_CMD..."
$PYTHON_CMD -m venv "$VENV_DIR"

# Ensure pip is up to date
echo "Upgrading pip in the venv..."
"$VENV_DIR/bin/python" -m pip install --upgrade pip setuptools wheel

echo "Installing packages from $REQ_FILE..."
"$VENV_DIR/bin/python" -m pip install -r "$REQ_FILE"

echo "Done. Activate with: source $VENV_DIR/bin/activate"
