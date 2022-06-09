import unittest

from helper import monthNumber
from helper import translate
from helper import correcter
from helper import ordinal

class testMonthNumber(unittest.TestCase):
    def test_number_string(self):
        data = "1"
        result = monthNumber(data)
        self.assertEqual(result, "January")
    def test_number_int(self):
        data = 1
        result = monthNumber(data)
        self.assertEqual(result, "January")
    def test_number_float(self):
        data = 1.0
        result = monthNumber(data)
        self.assertEqual(result, "January")
    def test_number_list(self):
        data = [1]
        result = monthNumber(data)
        self.assertEqual(result, "January")
    def test_number_tuple(self):
        data = (1,)
        result = monthNumber(data)
        self.assertEqual(result, "January")

if __name__ == "__main__":
    unittest.main()