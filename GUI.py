import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import cv2

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "click me"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.submit = tk.Button(self, text = 'Select file path', command = self.changepath)
        self.submit.pack(side ='top')

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def changepath(self):
        path = askopenfilename();
        print(path)
        if(path[-3:] != 'png' and path[-3:] != 'jpg' and path[-3:] != 'peg'):
            print('Invalid imagefile')
        else:
            img = cv2.imread(path,0);
            print(img)

    def say_hi(self):
        print("hi !")

root = tk.Tk()
root.config(background = 'red')
app = Application(master=root)
app.mainloop()
