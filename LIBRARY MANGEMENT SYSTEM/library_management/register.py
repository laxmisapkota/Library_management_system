from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from library_management.user_qry import Staff


class Register:
    def __init__(self, screen_em):
        self.screen_em = screen_em
        self.sign_up = Staff()
# ------main frame---------------------------------------------------------------------------------------------------#
        self.main_frame=Label(screen_em, width=1000, height=600, bg='white', bd=0)
        self.main_frame.pack()
# ------frame 1------------------------------------------------------------------------------------------------------#
        self.employee_frame = LabelFrame(self.main_frame, width=572, height=730, bg='white')
        self.employee_frame.place(x=0, y=0)
# ------form title---------------------------------------------------------------------------------------------------#
        self.title = Label(self.employee_frame, text='STAFF REGISTRATION', font=('Arial', 20, 'bold'), bg='white')
        self.title.place(x=10, y=10)
        self.title_head = Label(self.employee_frame, text='Please fill out your information below.', bg='white',
                                font=('Arial', 10)).place(x=10, y=45)
# ------border line--------------------------------------------------------------------------------------------------#
        self.line = Label(self.employee_frame, width=80, height=0, bg='grey').place(x=0, y=70)
        self.head = Label(self.employee_frame, text='Personal Information', font=('Arial', 15, 'bold'), bg='white')
        self.head.place(x=10, y=95)
# ------Employee form entries----------------------------------------------------------------------------------------#
# ------First and last name------------------------------------------------------------------------------------------#
        self.firstname = StringVar()
        self.lastname = StringVar()
        self.name = Label(self.employee_frame, text='Name:', font=('Arial', 10, 'bold'), bg='white').place(x=10, y=140)
        self.first_name_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.firstname)
        self.first_name_entry.place(x=10, y=164)
        self.first_label = Label(self.employee_frame, text='First Name', font=('Arial', 8), bg='white').place(x=10,
                                                                                                              y=185)
        self.last_name_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.lastname)
        self.last_name_entry.place(x=150, y=164)
        self.last_label = Label(self.employee_frame, text='Last Name', bg='white', font=('Arial', 8)).place(x=150,y=185)
# ------date of birth------------------------------------------------------------------------------------------------#
        self.DOB = StringVar()
        self.date = Label(self.employee_frame, text='Date Of Birth:', bg='white', font=('Arial', 10, 'bold')).place(
            x=10, y=215)
        self.date_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.DOB)
        self.date_entry.place(x=10, y=240)
        self.date_format = Label(self.employee_frame, text='Format:YY/MM/DD', font=('Arial', 8), bg='white').place(
            x=140, y=240)
# ------address------------------------------------------------------------------------------------------------------#
        self.city = StringVar()
        self.state = StringVar()
        self.address = Label(self.employee_frame, text='Address:', bg='white', font=('Arial', 10, 'bold')).place(x=10, y=275)
        self.city_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.city)
        self.city_entry.place(x=10, y=300)
        self.state_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.state)
        self.state_entry.place(x=150, y=300)
        self.city_label = Label(self.employee_frame, text='City', bg='white', font=('Arial', 8)).place(x=20, y=320)
        self.state_label = Label(self.employee_frame, text='Province', bg='white', font=('Arial', 8)).place(x=160, y=320)
# ------contact------------------------------------------------------------------------------------------------------#
        self.code_no = StringVar()
        self.phone_no = StringVar()
        self.phone_no_label = Label(self.employee_frame, text='PHONE NO.:', bg='white', font=('Arial', 10, 'bold')).place(
            x=10, y=350)
        self.code = Entry(self.employee_frame, width=5, bg='light grey', textvariable=self.code_no)
        self.code.place(x=10, y=375)
        self.code.insert(0, '+')
        self.code_label = Label(self.employee_frame, text='Code', font=('Arial', 8), bg='white')
        self.code_label.place(x=10, y=395)
        self.number = Entry(self.employee_frame, bg='light grey', textvariable=self.phone_no)
        self.number.place(x=55, y=375)
        self.number_label = Label(self.employee_frame, text='Number', font=('Arial', 8), bg='white')
        self.number_label.place(x=60, y=395)
# ------email address------------------------------------------------------------------------------------------------#
        self.email = StringVar()
        self.email_label = Label(self.employee_frame, text='Email:', bg='white', font=('Arial', 10, 'bold')).place(x=10,
                                                                                                             y=420)
        self.email_entry = Entry(self.employee_frame, width=38, bg='light grey', textvariable=self.email)
        self.email_entry.place(x=10, y=445)

# ------Gender----------------------------------------------------------------------------------------------------------#
        self.gender_var = StringVar()
        self.Gender = Label(self.employee_frame, text='Gender:', bg='white', font=('Arial', 10, 'bold')).place(x=10, y=470)
        self.gender = ttk.Combobox(self.employee_frame, values=['-', 'Male', 'Female', 'Others'], textvariable=self.gender_var)
        self.gender.place(x=10, y=493)
        self.gender.current(0)
        self.gender.config(state='readonly')
# ------marital status-----------------------------------------------------------------------------------------------#
        self.marry = StringVar()
        self.marital = Label(self.employee_frame, text='Marital Status:', bg='white', font=('Arial', 10, 'bold')).place(
            x=200, y=470)
        self.marital_combo = ttk.Combobox(self.employee_frame, values=['-', 'Married', 'Unmarried'], textvariable=self.marry)
        self.marital_combo.place(x=200, y=493)
        self.marital_combo.current(0)
        self.marital_combo.config(state='readonly')
# ------username-----------------------------------------------------------------------------------------------#
        self.Username = StringVar()
        self.Username_label = Label(self.employee_frame, text='Username:', font=('Arial', 10, 'bold'), bg='white')
        self.Username_label.place(x=350, y=140)
        self.Username_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.Username)
        self.Username_entry.place(x=350, y=164)
        # ----------------------------- password----------------------------------------
        self.Password = StringVar()
        self.Password_label = Label(self.employee_frame, text='Password:', font=('Arial', 10, 'bold'), bg='white')
        self.Password_label.place(x=350, y=216)
        self.Password_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.Password, show="*")
        self.Password_entry.place(x=350, y=240)
        # ----------------------------- confirm password----------------------------------------
        self.Conform_Password = StringVar()
        self.Conform_Password_label = Label(self.employee_frame, text='Conform Password:', font=('Arial', 10, 'bold'), bg='white')
        self.Conform_Password_label.place(x=350, y=286)
        self.Conform_Password_entry = Entry(self.employee_frame, bg='light grey', textvariable=self.Conform_Password, show="*")
        self.Conform_Password_entry.place(x=350, y=310)
        # ----------------------------- Button----------------------------------------
        self.button_signup = Button(self.employee_frame, text='Sign Up', font=('Arial', 15, 'bold'),
                                     relief=SUNKEN, bg='white', command=self.but_func)
        self.button_signup.place(x=10, y=540)
        self.back_button = Button(self.employee_frame, text='<<Back', bg='white', command=self.back)
        self.back_button.place(x=500, y=30)
    # -------------------------------Button Function------------------------
    def back(self):
        self.main_frame.pack_forget()
        self.main_frame.destroy()

    def but_func(self):
        first_name = self.firstname.get()
        last_name = self.lastname.get()
        dob = self.DOB.get()
        city = self.city.get()
        state = self.state.get()
        number = self.code_no.get() + self.phone_no.get()
        email = self.email.get()
        gender = self.gender_var.get()
        marital = self.marry.get()
        username = self.Username.get()
        confirm_password = self.Conform_Password.get()

        if self.sign_up.register(username, confirm_password, first_name, last_name, dob, city, state, number, email, gender, marital):
            messagebox.showinfo('ADDED', 'Account created')
        else:
            messagebox.showerror('Error', 'Request unable to process')


# screen = Tk()
# dis = Register(screen)
# screen.geometry('1000x600')
# screen.mainloop()
