import unittest
from address_book import AdressBook

class AbTest(unittest.TestCase):
    def test_check_ok(self):
        abonents = {4 :  ('test', 'test', 'test', 'test', 'test')}
        self.assertTrue(AdressBook.check(self, abonents))
    
    def test_check_fail(self):
        abonents = {}
        self.assertFalse(AdressBook.check(self, abonents))
        
if __name__ == '__main__':
    unittest.main()