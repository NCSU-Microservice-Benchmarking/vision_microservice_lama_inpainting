#!/usr/bin/env bash

# shellcheck source=/dev/null

set -ex

# Environment
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# App
flask run
