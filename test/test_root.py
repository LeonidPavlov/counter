import pytest
import tkinter as tk

from chooser.root import Root

Root()


def test_get_root_method() -> None:
    assert (isinstance(Root.get_root(), tk.Tk))


def test_default_string_variable() -> None:
    Root.set_variable(variable=tk.StringVar(Root.get_root(), 'default'))
    assert (Root.get_variable().get() == 'default')


def test_arbitrary_string_variable() -> None:
    Root.set_variable('ebumba', tk.StringVar(Root.get_root(), 'sosimbos'))
    assert (Root.get_variable('ebumba').get() == 'sosimbos')


def test_update_variable() -> None:
    new_variable: tk.StringVar = tk.StringVar(Root.get_root(), 'sosimbosimba')
    Root.update_variable('ebumba', new_variable)
    assert (Root.get_variable('ebumba').get() == 'sosimbosimba')


Root.clear_variables()
Root.get_root().destroy()
