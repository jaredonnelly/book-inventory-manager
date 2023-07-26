import unittest
import sqlite3
import isbn_auth
import pandas as pd
import logging as log

class IsbnValueError(Exception):
    pass

def list_books(dbconn, sortby, count):
    """Lists all books in the database."""
    df = pd.read_sql_query("SELECT * FROM books;", dbconn)
    if sortby != 'w':
        df = df.sort_values(by=sortby)
    
    if type(count) == str:
        pd.set_option('display.max_rows', None)
        print("List of books in inventory\n", df)
    else:
        pd.set_option('display.max_rows', count)
        print("List of books in inventory\n", df.head(count))
    

def addBook_to_database(dbcon, isbn, title, author, publisher, year, stock=0, tablename="books", isbn_checksum=False):
    """Adds a book to the books table in the bookManager database"""
    try:
        if isbn_checksum:
            if not isbn_auth.authenticate(isbn):
                log.error("Invalid ISBN: %s", str(isbn))
                return 1
            isbn = isbn_auth.cannon(isbn)

        insert_param = """INSERT OR IGNORE INTO books
            (isbn, title, author, publisher, year, stock)
            VALUES (?, ?, ?, ?, ?, ?);"""
        
        data_tuple = (isbn, title, author, publisher, year, stock)
        
        dbcur = dbcon.cursor()
        dbcur.execute(insert_param, data_tuple)
        dbcon.commit()
        log.info("Book added to table under isbn: %s", str(isbn))
        
        dbcur.close()
    
    except sqlite3.Error as error:
        log.critical("Failed to insert book into sqlite table", error)
        return 1

    except IsbnValueError:
        return 1
    
    else:
        return 0
        
def user_add(dbconn):
    """Collects user input for adding a book to the database"""
    print("""To add a book to the database you will need the book's isbn. You will also be able to input the title, author's name, publisher, year published, and the number of copies you have.""")
    print("The ISBN is a 10 or 13 digit long code ending in either 0-9 or X. You may include hyphens.")
    isbn = str(input("Enter the book's ISBN: "))
    title = str(input("Enter the title of the book: "))
    author = str(input("Enter the name of the author: "))
    publisher = str(input("Enter the name of the publisher: "))
    year = int(input("Enter the year: "))
    stock = int(input("Enter how many you have: "))
    addBook_to_database(dbconn, isbn, title, author, publisher, year, stock)

def user_remove(dbconn, dbcur):
    """Collects user input for the book to be deleted."""
    print("\nTo remove a book from the database you will need to provide the book's isbn.")
    print("The ISBN is a 10 or 13 digit long code ending in either 0-9 or X. You may include hyphens.")
    isbn = str(input("Enter the book's ISBN: "))

    remove_sql = "DELETE FROM books WHERE isbn = (?)"
    dbcur.execute(remove_sql, (isbn,))    
    dbconn.commit()
    
    print("Book removed from database. ISBN: ", isbn)
