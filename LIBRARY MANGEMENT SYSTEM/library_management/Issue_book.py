from tkinter import *
from tkinter import ttk
from library_management.library_qry import management_qry
from tkinter import messagebox
import calendar



class Issue:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to softwarica library')
        self.wn.geometry('900x650+70+10')
        self.wn.configure(bg='#EEE8AA')
        self.wn.resizable(0, 0)

        self.update_index = ""
        self.bookid = management_qry()
        self.all_books = self.bookid.show_book()


        self.title_photo = PhotoImage(file="ii.png")
        self.title_photo_lable = Label(self.wn, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=580, y=350)


        self.lb_heading = Label(window, text="BOOK ISSUE ", font=('Elephant', 20), fg='red', bg='#EEE8AA')
        self.lb_heading.place(x=100, y=0)

        self.frame1 = LabelFrame(window, width=550, height=570, bg='white', bd=0)
        self.frame1.place(x=20, y=50)

        self.Book_Issue = Button(window, text='Book Issue', bg='#DEB887', width=15, height=2, command=self.book_issue)
        self.Book_Issue.place(x=200, y=310)

        self.Update = Button(window, text='Update', bg='#DEB887', width=15, height=2, command=self.update_button)
        self.Update.place(x=50, y=310)

        self.Exit = Button(window, text='Exit', bg='#DEB887', width=15, height=2, command=self.wn.destroy)
        self.Exit.place(x=350, y=310)

        ###################
        font_family = "Gabriola"
        font_size = 15
        self.name_label = Label(window, text='Student Name:', bg='white', font=(font_family, font_size))
        self.name_label.place(x=40, y=70)

        self.name = Entry(window, width=30)
        self.name.place(height=40, x=200, y=70)

        # Book id
        self.id_label = Label(window, text='Book Name', bg='white', font=(font_family, font_size))
        self.id_label.place(x=40, y=130)
        self.id_var = StringVar()

        book_show=[]
        for i in self.all_books:
            book_show.append(i[1])

        self.id = ttk.Combobox(window, width=30, textvariable=self.id_var, values=book_show)
        self.id.place(height=40, x=200, y=130)
#issue
        self.issue_label = Label(window, text='Issue Date', bg='white', font=(font_family, font_size))
        self.issue_label.place(x=40, y=190)

        self.issue_var = StringVar()
        self.issue = Entry(window, width=30, textvariable=self.issue_var)
        self.issue.place(height=40, x=200, y=190)
#expiry
        self.expiry_label = Label(window, text='Expiry Date', bg='white', font=(font_family, font_size))
        self.expiry_label.place(x=40, y=250)

        self.ex_var = StringVar()
        self.ex = Entry(window, width=30, textvariable=self.ex_var)
        self.ex.place(height=40, x=200, y=250)

        self.order_tree = ttk.Treeview(self.frame1, column=('Student Name', 'Book ID','Book name' ,'Issue Date', 'Expiry Date'))
        self.order_tree.place(x=10, y=315)
        self.order_tree['show'] = 'headings'
        self.order_tree.column('Student Name', width=100, anchor='center')
        self.order_tree.column('Book ID', width=100, anchor='center')
        self.order_tree.column('Book name', width=100, anchor='center')
        self.order_tree.column('Issue Date', width=100, anchor='center')
        self.order_tree.column('Expiry Date', width=100, anchor='center')
        self.order_tree.heading('Student Name', text='Student Name')
        self.order_tree.heading('Book ID', text='Book ID')
        self.order_tree.heading('Book name', text='Book name')
        self.order_tree.heading('Issue Date', text='Issue Date')
        self.order_tree.heading('Expiry Date', text='Expiry Date')

        self.show_tree()

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

    def show_tree(self):
        try:
            self.order_tree.delete(*self.order_tree.get_children())
            info = self.bookid.show_customer()
            for i in info:
                self.order_tree.insert("", "end", text=i[0], value=(i[1], i[2],i[6], i[3], i[4]))
            self.order_tree.bind("<Double-1>", self.on_book_select)
        except Exception as error:
            print(error)

    def on_book_select(self, event):
        select_row = self.order_tree.selection()
        select_item = self.order_tree.item(select_row, 'values')
        self.update_index = self.order_tree.item(select_row, 'text')
        self.name.delete(0, END)
        self.name.insert(0, select_item[0])
        self.id.set('')
        self.id.set(select_item[1])
        self.issue.delete(0, END)
        self.issue.insert(0, select_item[2])
        self.ex.delete(0, END)
        self.ex.insert(0, select_item[3])

    def book_issue(self):
        if self.update_index == "":
            print(self.update_index,'book issue')
            name = self.name.get()
            #id = self.id_var.get()
            selected=self.id.current()
            id=self.all_books[selected][0]
            issue_date = self.issue_var.get()
            expiry_date = self.ex_var.get()
            try:
                if name == "" or id == "" or issue_date == "" or expiry_date == "":
                    messagebox.showerror('Érror', 'Please enter all values')
                elif self.bookid.issue_book(name, id, issue_date, expiry_date):
                    messagebox.showinfo('Issued', 'Book received by'+' '+name, parent=self.wn)
                    self.show_tree()
                else:
                    messagebox.showerror('ERROR', 'unable to add', parent=self.wn)
            except:
                pass
        else:
            messagebox.showerror('Érror', 'Data is selected')

    def update_button(self):
        if self.update_index == "":
            messagebox.showerror('Érror', 'Please select data')
            print(self.update_index)
        else:
            print(self.update_index,'after else')
            name = self.name.get()
            id = self.id_var.get()
            issue_date = self.issue_var.get()
            expiry_date = self.ex_var.get()
            try:
                if name == "" or id == "" or issue_date == "" or expiry_date == "":
                    messagebox.showerror('Érror', 'Please enter all values')
                elif self.bookid.issue_book_update(self.update_index, name, id, issue_date, expiry_date):
                    messagebox.showinfo('Issued', 'Book received by'+' '+name, parent=self.wn)
                    self.show_tree()
                    self.update_index=''
                else:
                    messagebox.showerror('ERROR', 'unable to add', parent=self.wn)
            except:
                pass



#
# wn=Tk()
# Issue(wn)
# wn.mainloop()
#
