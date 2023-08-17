from tkinter import *
from PIL import Image

class open_frame:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Login Form')
        self.wn.geometry('1050x650+70+10')

        global back
        back = PhotoImage(file='111.png')
        self.img_bg = Label(self.wn, image = back)
        self.img_bg.place(x=0, y=0)
        #title=Label(self.wn,text="Webcode Analog Clock ",font=('times new roman',50,'bold')),bg=''
        self.lbl=Label(self.wn,bg='white')
        self.lbl.place(x=450,y=150,height=400,width=400)
        #self.working()
    def clock_image(self):
        clock=Image.new('RGB',(400,400),(255,255,255))












wn=Tk()
open_frame(wn)
mainloop()