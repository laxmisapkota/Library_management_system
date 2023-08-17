import unittest
from library_management.library_qry import *
from library_management.user_qry import *

class unit_testing(unittest.TestCase):
    mgt= management_qry()
    user= Staff()

    def test_add_book(self):
        result=self.mgt.add_book('#111','Eleven minutes','romance','Paulo Coelho','56')
        self.assertTrue(result)

    def test_update_book(self):
        result=self.mgt.update_book('#Tcmt8','The Alchemist','fiction','Paulo Coelho','14','#Tcmt8')
        self.assertTrue(result)

    def test_delete_book_management(self):
        actual_result = self.mgt.search('Eleven minutes')
        id=actual_result[0][0]
        self.assertTrue(self.mgt.delete_from_book_management(id))

    def test_issue_book(self):
        actual_result = self.mgt.search('harry potter')
        id=actual_result[0][0]
        result=self.mgt.issue_book('Ram',id,'2020/8/9','2021/01/9')
        self.assertTrue(result)

    def test_search_book(self):
        actual_result=self.mgt.search('harry potter')
        expected_result=[('#hrpt9','harry potter','friction','jk','23')]
        self.assertEqual(expected_result,actual_result)

    def test_register(self):
        result=self.user.register('Alu','student','alisha','Adhikari','2000/8/9','putalisadak','4','4522125','alisha@adhikari','female','married')
        self.assertTrue(result)



















