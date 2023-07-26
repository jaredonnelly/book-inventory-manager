from menu import option_validation, correct_characters
import logging as log
import sqlite3
import databaseManager
import inventory
import search
import menu

log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

def main():
    running = True
    ref = correct_characters()
    conn, cur = databaseManager.setup('bookManager.db', 'MOCK_DATA.csv')

    print("Welcome to your book inventory manager!\n")
    print("To begin, please select an option below.")

    while running:
        
        option = menu.display()
        option = option_validation(option, [ref.main, ref.main_menu])

        match option:
            case "a":
                inventory.user_add(conn)
            case "r":
                inventory.user_remove(conn, cur)
            case "s":
                search.menu(conn, cur)
            case "l":
                sortby, count = menu.display_list()
                inventory.list_books(conn, sortby, count)
            case "q":
                running = False
                break
            case "w":
                continue

    conn.close()

main()
