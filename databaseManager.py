import sqlite3
import logging as log
import pandas as pd
import inventory

def setup(dbname, fname):
    """Ensures a database exists with the mock data
    returns the db connection and db cursor."""

    dbconn = sqlite3.connect(dbname)
    dbcur = dbconn.cursor()
    log.info('Database opened successfully.')

    if checkTableExists(dbconn, 'books'):
        log.info('The table, books, already exists.')
        return dbconn, dbcur
    else:
        createBookTable(dbconn)
        log.info('The table, books, was created.')
        load_database(fname, dbconn)
        log.info('System has finished loading data.')
        return dbconn, dbcur

def checkTableExists(dbconn, tablename):
    """returns whether or not a table exists"""
    dbcur = dbconn.cursor()

    dbcur.execute("""SELECT COUNT(*) 
        FROM sqlite_master 
        WHERE type ='table' 
        AND name = '{0}';
        """.format(tablename.replace('\'', '\'\'')))

    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        log.info('%s table exists!', tablename)
        return True

    dbcur.close()
    log.info('%s table does not exist.', tablename)
    return False

def load_database(filepath, dbconn):
    data = pd.read_csv(filepath)
    df = pd.DataFrame(data)

    for row in df.itertuples():
        inventory.addBook_to_database(dbconn, row.isbn, row.title, row.author, row.publisher, row.year, row.stock)

def createBookTable(dbcon, tablename="books"):
    dbcon.execute('''CREATE TABLE {0}
    (isbn INT PRIMARY KEY UNIQUE,
    title CHAR(50),
    author CHAR(50),
    publisher CHAR(50),
    year INT,
    stock INT);'''.format(tablename.replace('\'', '\'\'')))

    log.info("Table created successfully")