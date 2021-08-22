import pytest
import tkinter as tk

from chooser.view.root import Root

Root()

def test_get_root_method() -> None:
    assert(isinstance(Root.get_root(), tk.Tk))
    
def test_default_string_variable() -> None:
    Root.set_string_variable()
    assert(Root.get_variable().get() == 'default' )

def test_arbitrary_string_variable() -> None:
    Root.set_string_variable('ebumba', 'sosimbos')
    assert(Root.get_variable('ebumba').get() == 'sosimbos')
    
Root.clear_variables()
Root.get_root().destroy()
