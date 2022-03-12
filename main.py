from tkinter import Tk
from tkinter import Label
from datetime import datetime


class Screen:
    def __init__(self, master):
        self.master = master
        self.master.title('Relógio')
        self.master.configure(bg='white')

        self.clock_label = Label(font=('Sans', 25), fg='red', bg='white')
        self.clock_label.pack(pady=30, padx=30)

        self.update_clock()

    def update_clock(self):
        time = datetime.now().strftime('%H:%M:%S')
        self.clock_label.configure(text=time)

        self.master.after(1000, self.update_clock)


root = Tk()
Screen(root)
root.mainloop()
