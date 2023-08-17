from tkinter import *
from tkinter import ttk
from library_management.library_qry import management_qry
from tkinter import messagebox
import calendar

class Return:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to softwarica library')
        self.wn.geometry('900x650+70+10')
        self.wn.configure(bg='#A9A9A9')
        self.update_index = ""
        self.d1=dict()
        self.return_book = management_qry()
        for i in self.return_book.show_customer():
            self.d1[i[1]]=[i[3],i[6]]
        print(self.d1)
        # ----------------------------------topic-----------------------------------------------------------------------------
        self.fr1 = LabelFrame(window, width=450, height=50, bd=10)
        self.fr1.place(x=20, y=10)
        self.lbl_heading = Label(self.fr1, text='RETURN BOOK', font=('Antroposofia', 15, 'bold', 'italic'), fg='#6495ED')
        self.lbl_heading.place(x=00, y=0)
        # ______________________________Frame_______________________________________________________________
        self.frame1 = LabelFrame(window, width=450, height=570, bg='white', bd=0)
        self.frame1.place(x=20, y=60)
        font_family = "Gabriola"
        font_size = 15
        # ----------------------------- student name ----------------------------------------
        self.name_label = Label(window, text='Student name:', font=(font_family, font_size),bg='white')
        self.name_label.place(x=40, y=70)
        self.id = [i[1] for i in self.return_book.show_customer()]
        self.name_var = StringVar()
        self.name = ttk.Combobox(window, width=30, values=self.id, textvariable=self.name_var,postcommand=self.return_name)
        self.name.place(height=40, x=200, y=70)
        # -------------------------------------Book name---------------------------------------------------
        self.book_label = Label(window, text='Book Name:', font=(font_family, font_size),bg='white')
        self.book_label.place(x=40, y=130)
        self.book_var = StringVar()
        self.id1 = [i[1] for i in self.return_book.show_book()]
        self.book= Entry(window, width=30, textvariable=self.book_var)
        self.book.place(height=40, x=200, y=130)
        # -------------------------------------issue date---------------------------------------------------
        self.issue_date_label = Label(window, text='Issue Date', font=(font_family, font_size),bg='white')
        self.issue_date_label.place(x=40, y=190)
        self.issue_date_var = StringVar()
        self.issue_date = Entry(window, width=30, textvariable=self.issue_date_var)
        self.issue_date.place(height=40, x=200, y=190)
        # -------------------------------------Return date---------------------------------------------------
        self.return_label = Label(window, text='Return Date:', font=(font_family, font_size),bg='white')
        self.return_label.place(x=40, y=250)
        self.return_b = Entry(window, width=30)
        self.return_b.place(height=40, x=200, y=250)
        # ------------------return____________________________________________________________________-
        self.Return = Button(window, text='Book Return', bg='#F5F5DC', width=15, height=2, command=self.book_return)
        self.Return.place(x=200, y=300)
        self.Exit = Button(window, text='Exit', bg='#F5F5DC', width=15, height=2, command=self.wn.destroy)
        self.Exit.place(x=350, y=300)
        self.update = Button(window, text='Update', bg='#F5F5DC', width=15, height=2, command=self.update_button)
        self.update.place(x=50, y=300)
# --------------------------calender__________________________________________________________________________
        def show():
            a = int(spin1.get())
            b = int(spin2.get())
            cal = calendar.month(b, a)
            txt.delete(0.0, END)
            txt.insert(INSERT, cal)
        self.lb1 = Label(window, text="month", font=('arial', 9, 'bold')).place(x=590, y=50)
        self.lb2 = Label(window, text="Year", font=('arial', 9, 'bold')).place(x=690, y=50)
        spin1 = Spinbox(window, values=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12), width=4)
        spin1.place(x=645, y=50)
        spin2 = Spinbox(window, from_=1999, to=2100, width=4)
        spin2.place(x=740, y=50)
        # BUTTON
        self.btn = Button(window, text='Show', font=('arial', 9, 'bold'), command=show).place(x=670, y=80)
        txt = Text(window, width=24, height=8)
        txt.place(x=610, y=107)
# -----------------------------treeview -----------------------------------------------------------------------
        self.order_tree = ttk.Treeview(self.frame1, column=('Student Name', 'Book Name', 'Issue Date', 'Return Date'))
        self.order_tree.place(x=10,y=300)
        self.order_tree['show'] = 'headings'
        self.order_tree.column('Student Name', width=100, anchor='center')
        self.order_tree.column('Book Name', width=100, anchor='center')
        self.order_tree.column('Issue Date', width=100, anchor='center')
        self.order_tree.column('Return Date', width=100, anchor='center')
        self.order_tree.heading('Student Name', text='Student Name')
        self.order_tree.heading('Book Name', text='Book Name')
        self.order_tree.heading('Issue Date', text='Issue Date')
        self.order_tree.heading('Return Date', text='Return Date')
        self.show_tree()
        self.book.bind('<Button-1>',self.return_name)

    def return_name(self,event=None):
        name = self.name_var.get()
        book_name = self.book_var.get()
        issue_date = self.issue_date_var.get()
        if name in self.d1:
            self.book_var.set(self.d1[name][1])
            self.issue_date_var.set(self.d1[name][0])

    def book_return(self):
        name = self.name_var.get()
        book_name = self.book_var.get()
        issue_date = self.issue_date_var.get()
        return_date = self.return_b.get()
        if self.return_book.return_book(name, book_name, issue_date, return_date):
            messagebox.showinfo('Message', 'Book has been return by'+' '+name, parent=self.wn)
            self.return_book.delete_from_issue(name)
            self.show_tree()
        else:
            messagebox.showerror('ERROR', 'Unable to process', parent=self.wn)

    def show_tree(self):
        self.order_tree.delete(*self.order_tree.get_children())
        data = self.return_book.show_returned()
        print(data)
        for i in data:
            self.order_tree.insert("", "end", text=i[4], value=(i[0], i[1], i[2], i[3]))
        self.order_tree.bind("<Double-1>", self.on_book_select)

    def on_book_select(self, event):
        select_row = self.order_tree.selection()[0]
        select_item = self.order_tree.item(select_row, 'values')
        self.update_index = self.order_tree.item(select_row, 'text')
        self.name.set('')
        self.name.set(select_item[0])
        self.book.delete(0,END)
        self.book.insert(0,select_item[1])
        self.issue_date.delete(0,END)
        self.issue_date.insert(0,select_item[2])
        self.return_b.delete(0, END)
        self.return_b.insert(0, select_item[3])
        print(self.update_index)

    def update_button(self):
        if self.update_index == "":
            messagebox.showerror('Érror', 'Please select data')
        else:
            student_name = self.name.get()
            book_name = self.book_var.get()
            issue = self.issue_date.get()
            return_date = self.return_b.get()

            if student_name == "" or book_name == "" or issue == "" or return_date == "":
                messagebox.showerror('Érror', 'Please enter all values')
            elif self.return_book.return_book_update(student_name, book_name, issue, return_date, self.update_index):
                messagebox.showinfo('Message', 'Book has been return by' + ' ' + student_name, parent=self.wn)
                self.return_book.delete_from_issue(student_name)
                self.show_tree()
            else:
                messagebox.showerror('ERROR', 'Unable to process', parent=self.wn)


#
# wn=Tk()
# Return(wn)
# wn.mainloop()
