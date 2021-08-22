import pytest
import tkinter as tk

from chooser.view.base import Base


def test_get_root_method() -> None:
    root = tk.Tk()
    Base(root)
    assert(isinstance(Base.get_root(), tk.Tk))
    root.destroy()

