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

def display_list():
    ref = correct_characters()
    count = 'w'
    while count == 'w':
        print("\nWould you like to view all books or just the select few?")
        print("a - print all books")
        print("c - print selection of books\n")
        count = option_validation(input("Enter an option: "), [ref.list_func, ref.list_func_menu])

    if count == 'c':
        count = 'w'
        while count == 'w':
            count = int_validation(str(input("Enter amount: ")))

    sortby = 'w'
    while sortby == 'w':    
        print("\nSelect how you would like to sort the list and then enter how many you'd like to see.")
        print("i - sort by isbn.")
        print("t - sort by title.")
        print("a - sort by authors name.")
        print("p - sort by publishers name.")
        print("d - sort by publication date (year).")
        print("s - stock, the amount of books in inventory.\n")
        sortby = option_validation(input("Enter an option: "), [ref.list_c, ref.list_c_menu])

    match sortby:
        case 'i':
            sortby = "ISBN"
        case 't':
            sortby = "TITLE"
        case 'a':
            sortby = "AUTHOR"
        case 'p':
            sortby = "PUBLISHER"
        case 'd':
            sortby = "YEAR"
        case 's':
            sortby = "STOCK"

    return sortby, count

def option_validation(option, menu):
    """Validates option that was inputed by user"""

    if type(option) != str or len(option) != 1 or not option.isalpha():
        print("Invalid input. Inputs must be a single alphabetical character: ", menu[1], "\n")
        return "w"
    
    if option.lower() in menu[0]:
        return option.lower()
    else:
        print("Invalid input. Please select an option from the menu below.")
        return "w" # w is a reserved character and stands for 'wrong'.

def int_validation(input_int):
    """returns a validated int or false"""
    if input_int.isnumeric():
        return int(input_int)
    else:
        print("The number inputted must be a positive, whole, integer.")
        return 'w'

class correct_characters():
    main = ['a', 'r', 's', 'l', 'q']
    main_menu = "a, r, s, l, and q."

    list_func = ['a', 'c']
    list_func_menu = "a or c."

    list_c = ['i', 't', 'a', 'p', 'd', 's']
    list_c_menu = ['i, t, a, p, d, or s.']


class TestRequestValidation(unittest.TestCase):
    def test_valid_lowercase(self):
        self.assertEqual(option_validation('a'), 'a')
        self.assertEqual(option_validation('r'), 'r')
        self.assertEqual(option_validation('s'), 's')
        self.assertEqual(option_validation('l'), 'l')
        self.assertEqual(option_validation('q'), 'q')

    def test_valid_uppercase(self):
        self.assertEqual(option_validation('A'), 'a')
        self.assertEqual(option_validation('R'), 'r')
        self.assertEqual(option_validation('S'), 's')
        self.assertEqual(option_validation('L'), 'l')
        self.assertEqual(option_validation('Q'), 'q')

    def test_invalid(self):
        self.assertEqual(option_validation(123), 'w')
        self.assertEqual(option_validation(''), 'w')
        self.assertEqual(option_validation([1,'a']), 'w')
        self.assertEqual(option_validation('ar'), 'w')
        self.assertEqual(option_validation('w'), 'w')


if __name__ == '__main__':
    unittest.main()
