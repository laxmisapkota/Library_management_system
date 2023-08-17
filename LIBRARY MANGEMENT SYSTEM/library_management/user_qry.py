# users - properties/attributes(variables) and behaviour/features(methods)
from library_management.connection import MyDb


class Staff:
    def __init__(self):
        # self._username = un
        # self._password = pw
        self.db = MyDb()

    def set_un(self, un):
        # if not un.isalphnum():
        #     return False
        self._username = un

    def get_un(self):
        return self._username

    def set_pw(self, pw):
        self._password = pw

    def get_pw(self):
        return self._password

    def login(self, username, password):
        qry = "SELECT * FROM user_details WHERE Username = %s and Password = %s"
        values = (username, password)
        user = self.db.show_data_p(qry, values)
        return user

    def register(self, Username, Password, First_name, last_name, Date_of_Birth, City, Province, Number, Email, Gender, Marital):
        qry = "INSERT INTO user_details(Username, Password, First_name, last_name, Date_of_Birth, City,Province, Number,Email,Gender, Marital) VALUES(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
        values = (Username, Password, First_name, last_name, Date_of_Birth, City, Province, Number, Email, Gender, Marital)
        self.db.iud(qry, values)
        return True
