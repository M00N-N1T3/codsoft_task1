# from lib import tkinter as tk
import tkinter as tk

DEFAULT_FONT = ("Arial",16)

class Calculator:


    def __init__(self):


        self.root = tk.Tk()
        self.root.title("Calculator")

        self.root.minsize(width=250,height=250)
        self.root.maxsize(width=450,height=450)

        self.screen = tk.Text(self.root)
        self.screen.pack(padx=4,pady=4, expand=True,side=tk.TOP)

        self.aux_frame = tk.Frame(self.root)

        self.button_frame = tk.Frame(self.aux_frame)


        self.btn1= button_layout(self.button_frame,0,0,"test")
        self.button_frame.pack(expand=True, side=tk.LEFT)

        self.aux_frame.pack(expand=True, side=tk.TOP)





        self.root.mainloop()

class button_layout:

    def __init__(self,frame:tk.Frame ,column: int,row: int,text:str):
        btn = tk.Button(frame,height=1,width=2,text=text)
        btn.grid(column=column, row=row,padx=4,pady=4)
    pass


if __name__ == "__main__":
    calc = Calculator()
