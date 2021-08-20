#!/bin/bash -x

python3 -m venv venv

venv/bin/pip install pytest

venv/bin/python -m pytest

venv/bin/pip install --upgrade pyinstaller

venv/bin/pyinstaller cli.py --onefile

venv/bin/python cli.py

