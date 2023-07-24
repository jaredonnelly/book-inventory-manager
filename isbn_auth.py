import logging as log
import isbnlib
import numpy as np
import unittest

def authenticate(isbn, debug=False):
    """Verifies that the provided isbn meets international standards as described by:
    https://en.wikipedia.org/wiki/ISBN#ISBN-13_check_digit_calculation"""

    if type(isbn) not in [int, str]:
        print("The ISBN must be a 10 or 13 digit integer or string ending in either 0-9 or X.")
        return False
    
    isbn = str(isbn)
    isbn = isbnlib.canonical(isbn)
    
    if len(isbn) == 10:
        return isbnlib.is_isbn10(isbn)
    elif len(isbn) == 13:
        return isbnlib.is_isbn13(isbn)
    else:
        print("The ISBN must be a 10 or 13 digit integer or string ending in either 0-9 or X.")
        return False
    
def cannon(isbn):
    """Returns only the allowed characters in an isbn."""
    isbn = isbnlib.canonical(isbn)

    if len(isbn) == 10:
        return isbnlib.to_isbn13(isbn)
    else:
        return isbn

class TestIsbnAuthenticate(unittest.TestCase):
    def test_authenticate(self):
        # Test when isbn is a 13 digit number
        self.assertEqual(authenticate("9780306406157"), True)
        self.assertEqual(authenticate(9780306406157), True)
        self.assertEqual(authenticate("616380323X"), True)

    def test_delimters(self):
        self.assertEqual(authenticate("978-0306-406-15-7"), True)
        self.assertEqual(authenticate("978-030640615-5"), False)
        self.assertEqual(authenticate("616380323-X"), True)
    
if __name__ == '__main__':
    unittest.main()