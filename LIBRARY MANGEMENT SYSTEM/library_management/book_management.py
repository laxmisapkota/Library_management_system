from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from library_management.library_qry import management_qry
import random


class Detail_frame:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to Softwarica Library')
        self.wn.geometry('600x650+70+10')
        self.wn.configure(bg='white')
        self.book = management_qry()
        self.update_index = ''

        global background
        background = PhotoImage(file='man.png')
        self.img_bg = Label(self.wn, image =background)
        self.img_bg.place(x=0, y=0)


        self.fr1 = LabelFrame(self.wn, width=550, height=50, bd=10)
        self.fr1.place(x=20, y=50)
        self.lbl_heading = Label(self.fr1, text='DETAILS INFORMATION', font=('Antroposofia', 15, 'bold', 'italic'),
                                 fg='#6495ED')
        self.lbl_heading.place(x=00, y=0)

        self.book_name = Label(self.wn, text="Book Name:")
        self.book_name.place(x=20, y=120)

        self.entry_name = Entry(self.wn)
        self.entry_name.place(x=110,y=120)

        self.book_type = Label(self.wn, text="Type")
        self.book_type.place(x=20, y=150)

        self.entry_type = Entry(self.wn)
        self.entry_type.place(x=110, y=150)

        self.item_author = Label(self.wn, text="Author")
        self.item_author.place(x=20, y=180)

        self.entry_author = Entry(self.wn)
        self.entry_author.place(x=110, y=180)

        self.item_add = Button(self.wn, text="Add Book", command=self.add_item)
        self.item_add.place(x=40,y=250)

        self.item_update = Button(self.wn, text="Update Book", command=self.update_item)
        self.item_update.place(x=140,y=250)

        self.item_update = Button(self.wn, text="Delete Book", command=self.delete_book)
        self.item_update.place(x=250,y=250)

        self.item_tree = ttk.Treeview(self.wn, columns=('Book id', 'Book Name', 'Type', 'Author'))
        self.item_tree.place(x=10,y=300)
        self.item_tree['show'] = 'headings'
        self.item_tree.column('Book id', width=100)
        self.item_tree.column('Book Name', width=100)
        self.item_tree.column('Type', width=100)
        self.item_tree.column('Author', width=100)
        self.item_tree.heading('Book id', text="Book id")
        self.item_tree.heading('Book Name', text="Book Name")
        self.item_tree.heading('Type', text="Type")
        self.item_tree.heading('Author', text="Author")

        self.show_book_tree()

    def add_item(self):
        no = random.randint(0,11)
        name = self.entry_name.get()
        book_id = '#'+name[0::3]+str(no)
        type = self.entry_type.get()
        author = self.entry_author.get()
        book_copy = random.randint(0, 101)
        if self.validate():
            if self.book.add_book(book_id, name, type, author, book_copy):
                print('yes')
                messagebox.showinfo('Book', "Book Added", parent=self.wn)
                self.show_book_tree()
            else:
                print('no')
                messagebox.showerror("Error", "Unable to add", parent=self.wn)
# ---------------------------update book-----------------------------------------------------------------
    def update_item(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first", parent=self.wn)
        else:
            no = random.randint(0, 11)
            name = self.entry_name.get()
            book_id = '#' + name[0::3] + str(no)
            type = self.entry_type.get()
            author = self.entry_author.get()

            if self.book.update_book(book_id, name, type, author, self.update_index):
                messagebox.showinfo('Book', "Book Updated", parent=self.wn)
                self.show_book_tree()
                self.update_index = ""
            else:
                messagebox.showerror("Error", 'Cannot be updated !!!', parent=self.wn)
# ---------------------------delete book-----------------------------------------------------------------
    def delete_book(self):
        if self.update_index == "":
            messagebox.showerror("Error", "Please select a row first", parent=self.wn)
        else:
            if self.book.delete_from_book_management(self.update_index):
                messagebox.showinfo('DELETED', "Book Deleted", parent=self.wn)
                self.show_book_tree()
                self.update_index = ""
                self.entry_name.delete(0, END)
                self.entry_type.delete(0, END)
                self.entry_author.delete(0, END)
            else:
                messagebox.showerror("Error", 'Cannot be removed!!!', parent=self.wn)
# ---------------------------function to show book in tree-----------------------------------------------------------------
    def show_book_tree(self):
        self.item_tree.delete(*self.item_tree.get_children())
        data = self.book.show_book()
        for i in data:
            self.item_tree.insert("", "end", text=i[0], value=(i[0],i[1], i[2], i[3]))
        self.item_tree.bind("<Double-1>", self.on_book_select)

    def on_book_select(self, event):
        selected_row = self.item_tree.selection()[0]
        selected_item = self.item_tree.item(selected_row, 'values')
        self.update_index = self.item_tree.item(selected_row, 'text')
        self.entry_name.delete(0, END)
        self.entry_name.insert(0, selected_item[1])
        self.entry_type.delete(0, END)
        self.entry_type.insert(0, selected_item[2])
        self.entry_author.delete(0, END)
        self.entry_author.insert(0, selected_item[3])

    def validate(self):
        name = self.entry_name.get()
        type = self.entry_type.get()
        author = self.entry_author.get()
        if name == '' or type == '' or author == '':
            messagebox.showerror('Error', 'Fill all the fields', parent=self.wn)
            return False
        else:
            return True

#
#wn = Tk()
# Detail_frame(wn)
# wn.mainloop()

