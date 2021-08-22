#!/bin/bash -x

python3 -m venv venv

venv/bin/pip install pytest

venv/bin/python -m pytest

venv/bin/pip install --upgrade pyinstaller

rm -f dist/date_time_chooser

venv/bin/pyinstaller cli.py --onefile

mv dist/cli dist/date_time_chooser

./dist/date_time_chooser


