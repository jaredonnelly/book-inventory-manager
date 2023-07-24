import pandas as pd

def menu(conn, cur):
    searching = 's'
    while searching.lower() != 'b':
        print("\nSelect your search method.")
        print("i - search by isbn.")
        print("t - search by title.")
        print("a - search by author.")
        print("b - back. I do not want to search.")
        searching = input("\nEnter an search option: ")

        if type(searching) != str or len(searching) != 1:
            print("\nPlease enter a valid option from the list below.\n")
            continue

        search_term = str(input("Please enter your search term: "))

        match searching:
            case "i":
                by_isbn(conn, cur, search_term)
                searching = 'b'
            case "t":
                by_title(conn, cur, search_term)
                searching = 'b'
            case "a":
                by_author(conn, cur, search_term)
                searching = 'b'
            case "b":
                continue
            case _:
                print("\nPlease enter a valid option from the list below.\n")
                continue

def by_isbn(dbconn, dbcur, isbn):
    pd.set_option('display.max_rows', None)
    sql = "SELECT * FROM books WHERE isbn = '{}'".format(isbn)
    df = pd.read_sql_query(sql, dbconn)
    print("Books with a matching isbn.\n", df)

def by_title(dbconn, dbcur, title):
    pd.set_option('display.max_rows', None)
    sql = "SELECT * FROM books WHERE title = '{}'".format(title)
    df = pd.read_sql_query(sql, dbconn)
    print("Books with a matching title.\n", df)

def by_author(dbconn, dbcur, author):
    pd.set_option('display.max_rows', None)
    sql = "SELECT * FROM books WHERE author = '{}'".format(author)
    df = pd.read_sql_query(sql, dbconn)
    print("Books with a matching author.\n", df)