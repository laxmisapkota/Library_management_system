from library_management.connection import MyDb

class management_qry:
    def __init__(self):
        self.connect = MyDb()

    def add_book(self, book_id, name, types, author, copies):      # Book_management
        qry = "INSERT INTO BOOKS(Book_ID, Book_name, Type, Author, Copies) VALUES(%s, %s, %s, %s, %s)"
        values = (book_id, name, types, author, copies)
        self.connect.iud(qry, values)
        return True

    def update_book(self, book_id, name, types, author,copies, row):     # Book_management
        qry = "UPDATE BOOKS SET Book_ID = %s, Book_name =%s , Type = %s, Author = %s, Copies= %s WHERE Book_ID = %s"
        values = (book_id, name, types, author,copies, row)
        self.connect.iud(qry, values)
        return True

    def show_book(self):          # Book_management
        qry = "SELECT * FROM BOOKS"
        data = self.connect.show_data(qry)
        return data

    def delete_from_book_management(self, ID):   # Book_management
        qry = "DELETE FROM Books WHERE Book_id = %s"
        data = self.connect.iud(qry, (ID,))
        return data

    def search(self, key):        # Book_management
        qry = "SELECT * FROM BOOKS WHERE Book_name LIKE '" + key + "%'"
        info = self.connect.show_data(qry)
        return info

    def issue_book(self, name, book_id, issue_date, expiry_date):    # Issue_book
        qry = "INSERT INTO Issue(Student_name, Book_id, Issue_date, Expiry_date) VALUES (%s,%s,%s,%s)"
        values = (name, book_id, issue_date, expiry_date)
        self.connect.iud(qry, values)
        return True

    def issue_book_update(self, row, name, book_id, issue_date, expiry_date):    # Issue_book
        qry = "UPDATE Issue SET Student_name = %s, Book_id = %s, Issue_date = %s, Expiry_date= %s WHERE id = %s"
        values = (name, book_id, issue_date, expiry_date, row)
        self.connect.iud(qry, values)
        return True

    def show_customer(self):     # Issue_book
        qry = "SELECT * FROM `issue` JOIN books on issue.Book_id=books.Book_ID"
        data = self.connect.show_data(qry)
        return data

    def delete_from_issue(self, ID):   # Issue_book
        qry = "DELETE FROM ISSUE WHERE Student_name = %s"
        data = self.connect.iud(qry, (ID,))
        return data

    def return_book(self, name, book_id, book_name, return_date):  # Return_book
        qry = "INSERT INTO Book_returned(Student_name, Book_id, Book_name, Return_date) VALUES (%s,%s,%s,%s)"
        values = (name, book_id, book_name, return_date)
        self.connect.iud(qry, values)
        return True

    def return_book_update(self, name, book_id, book_name, return_date, row):  # Return_book
        qry = "UPDATE Book_returned SET Student_name = %s, Book_id= %s, Book_name = %s, Return_date = %s WHERE id=%s"
        values = (name, book_id, book_name, return_date, row)
        self.connect.iud(qry, values)
        return True

    def show_returned(self):      # Return_book
        qry = "SELECT * FROM Book_returned"
        data = self.connect.show_data(qry)
#        print(data)
        return data





#management_qry().show_returned()

