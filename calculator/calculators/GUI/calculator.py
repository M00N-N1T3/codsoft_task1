# from lib import tkinter as tk
import tkinter as tk

DEFAULT_FONT = ("Arial",16)

class Calculator:


    def __init__(self):


        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("150x290")
        self.root.minsize(width=250,height=290)
        self.root.maxsize(width=450,height=450)


        # self.screen.pack(padx=6,pady=6,expand=False,side=tk.TOP)

        self.aux_frame = tk.Frame(self.root)
        
        self.screen = tk.Text(self.aux_frame,height=1,font=("Arial",16))
        self.screen.pack(padx=6,pady=6,expand=False,fill="both")
        
        self.button_frame = tk.Frame(self.aux_frame)


        self.memory_clear = button_layout(self.button_frame,0,0,"MC")
        self.memory_plus = button_layout(self.button_frame,1,0,"M+")
        self.memory_minus = button_layout(self.button_frame,2,0,"M-")
        self.memory_recall = button_layout(self.button_frame,3,0,"MR")


        self.clear= button_layout(self.button_frame,0,1,"C")
        self.divide = button_layout(self.button_frame,1,1,"/")
        self.multiply= button_layout(self.button_frame,2,1,"X")
        self.delete= button_layout(self.button_frame,3,1,"<=")

        self.seven= button_layout(self.button_frame,0,2,"7")
        self.eight = button_layout(self.button_frame,1,2,"8")
        self.nine= button_layout(self.button_frame,2,2,"9")
        self.minus= button_layout(self.button_frame,3,2,"-")


        self.four= button_layout(self.button_frame,0,3,"4")
        self.five= button_layout(self.button_frame,1,3,"5")
        self.six= button_layout(self.button_frame,2,3,"6")
        self.plus= button_layout(self.button_frame,3,3,"+")

        self.one= button_layout(self.button_frame,0,4,"1")
        self.two= button_layout(self.button_frame,1,4,"2")
        self.three= button_layout(self.button_frame,2,4,"3")

        self.percent= button_layout(self.button_frame,0,5,"%")
        self.zero= button_layout(self.button_frame,1,5,"0")
        self.comma= button_layout(self.button_frame,2,5,",")

        self.equal = tk.Button(self.button_frame,height=1,width=2,text="=")
        self.equal.grid(column=3,row=4,rowspan=2,sticky=tk.NS)


        self.button_frame.pack(expand=True,fill="both")

        self.aux_frame.pack(expand=True,fill="both")
        # self.aux_frame.pack(expand=True,fill="both",side=tk.TOP)




        self.root.mainloop()

class button_layout:

    def __init__(self,frame:tk.Frame ,column: int,row: int,text:str):
        btn = tk.Button(frame,height=1,width=2,text=text)
        btn.grid(column=column, row=row,padx=4,pady=4)
        # btn.grid_configure(sticky=tk.NSEW)
    pass


if __name__ == "__main__":
    calc = Calculator()
