import tkinter as tk

class Achtung:
    def __init__(self, error: Exception = RuntimeError(), 
                    file: str = 'file unknoun', 
                    where: str = 'unknown place', **kwargs) -> None:
        top = tk.Toplevel()
        top.title('error')
        frame = tk.Frame(top, background='dark red')
        frame.pack()
        label = tk.Label(frame, text = f'in {__file__} file\n' +\
                                f'in {where}\n' +\
                                f'ERROR -> {repr(error)}',
                                foreground='pink',
                                background='dark red', 
                                font = 'Noto 10 bold')  
        label.pack()
        close = tk.Button(frame, text='CLOSE', background='dark red',
                            foreground='yellow', command=top.destroy)
        close.pack()

# def shuher(event) -> None:
#     Achtung(where='class constructor', error = ArithmeticError())

# if __name__ == '__main__':
#     master = tk.Tk()
#     master.bind('<Button-1>', shuher)
#     master.mainloop()
