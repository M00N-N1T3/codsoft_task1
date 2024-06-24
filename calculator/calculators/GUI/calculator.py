from lib import tkinter as tk


class Calculator:

    def __init__(self):
        self.root = tk.Tk()

        # root window
        self.root.title("Calculator")

        # we will add custom colors for our calculator
        # and try add a dialer theme, but lets keep it simple for now

        self.menubar = tk.Menu(self.root)

        # them we will come back to you
        self.theme = tk.Menu(self.menubar, tearoff=0)

        # adding a cascade to the menu is how we add a menu into a menu
        self.menubar.add_cascade(menu=self.theme, label="Theme", font=("Arial", 8))

        # if you do not config a menu it won't show. Config is the equivalent of pack
        self.root.config(menu=self.menubar)

        # frames
        self.frame1 = tk.Frame(self.root)
        self.screen = tk.Text(self.frame1, height = 2,width=8, font=("Arial" , 16))
        self.screen.pack(padx=5,pady=2,side=tk.LEFT,expand=True,fill=tk.X)
        self.frame1.pack(side=tk.TOP,fill=tk.X)

        self.root.mainloop()


if __name__ == "__main__":
    calc = Calculator()
