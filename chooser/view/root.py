import tkinter as tk

class Root:

    __root = tk.Tk()

    __variables: dict = {}


    @staticmethod
    def get_root() -> tk.Tk:
        return Root.__root


    def __init__(self, title:str = 'date and time chooser') -> None:
        self.__title = title

    def activate(self) -> None:
        Root.get_root().title(self.__title)
        Root.get_root().mainloop()


    @staticmethod
    def destroy_application() -> None:
        Root.get_root().destroy()


    @staticmethod
    def clear_variables() -> None:
        Root.__variables.clear()


    @staticmethod
    def set_variable(name: str = 'noname',
                            variable: tk.Variable = None) -> None:
        Root.__variables[name] = variable


    @staticmethod
    def get_variable(name: str = 'noname') -> tk.Variable:
        return Root.__variables[name]


    # NEED TO CREATE AND TEST UPDATE METHOD FOR DICTONARY