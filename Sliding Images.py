from itertools import cycle
import tkinter as tk

class App(tk.Tk):
    def __init__(self,image_files,x,y,delay):
        #TK window adjust to size of image
        tk.Tk.__init__(self)

        self.geometry("+{}+{}".format(x,y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image),image) for image in image_files)

        self.picture_display = tk.Label(self)
        self.picture_display.pack()
    # show images by slides 
    def show_slides(self):
        #cycle through the images & display them

        img_object , img_name = next(self.pictures)
        self.picture_display.config(image = img_object)
        self.title(img_name)
        self.after(self.delay,self.show_slides)

    def run(self):
        self.mainloop()

# time between every images 
delay = 3500

# file directions 
image_files = [ 
    'file_name_1',
    'file_name_2',
    'file_name_3'
]

x = 100
y = 50
# call program application  
app = App(image_files,x,y,delay)
app.show_slides()

# run application
app.run()
