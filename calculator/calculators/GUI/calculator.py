# from lib import tkinter as tk
import tkinter as tk

DEFAULT_FONT = ("Arial",16)
BLACK = "#1d1d1d"
ORANGE = "#d34615"
RED = "#991121"
LIGHT_GREY = "#313131"
WHITE = "#FFFFFF"


class Calculator:

    # button color
    btn_BGColor = ORANGE
    btnABGColor = LIGHT_GREY

    # screen color
    screen_BGColor = BLACK
    frame_BGColor = BLACK

    # Menu
    frame_BGColor = BLACK
    frame_FGColor = WHITE
    frame_ABGColor = ORANGE


    def __init__(self):

        self.root = tk.Tk()


        self.aux_frame = tk.Frame(self.root)
        self.aux_frame.config(background=self.screen_BGColor)
        self.screen_frame = tk.Frame(self.aux_frame)
        self.screen_frame.config(background=self.screen_BGColor)


        self.screen = Screen(self.root)
        self.screen = tk.Entry(self.screen_frame,font=("Arial",32),width=11)
        self.screen.focus_set()
        self.screen.bind("<KeyPress>",self.handle_input)
        self.memory = calculator_memory(self.screen)
        

        # self.menubar = tk.Menu(self.root,background=BLACK,foreground=WHITE,activebackground=ORANGE,border=0)
        # self.Theme = tk.Menu(self.menubar,tearoff=0,font=("Arial",8),background=BLACK,foreground=WHITE,activebackground=ORANGE)


        self.menubar = tk.Menu(self.root)
        self.menubar.config(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,border=0)
        self.Theme = tk.Menu(self.menubar,tearoff=0,font=("Arial",8),background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor)

        self.History = tk.Button(self.menubar,font=("Arial",8),background=self.frame_BGColor)

        # Adding dark mode to the calculator
        self.Theme.add_command(label="Dark mode",font=("Arial",8),command=lambda: self.change_theme("Dark"))
        # self.Theme.add_separator() # separates the columns
        self.Theme.add_command(label="Light mode",font=("Arial",8),command=lambda: self.change_theme("Light"))

        # lastly we need to add our submenus to our menu Ribbon
        self.menubar.add_cascade(menu=self.Theme,label="Theme",font=("Arial",8))
        self.menubar.add_cascade(menu=self.History,label="History",font=("Arial",8))
        # then we need to add our menubar to our root window by using the root.config
        self.root.config(menu=self.menubar)

        self.screen.grid(row=0,padx=3,pady=3,columnspan=5)
        self.screen_frame.pack(expand=True,fill="both")

        self.button_frame = tk.Frame(self.aux_frame,background=self.frame_BGColor)

        self.memory_clear = button_layout(self.button_frame,0,0,"MC",command = self.memory.memory_clear)
        self.memory_plus = button_layout(self.button_frame,1,0,"M+",command = self.memory.memory_plus)
        self.memory_minus = button_layout(self.button_frame,2,0,"M-", command=self.memory.memory_minus)
        self.memory_recall = button_layout(self.button_frame,3,0,"MR",command=self.memory.memory_recall)

        self.clear= button_layout(self.button_frame,0,1,"C",command=self.clear_screen)
        self.divide = button_layout(self.button_frame,1,1,"/",command=lambda: self.clicked("/"))
        self.multiply= button_layout(self.button_frame,2,1,"X",command=lambda: self.clicked("x"))
        self.delete= button_layout(self.button_frame,3,1,"\u2190",command=self.backspace)

        self.seven= button_layout(self.button_frame,0,2,"7",command=lambda: self.clicked("7"))
        self.eight = button_layout(self.button_frame,1,2,"8",command=lambda: self.clicked("8"))
        self.nine= button_layout(self.button_frame,2,2,"9",command=lambda: self.clicked("9"))
        self.minus= button_layout(self.button_frame,3,2,"-",command=lambda: self.clicked("-"))


        self.four= button_layout(self.button_frame,0,3,"4",command=lambda: self.clicked("4"))
        self.five= button_layout(self.button_frame,1,3,"5",command=lambda: self.clicked("5"))
        self.six= button_layout(self.button_frame,2,3,"6",command=lambda: self.clicked("6"))
        self.plus= button_layout(self.button_frame,3,3,"+",command=lambda: self.clicked("+"))

        self.one= button_layout(self.button_frame,0,4,"1",command=lambda: self.clicked("1"))
        self.two= button_layout(self.button_frame,1,4,"2",command=lambda: self.clicked("2"))
        self.three= button_layout(self.button_frame,2,4,"3",command=lambda: self.clicked("3"))

        self.percent= button_layout(self.button_frame,0,5,"%",command=self.get_percent)
        self.zero= button_layout(self.button_frame,1,5,"0",command=lambda: self.clicked("0"))
        self.comma= button_layout(self.button_frame,2,5,".",command=lambda: self.clicked("."))


        self.equal = button_layout(self.button_frame,3,4,"=",command=self.equals)
        self.equal.configure_equal()

        self.button_frame.pack(expand=False,fill="both")
        self.aux_frame.pack(expand=False,fill="both",padx=10)

        self.root.mainloop()

    def change_theme(self, theme: str):

        # button color
        self.btn_BGColor = ORANGE if theme == "Dark" else WHITE
        # self.btn_BGColor = ORANGE if theme == "Dark" else LIGHT_GREY
        self.btnABGColor = WHITE

        # screen color
        self.screen_BGColor = BLACK if theme == "Dark" else "GREY"


        # frame color
        self.frame_BGColor = BLACK if theme == "Dark" else "GREY"
        self.frame_FGColor = WHITE if theme == "Dark" else BLACK
        self.frame_ABGColor = ORANGE if theme == "Dark" else "GREY"
        self.frame_AFGColor = WHITE if theme != "DarK" else None


        buttons = [self.memory_plus, self.memory_clear, self.memory_minus, self.memory_recall,
                   self.clear, self.divide, self.multiply, self.delete, self.seven, self.eight,
                   self.nine ,self.minus, self.four, self.five ,self.six ,self.plus,
                   self.one, self.two, self.three, self.percent, self.zero, self.comma, self.equal]
        for button in buttons:
            button.change_theme(BGColor=self.btn_BGColor,ABGColor=self.btnABGColor)

        self.menubar.configure(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,activeforeground=self.frame_AFGColor)
        self.Theme.configure(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,activeforeground=self.frame_AFGColor)
        self.button_frame.configure(background=self.frame_BGColor)
        self.screen_frame.configure(background=self.screen_BGColor)
        self.root.configure(background=self.frame_BGColor)
        self.aux_frame.config(background=self.frame_BGColor)

    def get_percent(self):
        values = self.screen.get()
        result  = eval(values)

        # result = str(result / 100)
        result = "{:.9f}".format(result/100)
        print(result)

        if len(values)!=0:
            self.screen.delete(0,"end")
            self.screen.insert(0,result)


    def clear_screen(self):
        try:
            self.screen.configure(state=["normal"])
            self.screen.delete("0",tk.END)
        except tk.TclError as e:
            e.add_note("Nothing on the screen")
            print(e)

    def handle_input(self,event):

        # accepted keyboard entries
        keypad = ["KP_1","KP_2","KP_3","KP_4","KP_5","KP_6","KP_7","KP_8","KP_9","KP_0",'KP_Decimal']
        special = ["period","BackSpace","KP_Add","KP_Subtract","minus","plus","\u2190","Right","Left","Delete","x","slash"]

        numbers = ["+",'-',",","1","2","3","4","5","6","7","8","9","0","."]
        numbers.extend(keypad); numbers.extend(special)

        print(event)
        if event.keysym in ["Return","KP_Enter"]:
            self.equals()
            self.screen.configure(state=["normal"],disabledbackground="White",foreground="Black",background="White",disabledforeground="Black")

        elif not event.keysym in numbers:
            self.screen.configure(state=["disabled"], disabledbackground='white', disabledforeground='Black')

        else:
            self.screen.configure(state=["normal"],disabledbackground="White",foreground="Black",background="White",disabledforeground="Black")

    def clicked(self,text):
        char_on_screen = self.screen.get()
        self.screen.insert(len(char_on_screen),text)

    def backspace(self):
        text = self.screen.get()
        self.screen.delete(len(text)-1,"end")

    def equals(self):
        calculation = self.screen.get()
        # removing the x
        calculation = calculation.replace("x",'*') if "x" in calculation else calculation
        try:
            if len(calculation) > 0:
                result = eval(calculation)
            else:
                result=""
        except Exception: # zero division error, cam mot divide by zero
            result = "Error"

        if "." in str(result):
            result = "{:.9f}".format(result)

        self.screen.delete(0,"end")
        self.screen.insert(0,result)

class calculator_memory:

    def __init__(self,screen: tk.Text|tk.Entry):
        self.memory = []
        self.screen=screen

    def memory_recall(self):

        if len(self.screen.get()) != 0:
            self.screen.delete("0",tk.END)

        if len(self.memory) != 0:
            self.screen.insert(0,self.memory[0])

    def memory_plus(self):

        old = None

        if len(self.memory) == 1:
            old = self.memory[0]
            del self.memory[0]


        try:
            value = str(eval(self.screen.get()))
            self.memory.append(value)
        except Exception as e:
            if old == None:
                pass
            else:
                self.memory.append(old)

    def memory_clear(self):
        if len(self.memory) > 0:
            del self.memory[0]


    def memory_minus(self):
        value=self.screen.get()

        if len(self.memory) > 0 and value in self.memory:
            del self.memory[0]

class button_layout:
    """
    Creates a single button widget for you
    Args:
        frame (tk.Frame): the frame the button belongs to
    """

    def __init__(self,frame:tk.Frame ,column: int,row: int,text:str, command: tk.COMMAND = None):
        self.btn = tk.Button(frame,height=2,width=4,text=text,command=command,border=2)
        self.btn.configure(background=ORANGE,activebackground=WHITE,font=("Arial",11))
        self.btn.grid(column=column, row=row,padx=4,pady=4)


    def change_theme(self,BGColor: str =ORANGE, ABGColor: str=WHITE):
        self.btn.configure(background=BGColor,activebackground=ABGColor,font=("Arial",11))

    def configure_equal(self,rowspan: int=2,height:int = 5,width: int=4,border:int=2):
        self.btn.configure(height=height,width=width,border=border)
        self.btn.grid(rowspan=rowspan)

class Screen:

    def __init__(self,root: tk.Tk):
        root.title("Calculator")
        root.configure(background=BLACK)
        root.geometry("300x450")
        root.minsize(width=300,height=450)
        root.maxsize(width=300,height=450)




if __name__ == "__main__":
    calc = Calculator()


