from tkinter import *
import os

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):
        
        def cameracall():
            exec(open("realtimedata.py").read()) 
            
        def traincall():
            exec(open("Make_aligndata_git.py").read()) 
            exec(open("Make_classifier_git.py").read()) 
        # changing the title of our master widget      
        self.master.title("Face Recognition")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        Camera = Button(self, text="Start Recognition",command = cameracall)
        Upload = Button(self, text="Train  model",command = traincall)
        # placing the button on my window
        Camera.place(x=165, y=100)
        Upload.place(x=180, y = 150)

root = Tk()

#size of the window
root.geometry("400x300")

app = Window(root)
root.mainloop()