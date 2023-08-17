from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import*

class open_frame:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to library')
        self.wn.geometry('1080x650+30+10')
        self.canvas = Canvas(window,width=800,height= 600,highlightthickness=0)
        self.canvas.place(x=0,y=0)
        self.image_frame = []
        # ----------------------------------------animation------------------------------------------------------------------
        for i in range(1,125):
            img = 'images/ebook' + str(i) + '.png'
            self.image_frame += [PhotoImage(file=img)]
        self.lbl = Label(self.wn, bg='#ff6f58')
        self.lbl.place(x=780, y=0, height=300, width=300)
        self.working()
        self.animate(0)

        # ----------------------------------------frame------------------------------------------------------------------
        self.fr1 = LabelFrame(self.wn, width=320, height=310, bd=10)
        self.fr1.place(x=780, y=300)
        self.lbl_heading = Label(self.fr1, text='OPENS FROM 6:00 A.M TO 5:30PM ', font=('Antroposofia', 10, 'bold', 'italic'),fg='black')
        self.lbl_heading.place(x=0, y=0)
        self.lbl_heading = Label(self.fr1, text='RULES OF LIBRARY', font=('Antroposofia', 8, 'bold', 'italic'),fg='black')
        self.lbl_heading.place(x=10, y=30)
        rules = '''
        1.Maintain silence 

        2.Phone should be kept on silent mode

        3.Do not write in book 

        4.All books and periodicals must be returned
          to the shelves after use.

        5.It is forbidden to bring food into the Library.
        
        6.Conversations on mobile phones must be
            held outside of the Library.'''
        self.lbl_heading = Label(self.fr1, text=rules,justify=LEFT, font=('Antroposofia', 8, 'bold', 'italic'),fg='black')
        self.lbl_heading.place(x=-5, y=60)
        self.lbl_heading = Label(self.wn, text='WELCOME TO SOFTWARICA LIBRARY',justify=LEFT, font=('Antroposofia', 25, 'bold', 'italic'),fg='#c96560')
        self.lbl_heading.place(x=0, y=0)
        # ----------------------------------------button------------------------------------------------------------------
        self.admin = Button(self.wn,text='admin',width=20,command=self.button_admin)
        self.admin.place(x=350, y=520)

    def button_admin(self):
        self.wn.destroy()
        from library_management import login
        wn=Tk()

        admin=login.Login_frame(wn)
        mainloop()

    # ----------------------------------------clock_image------------------------------------------------------------------
    def clock_image(self, hr, min_, sec_):
        clock = Image.new('RGB', (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)
        bg = Image.open('square_clock.png')
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))
        origin = 200, 200
        # _________________for line________________
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill='black', width=4)
        # min______________________
        draw.line((origin, 200 + 80 * sin(radians(min_)), 200 - 80 * cos(radians(min_))), fill='orange', width=3)
        # sec_________________
        draw.line((origin, 200 + 100 * sin(radians(sec_)), 200 - 100 * cos(radians(sec_))), fill='brown', width=4)
        draw.ellipse((195, 195, 210, 210), fill='black')
        clock.save('clock_new.png')

    def animate(self,frame_rate):
        def start():
            self.canvas.create_image(400,300, image=self.image_frame[frame_rate],tag='books')
        self.canvas.delete('books')
        try:
            start()
        except IndexError:
            frame_rate=0
            start()
        frame_rate +=1
        self.canvas.after(10,self.animate,frame_rate)


    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second
        print(h, m, s)
        hr = (h / 12) * 360
        min_ = (m / 60) * 360
        sec_ = (s / 60) * 360
        self.clock_image(hr, min_, sec_)
        self.img = PhotoImage(file='clock_new.png')
        self.lbl.config(image=self.img)
        self.lbl.after(200, self.working)

wn = Tk()
open_frame(wn)
wn.mainloop()
