#!/bin/bash -x

python3 -m venv venv

venv/bin/pip install pytest

venv/bin/pytest

venv/bin/pip install --upgrade pyinstaller

venv/bin/pyinstaller chooser.py --onefile

venv/bin/python chooser.py

