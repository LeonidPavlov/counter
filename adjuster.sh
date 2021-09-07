#!/bin/bash -x

python3 -m venv venv

venv/bin/python install pip

venv/bin/pip install --upgrade fbs PyQt5 PyInstaller==3.4 pytest

venv/bin/python -m pytest

rm -f dist/cli

venv/bin/pyinstaller cli.py --onefile

./dist/cli


