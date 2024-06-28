from lib import tkinter as tk
# import tkinter as tk
# from tkinter import messagebox
from lib.tkinter import messagebox

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
        self.memory = Calculator_memory(self.screen)
        self.history = Calculator_history()

        self.menubar = tk.Menu(self.root)
        self.menubar.config(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,border=0)
        self.Theme = tk.Menu(self.menubar,tearoff=0,font=("Arial",8),background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor)
        self.History = tk.Menu(self.menubar,tearoff=0,font=("Arial",8),background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor)


        # adding history
        self.History.add_command(label="Show history",font=("Arial",8),command=self.display_history)
        self.History.add_command(label="Clear history",font=("Arial",8),command=self.history.clear)

        # Adding dark mode to the calculator
        self.Theme.add_command(label="Dark mode",font=("Arial",8),command=lambda: self.change_theme("Dark"))
        self.Theme.add_command(label="Light mode",font=("Arial",8),command=lambda: self.change_theme("Light"))

        # lastly we need to add our submenus to our menu Ribbon
        self.menubar.add_cascade(menu=self.Theme,label="Theme",font=("Arial",8))
        self.menubar.add_cascade(menu=self.History,label="History",font=("Arial",8))
        # then we need to add our menubar to our root window by using the root.config
        self.root.config(menu=self.menubar)

        self.screen.grid(row=0,padx=3,pady=3,columnspan=5)
        self.screen_frame.pack(expand=True,fill="both")

        self.button_frame = tk.Frame(self.aux_frame,background=self.frame_BGColor)

        self.memory_clear = Button_layout(self.button_frame,0,0,"MC",command = self.memory.memory_clear)
        self.memory_plus = Button_layout(self.button_frame,1,0,"M+",command = self.memory.memory_plus)
        self.memory_minus = Button_layout(self.button_frame,2,0,"M-", command=self.memory.memory_minus)
        self.memory_recall = Button_layout(self.button_frame,3,0,"MR",command=self.memory.memory_recall)

        self.clear= Button_layout(self.button_frame,0,1,"C",command=self.clear_screen)
        self.divide = Button_layout(self.button_frame,1,1,"/",command=lambda: self.clicked("/"))
        self.multiply= Button_layout(self.button_frame,2,1,"X",command=lambda: self.clicked("x"))
        self.delete= Button_layout(self.button_frame,3,1,"\u2190",command=self.backspace)

        self.seven= Button_layout(self.button_frame,0,2,"7",command=lambda: self.clicked("7"))
        self.eight = Button_layout(self.button_frame,1,2,"8",command=lambda: self.clicked("8"))
        self.nine= Button_layout(self.button_frame,2,2,"9",command=lambda: self.clicked("9"))
        self.minus= Button_layout(self.button_frame,3,2,"-",command=lambda: self.clicked("-"))


        self.four= Button_layout(self.button_frame,0,3,"4",command=lambda: self.clicked("4"))
        self.five= Button_layout(self.button_frame,1,3,"5",command=lambda: self.clicked("5"))
        self.six= Button_layout(self.button_frame,2,3,"6",command=lambda: self.clicked("6"))
        self.plus= Button_layout(self.button_frame,3,3,"+",command=lambda: self.clicked("+"))

        self.one= Button_layout(self.button_frame,0,4,"1",command=lambda: self.clicked("1"))
        self.two= Button_layout(self.button_frame,1,4,"2",command=lambda: self.clicked("2"))
        self.three= Button_layout(self.button_frame,2,4,"3",command=lambda: self.clicked("3"))

        self.percent= Button_layout(self.button_frame,0,5,"%",command=self.get_percent)
        self.zero= Button_layout(self.button_frame,1,5,"0",command=lambda: self.clicked("0"))
        self.comma= Button_layout(self.button_frame,2,5,".",command=lambda: self.clicked("."))


        self.equal = Button_layout(self.button_frame,3,4,"=",command=self.equals)
        self.equal.configure_equal()

        self.button_frame.pack(expand=False,fill="both")
        self.aux_frame.pack(expand=False,fill="both",padx=10)

        self.root.mainloop()

    def change_theme(self, theme: str):
        """
        Changes the theme of the calculator from dark to light mode
        Args:
            theme (str): trigger for color change
        """

        # button color
        self.btn_BGColor = ORANGE if theme == "Dark" else WHITE
        # self.btn_BGColor = ORANGE if theme == "Dark" else LIGHT_GREY
        self.btnABGColor = WHITE

        # frame color
        self.frame_BGColor = BLACK if theme == "Dark" else "GREY"
        self.frame_FGColor = WHITE if theme == "Dark" else BLACK
        self.frame_ABGColor = ORANGE if theme == "Dark" else "GREY"
        self.frame_AFGColor = WHITE if theme != "DarK" else None


        # all the available buttons
        buttons = [self.memory_plus, self.memory_clear, self.memory_minus, self.memory_recall,
                   self.clear, self.divide, self.multiply, self.delete, self.seven, self.eight,
                   self.nine ,self.minus, self.four, self.five ,self.six ,self.plus,
                   self.one, self.two, self.three, self.percent, self.zero, self.comma, self.equal]
        for button in buttons:
            button.change_theme(BGColor=self.btn_BGColor,ABGColor=self.btnABGColor)

        # changing the colors of all the frames
        frames = [self.root,self.aux_frame,self.button_frame,self.screen_frame]
        for frame in frames:
            frame.configure(background=self.frame_BGColor)

        self.menubar.configure(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,activeforeground=self.frame_AFGColor)
        self.Theme.configure(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,activeforeground=self.frame_AFGColor)
        self.History.configure(background=self.frame_BGColor,foreground=self.frame_FGColor,activebackground=self.frame_ABGColor,activeforeground=self.frame_AFGColor)

    def display_history(self):
        """
        Pops up a new windows revealing the history
        """
        messagebox.showinfo(title="History",message=self.history.show())


    def get_percent(self):
        """
        Returns the percentage of the value by dividing it by 100
        """
        values = self.screen.get()
        if len(values) == 0:
            return

        result  = eval(values)

        result_string = str(result / 100)
        if (len(result_string) >= 4 and "." in result_string):
            result = "{:.5f}".format(result/100)

            zero = 0
            for char in result[4::]:
                if char == "0":
                    zero+=1

            if zero == 3:
                result = result[0:4]

        else:
            result = (result/100)

        if len(values)!=0:
            self.screen.delete(0,"end")
            self.screen.insert(0,result)


    def clear_screen(self):
        """
        Clears the screen. Deletes all the existing content
        """
        try:
            self.screen.configure(state=["normal"])
            self.screen.delete("0",tk.END)
        except tk.TclError as e:
            e.add_note("Nothing on the screen")
            print(e)

    def handle_input(self,event):
        """
        Handles the keypress events when a user opts to type the individual values.
        Ensures that not all keys are recorded unless specified

        Args:
            event (<KeyPress>): The key being pressed
        """

        # accepted keyboard entries
        keypad = ["KP_1","KP_2","KP_3","KP_4","KP_5","KP_6","KP_7","KP_8","KP_9","KP_0",'KP_Decimal']
        special = ["period","BackSpace","KP_Add","KP_Subtract","minus","plus","\u2190","Right","Left","Delete","x","slash"]

        numbers = ["+",'-',",","1","2","3","4","5","6","7","8","9","0","."]
        numbers.extend(keypad); numbers.extend(special)

        if event.keysym in ["Return","KP_Enter"]:
            self.equals()
            self.screen.configure(state=["normal"],disabledbackground="White",foreground="Black",background="White",disabledforeground="Black")

        elif not event.keysym in numbers:
            self.screen.configure(state=["disabled"], disabledbackground='white', disabledforeground='Black')

        else:
            self.screen.configure(state=["normal"],disabledbackground="White",foreground="Black",background="White",disabledforeground="Black")

    def clicked(self,text: str):
        """
        prints the clicked button's char onto the calculator screen

        Args:
            text (str): the character belonging to the clicked key
        """
        char_on_screen = self.screen.get()
        self.screen.insert(len(char_on_screen),text)

    def backspace(self):
        """
        Deletes a single char from the screen.
        This method is called when you press the backspace key on the calculator
        """
        text = self.screen.get()

        if len(text) == 0:
            pass
        elif text != "Error":
            self.screen.delete(len(text)-1,"end")
        else:
            self.clear_screen()

    def equals(self):
        """
        Evaluates an expression and equates it.
        Method is called upon when user presses Enter or onscreen equal.
        """
        calculation = self.screen.get()
        calculation = calculation.replace("x",'*') if "x" in calculation else calculation
        try:
            if len(calculation) > 0:
                result = eval(calculation)
            else:
                result=""
        except Exception: # zero division error, cam mot divide by zero
            result = "Error"

        # recording the operation and storing to history
        self.history.record(f"{calculation} = {result}")

        self.screen.delete(0,"end")
        self.screen.insert(0,result)

class Calculator_memory:
    """
    The main class for handling the calculator memory
    """
    def __init__(self,screen: tk.Text|tk.Entry):
        """
        The instantiation of the memory. We are assigning a new memory field
        to the given calculator

        Args:
            screen (tk.Text | tk.Entry): the Text/Entry object that we wish to
            collect data from  and display data on
        """
        self.memory = []
        self.screen=screen

    def memory_recall(self):
        """
        Prints the data stored in memory on the screen
        """

        if len(self.screen.get()) != 0:
            self.screen.delete("0",tk.END)

        if len(self.memory) != 0:
            self.screen.insert(0,self.memory[0])

    def memory_plus(self):
        """
        adds/Overwrites the memory with new data
        """

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
        """
        Removes any existing data in the memory
        """
        if len(self.memory) > 0:
            del self.memory[0]


    def memory_minus(self):
        """
        Removes the current value on screen from the memory if the value exists in the memory
        """
        value=self.screen.get()

        if len(self.memory) > 0 and value in self.memory:
            del self.memory[0]

class Button_layout:
    """
    Creates a single button widget for you
    Args:
        frame (tk.Frame): the frame the button belongs to
    """

    def __init__(self,frame:tk.Frame ,column: int,row: int,text:str, command: tk.COMMAND = None):
        """
        The instantiating of a single tkinter button object. 
        This includes the placing of the button using the grid layout

        Args:
            frame (tk.Frame): the frame to place the button on
            column (int): the column the button will be grided in
            row (int): the row the button will be grided in
            text (str): the title/label on the button
            command (tk.COMMAND, optional):the command that gets executed on press. Defaults to None.
        """
        self.btn = tk.Button(frame,height=2,width=4,text=text,command=command,border=2)
        self.btn.configure(background=ORANGE,activebackground=WHITE,font=("Arial",11))
        self.btn.grid(column=column, row=row,padx=4,pady=4)


    def change_theme(self,BGColor: str =ORANGE, ABGColor: str=WHITE):
        """
        Changes the color of a button

        Args:
            BGColor (str, optional):background color of a button. Defaults to ORANGE.
            ABGColor (str, optional): active background of a color. Defaults to WHITE.
        """
        self.btn.configure(background=BGColor,activebackground=ABGColor,font=("Arial",11))

    def configure_equal(self,rowspan: int=2,height:int = 5,width: int=4,border:int=2):
        """
        Configures the equal button to fit the frame. This method is precisely designed just for the
        the equal button

        Args:
            rowspan (int, optional): how many rows teh button should span. Defaults to 2.
            height (int, optional): the height of the button if necessary. Defaults to 5.
            width (int, optional): the width of the button if necessary. Defaults to 4.
            border (int, optional): the size of the border. Defaults to 2.
        """
        self.btn.configure(height=height,width=width,border=border)
        self.btn.grid(rowspan=rowspan)

class Screen:

    def __init__(self,root: tk.Tk):
        """
        Used to generate a new screen object

        Args:
            root (tk.Tk):the root frame of your application
        """
        root.title("Calculator")
        root.configure(background=BLACK)
        root.geometry("300x450")
        root.minsize(width=300,height=450)
        root.maxsize(width=300,height=450)

class Calculator_history():

    def __init__(self):
        self.history = []

    def record(self,text:str):
        """
        adds to teh current history

        Args:
            text (str): text to add
        """
        self.history.append(text)

    def show(self):
        """
        creates a string message text out of teh record history

        Returns:
            str: the history
        """
        text = ""

        if len(self.history) == 0:
            text = "History is empty"
        else:
            for record in self.history:
                text += f"[{self.history.index(record) + 1}]: {record}\n"

        return text

    def clear(self):
        """
        clears the history
        """
        self.history = []



def main():
    Calculator()

if __name__ == "__main__":
    main()


