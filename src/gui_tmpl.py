from tkinter import *

class myapp:
    
    window = None
    lbl = None
    btn = None
    txt = None 
    
    def __init__(self):
        self.window = Tk() 
        self.window.title("Welcome to LikeGeeks app")
        self.window.geometry('350x200')
        self.lbl = Label(self.window, text="Hello")
        self.lbl.grid(column=0, row=0)
        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=1, row=0)  
        self.txt = Entry(self.window,width=10)
        self.txt.grid(column=2, row=0)  
 
    def clicked(self):
        if self.txt.get() == "":
            self.lbl.configure(text="Button was clicked !!")
        else:
            self.lbl.configure(text=self.txt.get())
 
    def startapp(self):
        self.window.mainloop()
        
if __name__ == '__main__':
    a = myapp()
    a.startapp()