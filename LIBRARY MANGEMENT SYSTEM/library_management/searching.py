# # linear search
# def linear_search(list, key):
#     for i in range(len(list)):
#         if list[i] == key:
#             return i
#     return -1
# # time complexity = O(n)
#
# # binary search
def binary_search_iterative(list, key):
    start = 0
    end = len(list) - 1
    while start <= end:
        mid = (start + end) // 2
        if list[mid][0] == key:
            return mid
        elif list[mid][0] > key:
            end = mid - 1
        else:
            start = mid + 1
    return -1

# def binary_search_recursive(list, key, start, end):
#     if start <= end:
#         mid = (start + end) // 2
#         if list[mid] == key:
#             return mid
#         elif list[mid] > key:
#             return binary_search_recursive(list, key, start, mid-1)
#         else:
#             return binary_search_recursive(list, key, mid+1, end)

# time complexity = O(log(n))
# n/2, (n/2)/2 = n/4 , n/4/2 = n/8, n/8/2 = n/16
# 1 = n/16
# n = 16
# n = 2^k
# k = log(n)

# students = [2, 5, 7, 8, 12, 15, 18]  # 18
# students = ['abishek', 'anand', 'astha', 'bibek', 'binayak', 'diptan', 'diwas', 'gamvirta']
# result = binary_search_iterative(students, 'sujit')
# if result < 0:
#     print("Given key is not in the list")
# else:
#     print("Given key is at index: ", result)




def login(self, username, password):
    qry = "SELECT * FROM user_details WHERE Username = %s and Password = %s"
    values = (username, password)
    user = self.db.show_data_p(qry, values)
    return user

def login():
    my_data = []
    for i in data:
        my_data.append(i[0])
    print(binary_search_iterative(data, 'Username'))
    user = self.db.show_data_p(qry, values)
login()


def register(self, Username, Password, First_name, last_name, Date_of_Birth, City, Province, Number, Email, Gender,
             Marital):
    qry = "INSERT INTO user_details(Username, Password, First_name, last_name, Date_of_Birth, City,Province, Number,Email,Gender, Marital) VALUES(%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
    values = (Username, Password, First_name, last_name, Date_of_Birth, City, Province, Number, Email, Gender, Marital)
    self.db.iud(qry, values)
    return True
