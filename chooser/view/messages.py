import tkinter as tk

class Achtung:
    def __init__(self, error: Exception = RuntimeError(), 
                    file: str = 'file unknoun', 
                    where: str = 'unknown place', **kwargs) -> None:
        top = tk.Toplevel()
        top.title('error')
        frame = tk.Frame(top, background='dark red', pady=10, padx=10)
        frame.pack()
        label = tk.Label(frame, text = f'in {__file__} file\n' +\
                                f'in {where}\n' +\
                                f'ERROR -> {repr(error)}',
                                foreground='yellow',
                                background='dark red', 
                                font = 'Noto 10 bold')  
        label.pack()
        close = tk.Button(frame, text='CLOSE', background='dark red',
                            foreground='yellow', command=top.destroy, )
        close.pack()


class Info:
    def __init__(self, info: str = 'default ingo') -> None:
        top = tk.Toplevel()
        top.title('info')
        frame = tk.Frame(top, background='dark green', pady=10, padx=10)
        frame.pack()
        label = tk.Label(frame, text = info, foreground='pink', wraplength=300,
                            background='dark green', font = 'Noto 10 bold')
        label.pack()
        close = tk.Button(frame, text='CLOSE', background='dark green',
                            foreground='pink', command=top.destroy)
        close.pack()

def shuher(event) -> None:
    Achtung(where='class constructor', error = ArithmeticError())

def message(event) -> None:
    Info('ebat colotit sisi banan nahuy a to za ebalo dksls slkdslk')



if __name__ == '__main__':
    master = tk.Tk()
    master.bind('<Button-1>', shuher)
    master.bind('<Button-3>', message)
    
    master.mainloop()
