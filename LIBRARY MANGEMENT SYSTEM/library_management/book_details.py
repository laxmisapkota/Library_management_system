from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from library_management.library_qry import management_qry

class Book:
    def __init__(self, window):
        self.wn = window
        self.wn.title('Welcome to softwarica library')
        self.wn.geometry('600x650+70+10')
        self.wn.configure(bg='white')
        self.load_book = management_qry()
        self.update_index = ""
        # print(self.load_book.show_book())

        self.d = dict()
        for i in range(len(self.load_book.show_book())):
            self.d[i] = [self.load_book.show_book()[i][0:]]
            # print(self.d)
        self.input = [i[1] for i in self.load_book.show_book()]
        # print(self.input)

        self.bookid = management_qry()
        self.all_books = self.bookid.show_book()
        self.lb_heading = Label(window, text="BOOK DETAILS ", font=('Elephant', 20), fg='#B8860B', bg='#FFF8DC')
        self.lb_heading.place(x=100, y=0)
# -----------------------------frame----------------------------------------------------------------------------------------------------------------
        self.frame1 = LabelFrame(window, width=550, height=500, bg='white', bd=0)
        self.frame1.place(x=20, y=50)
# -----------------------------image_____________________________________________________________________________________________________________________
        self.title_photo = PhotoImage(file="de.png")
        self.title_photo_lable = Label(self.frame1, image=self.title_photo, bg="white")
        self.title_photo_lable.image = self.title_photo
        self.title_photo_lable.place(x=20, y=10)
        font_family = "Gabriola"
        font_size = 15
#--------------------------------------Book name-----------------------------------------------------------------------------------------
        self.id_label = Label(window, text='Book Name', bg='white', font=(font_family, font_size))
        self.id_label.place(x=40, y=70)
        self.book_id_var = StringVar()
        book_show=[]
        for i in self.all_books:
            book_show.append(i[1])
        self.book_id = ttk.Combobox(window, width=30, values=book_show, textvariable=self.book_id_var)
        self.book_id.place(height=50, x=200, y=70)
#-------------------------------------search------------------------------------------------------------------
        self.login = Button(window, text='Search', bg='grey', width=15, height=2, command=self.search)
        self.login.place(x=200, y=150)
#--------------------------------------exit---------------------------------------------------------------------
        self.login = Button(window, text='Exit', bg='grey', width=15, height=2, command=self.wn.destroy)
        self.login.place(x=350, y=150)
        self.book_tree = ttk.Treeview(self.frame1, column=('Book id', 'Book Name', 'Subject', 'Author', 'Copies'))
        self.book_tree.place(x=10, y=150)
        self.book_tree['show'] = 'headings'
        self.book_tree.column('Book id', width=100, anchor='center')
        self.book_tree.column('Book Name', width=100, anchor='center')
        self.book_tree.column('Subject', width=100, anchor='center')
        self.book_tree.column('Author', width=100, anchor='center')
        self.book_tree.column('Copies', width=100, anchor='center')
        self.book_tree.heading('Book id', text='Book id')
        self.book_tree.heading('Book Name', text='Book Name')
        self.book_tree.heading('Subject', text='Subject')
        self.book_tree.heading('Author', text='Author')
        self.book_tree.heading('Copies', text='Copies')

    def binary_search_iterative(self, list, key):
        start = 0
        end = len(list) - 1
        while start <= end:
            mid = (start + end) // 2
            if list[mid][1] == key:
                return mid
            elif list[mid][1] > key:
                end = mid - 1
            else:
                start = mid + 1
        return -1

    def search(self):
        self.name = self.book_id.get()
        if self.name == '':
            messagebox.showerror('ERROR', 'CANNOT PROCESS YOUR REQUEST...')
        # elif self.name in self.input:
        #     self.look = self.d[self.input.index(self.name)]
        #     messagebox.showinfo('Found', 'book found', parent=self.wn)
        #     self.show_book_tree()
        else:
            book_info = self.all_books[(self.binary_search_iterative(self.all_books, self.name))]
            # print("after binary serching", book_info)
            self.show_book_tree(book_info)
            # messagebox.showerror('Error', 'error while processing', parent=self.wn)

    def show_book_tree(self, data):
        self.book_tree.delete(*self.book_tree.get_children())
        self.book_tree.insert("", "end", text=data[0], value=(data[0], data[1], data[2], data[3], data[4]))

    # def show_book_tree(self):
    #     self.book_tree.delete(*self.book_tree.get_children())
    #     data = self.load_book.search(self.name)
    #     print(self.look)
    #     for i in self.look:
    #         self.book_tree.insert("", "end", text=i[0], value=(i[0], i[1], i[2], i[3], i[4]))
        # self.book_tree.bind("<Double-1>", self.on_book_select)


#
# wn=Tk()
# Book(wn)
# wn.mainloop()
