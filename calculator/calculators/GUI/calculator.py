from lib import tkinter as tk
from tkinter import messagebox


class Calculator:

    def __init__(self):
        self.root = tk.Tk()

        # root window
        self.root.title("Calculator")

        # we will add custom colors for our calculator
        # and try add a dialer theme, but lets keep it simple for now

        self.menubar = tk.Menu(self.root)

        # them we will come back to you
        self.theme= tk.Menu(self.menubar,tearoff=0)

        # adding a cascade to the menu is how we add a menu into a menu
        self.menubar.add_cascade(menu=self.theme,label="Theme",font=("Arial",8))

        # if you do not config a menu it won't show. Config is the equivalent of pack
        self.root.config(menu=self.menubar)

        self.entry_box = tk.Entry(self.root)
        self.entry_box.pack(pady=5,padx=5,expand=True,fill=tk.X)

        # the buttons will be in a grid layout
        self.button_frame = tk.Frame(self.root)
        self.button_frame.columnconfigure(0,weight=5)
        self.button_frame.columnconfigure(1,weight=1)
        self.button_frame.columnconfigure(2,weight=1)
        self.button_frame.columnconfigure(3,weight=1)


        # button layouts # row 3
        self.button7= tk.Button(self.button_frame,text="7")
        self.button7.grid(row=3,column=0,padx=2,pady=2)
        
        self.button8= tk.Button(self.button_frame,text="8")
        self.button8.grid(row=3,column=1,padx=2,pady=2)
        
        self.button9= tk.Button(self.button_frame,text="9")
        self.button9.grid(row=3,column=2,padx=2,pady=2)


        # row 4
        
        self.button4= tk.Button(self.button_frame,text="4")
        self.button4.grid(row=4,column=0,padx=2,pady=2)
        
        self.button5= tk.Button(self.button_frame,text="5")
        self.button5.grid(row=4,column=1,padx=2,pady=2)
        
        self.button6= tk.Button(self.button_frame,text="6")
        self.button6.grid(row=4,column=2,padx=2,pady=2)
        

        # row 5
        self.button1= tk.Button(self.button_frame,text="1")
        self.button1.grid(row=5,column=0,padx=2,pady=2)

        self.button2= tk.Button(self.button_frame,text="2")
        self.button2.grid(row=5,column=1,padx=2,pady=2)

        self.button3= tk.Button(self.button_frame,text="3")
        self.button3.grid(row=5,column=2,padx=2,pady=2)


        # self.button0= tk.Button(self.button_frame,text="0")
        # self.button0.grid(row=0,column=0,padx=2,pady=2)

        self.button_frame.pack(padx=5,pady=5,)

        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()