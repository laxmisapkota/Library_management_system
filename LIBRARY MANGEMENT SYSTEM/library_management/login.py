from tkinter import *
from tkinter import messagebox
from library_management import register
from library_management.user_qry import Staff

class Login_frame:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Login/SignUp Form')
        self.wn.geometry('1000x650+70+10')
        self.wn.configure(bg='black')
        self.lb_heading = Label(self.wn, text="Login System ", font=('Elephant', 20), fg='red', bg='yellow')
        self.lb_heading.place(x=100, y=0)
        self.log = Staff()
        # ----------------------------- back ground photo---------------------------------------------------------------
        global background
        background = PhotoImage(file='jxk.png')
        self.img_bg = Label(self.wn, image = background)
        self.img_bg.place(x=0, y=0)
        # ----------------------------- frame 1------------------------------------------------------------------
        self.frame1 = LabelFrame(wn, width=395, height=455, bg='white', bd=0)
        self.frame1.place(x=470, y=100)
        # ----------------------------- topic----------------------------------------
        self.title1 = Label(self.frame1, text='LIBRARY', bg='white', fg='#8428e5', font=('Arial', 40))
        self.title1.place(x=100, y=5)
        self.title2 = Label(self.frame1, text=' SYSTEM MANAGEMENT', bg='white', fg='#8428e5',
                            font=('Arial', 15))
        self.title2.place(x=100, y=70)
        # ----------------------------- book photo----------------------------------------
        self.title_photo = PhotoImage(file="book.png")
        self.title_photo_lable = Label(self.frame1, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=20, y=10)
        # self.wn.wm_attributes("-transparentcolor","white")
        # ----------------------------- variable----------------------------------------
        font_family = "Gabriola"
        font_size = 20
        self.title_photo = PhotoImage(file="user.png")
        self.name_label = Label(text='Username:', image=self.title_photo, compound=LEFT, font=(font_family, font_size),bg="white")
        self.name_label.image = self.title_photo
        self.name_label.place(x=500, y=300)
        self.username_var = StringVar()
        self.username = Entry(width=30)
        self.username.place(height=50, x=650, y=300)

        self.title_photo1 = PhotoImage(file="images.png")
        # ----------------------------------------password------------------------------------------------------------------
        self.p_label = Label(text='Password:', image=self.title_photo1, compound=LEFT, font=(font_family, font_size),bg='white')
        self.p_label.image = self.title_photo1
        self.p_label.place(x=500, y=400)
        self.password_var = StringVar()
        self.password = Entry(width=30, show="*")
        self.password.place(height=50, x=650, y=400)
        # -------------------------------------signup--------------------------------------------------------
        self.sign_up = Button(text='Sign up', bg='green', height='0',command=self.signup)
        self.sign_up.place(x=800, y=100)
        # register
        self.login = Button(text='Login', bg='green', command=self.login)
        self.login.place(x=800, y=480)
        # ----------------------------- animated photo ----------------------------------------
        self.title_photo = PhotoImage(file="Untitled.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=180, y=100)
        self.im1 = PhotoImage(file="imm.png")
        self.im2 = PhotoImage(file="ee.png")
        self.im3 = PhotoImage(file="im2.png")
        self.im4 = PhotoImage(file="mmm.png")
        self.im5 = PhotoImage(file="11.png")
        self.lbl_change_image = Label(self.wn, bg='white')
        self.lbl_change_image.place(x=265, y=153, width=190, height=380)
        self.animate()
        self.frame = LabelFrame(self.wn).pack()

    # ----------------------------- function for photo ----------------------------------------
    def animate(self):
        self.im = self.im1
        self.im1 = self.im2
        self.im2 = self.im3
        self.im3 = self.im4
        self.im4 = self.im5
        self.im5 = self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000, self.animate)

    def signup(self):
        window = register.Register(self.frame)

    # ----------------------------- login function ----------------------------------------
    def login(self):
        details = self.log.login(self.username.get(), self.password.get())
        print(details)
        try:
            if self.username.get() == "" or self.password.get() == "":
                messagebox.showerror('Error', 'All fields are required!!', parent=self.wn)

            elif self.username.get() in details[0] and self.password.get() in details[0]:
                messagebox.showinfo("successfull", f"welcome {self.username.get()}")
                user_name = self.username.get()
                self.wn.destroy()
                from library_management import home1
                win = Tk()
                new = home1.Main(win, user_name)
                mainloop()
            else:
                messagebox.showerror('Error', "Incorrect username or password")
        except:
                pass

wn = Tk()
Login_frame(wn)
wn.mainloop()
