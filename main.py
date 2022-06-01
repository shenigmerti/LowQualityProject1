from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")

# function
def time():
    string = strftime("%H:%M:%S %P")
    label.config(text=string)
    label.after(1000, time)
    
#configure font and details
label = Label(root, font=("ds-digital", 80), background="black", foreground="green")
label.pack(anchor="center")

time()

mainloop()
