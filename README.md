programm is a part of another and have limited functionality
it create date time instanse from date picker


tested in ubuntu 20.04

minimun required python 3.3 (documentation for venv)

inside directory date_time_chooser run script ./adjuster.sh

it's do next:

install python3 venv

install pytest, pycairo for gtk+, PyGObject for gkt+, pyinstaller

pytest in virtual environment

run tests

create runnable file chooser in directory dist

run chooser runnable file

for other operating systems need to use modifications 
of same commands as in file  adjuster.sh


P.S. I tried run tkinter ttk for simplicity, but crashed with that problem:
I attempted to bind label or button to event within cycle, because elements was about 100.
For this problem  tkinter not  intended, only in list
So i migrate to use Gtk+ or if python don't work this way exist C with some complicity, but with warranty work