# imports libraries 
from tkinter import *
from time import strftime

window = Tk()
window.title('Digital Clock')

#function used time
def time():
    string = strftime('%H:%M:%S')
    lbl.config(text = string)
    lbl.after(1000,time)

# label 
lbl = Label(window,font=('arial',160,'bold'),bg='black',fg='white')
lbl.pack(anchor='center',fill='both',expand=1)

time()
# run application program
mainloop()