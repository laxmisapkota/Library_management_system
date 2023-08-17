from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
import time
from math import*


class Main:
    def __init__(self, window, user_name):
        self.wn = window
        self.wn.title('Welcome to softwarica library')
        self.wn.geometry('1280x650+70+10')
        self.wn.configure(bg='#DEB887')
# ----------------------------------------heading------------------------------------------------------------------
        self.lb_heading = Label(self.wn, text="WELCOME TO SOFTWARICA LIBRARY ", font=('Elephant', 20),
                                fg='#D2691E', bg='#DEB887')
        self.lb_heading.place(x=300, y=2)
        # issue book
        self.issue_book = PhotoImage(file="im2.png")
        self.issue_book_lable = Label(self.wn, image=self.issue_book, bg="white")
        self.issue_book_lable.image = self.issue_book
        self.issue_book_lable.place(x=50, y=300)
        self.issue = Button(height=300,text='Book issue',width=300,image=self.issue_book,command=self.button_book_issue,compound=BOTTOM,font=('arial',40))
        self.issue.place(x=50, y=300)
        # ----------------------------------------return------------------------------------------------------------------
        self.return_book = PhotoImage(file="return.png")
        self.return_book_lable = Label(self.wn, image=self.return_book, bg="white")
        self.return_book_lable.image = self.return_book
        self.return_book_lable.place(x=900, y=300)
        self.issue = Button(height=300,text='Book return',width=300,image=self.return_book,command=self.button_book_return,compound=BOTTOM,font=('arial',40))
        self.issue.place(x=900, y=300)
        # ----------------------------------------detail------------------------------------------------------------------
        self.detail_book = PhotoImage(file="detail.png")
        self.detail_book_lable = Label(self.wn, image=self.detail_book, bg="white")
        self.detail_book_lable.image = self.detail_book
        self.detail_book_lable.place(x=500, y=300)
        self.detail = Button(height=300, text='Details',width=300, image=self.detail_book, command=self.button_book_details,compound=BOTTOM,font=('arial',40))
        self.detail.place(x=500, y=300)
        self.login = Button(self.wn, text='Manage', bg='#808080', width=15, height=2, command=self.book_mgmt)
        self.login.place(x=1080, y=200)

    def book_mgmt(self):
        from library_management import book_management
        win = Toplevel()
        book = book_management.Detail_frame(win)

    def button_book_issue(self):
        from library_management import Issue_book
        win = Toplevel()
        book = Issue_book.Issue(win)

    def button_book_details(self):
        from library_management import book_details
        win = Toplevel()
        book = book_details.Book(win)

    def button_book_return(self):
        from library_management import Return_book
        win = Toplevel()
        book = Return_book.Return(win)

wn = Tk()
Main(wn,'text')
wn.mainloop()
