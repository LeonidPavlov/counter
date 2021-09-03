import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window(Gtk.Window):

    @staticmethod
    def run_application() -> None:
        win = Window()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()        

    def __init__(self) -> None:
        super().__init__(title = 'EBAT V ROT')
        self.button = Gtk.Button(label = 'click here')
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self,widget):
        widget.set_label('sosimba')    

