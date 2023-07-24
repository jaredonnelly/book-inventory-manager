import unittest

def display():
    """"Prints menu and gets option from user."""
    print("")
    print("a - add book to inventory.")
    print("r - remove book from inventory.")
    print("s - search for a book in your inventory.")
    print("l - list all books available.")
    print("q - quit. Exit the program.\n")

    return input("Enter an option: ")

def request_validation(option):
    """Validates option that was inputed by user"""

    if type(option) != str or len(option) != 1:
        print("Invalid input. Inputs must be a single character a, r, s, l, or q.\n")
        return "w"
    
    match option.lower():
        case "a":
            return "a"
        case "r":
            return "r"
        case "s":
            return "s"
        case "l":
            return "l"
        case "q":
            print("Thank you for using our book manager. Come again soon!\n")
            return "q"
        case _:
            print("Invalid input. Inputs must be a single character a, r, s, or l.\n")
            return "w"

class TestRequestValidation(unittest.TestCase):
    def test_valid_lowercase(self):
        self.assertEqual(request_validation('a'), 'a')
        self.assertEqual(request_validation('r'), 'r')
        self.assertEqual(request_validation('s'), 's')
        self.assertEqual(request_validation('l'), 'l')
        self.assertEqual(request_validation('q'), 'q')

    def test_valid_uppercase(self):
        self.assertEqual(request_validation('A'), 'a')
        self.assertEqual(request_validation('R'), 'r')
        self.assertEqual(request_validation('S'), 's')
        self.assertEqual(request_validation('L'), 'l')
        self.assertEqual(request_validation('Q'), 'q')

    def test_invalid(self):
        self.assertEqual(request_validation(123), 'w')
        self.assertEqual(request_validation(''), 'w')
        self.assertEqual(request_validation([1,'a']), 'w')
        self.assertEqual(request_validation('ar'), 'w')
        self.assertEqual(request_validation('w'), 'w')


if __name__ == '__main__':
    unittest.main()