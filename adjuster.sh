#!/bin/bash -x

python3 -m venv venv

venv/bin/pip install pytest


venv/bin/pip install pycairo

venv/bin/pip install PyGObject

venv/bin/pip install --upgrade pyinstaller

venv/bin/python -m pytest

rm -f dist/date_time_chooser

venv/bin/pyinstaller cli_gtk.py --onefile

mv dist/cli_gtk dist/date_time_chooser

./dist/date_time_chooser


