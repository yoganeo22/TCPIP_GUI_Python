import sqlite3
import pandas as pd
import traceback

# use sqlitestudio to open the db
def createConnection(fileName):
    '''
        Create database connection to sqlite database
        If the file does not exist, it will create the new database
    :param filename: db filename
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        #print("Sqlite3 version: {}".format(sqlite3.version))
    except:
        print(traceback.print_exc())
    finally:
        if conn:
            # always close connection after use.
            conn.close()

def sqlQueryCommand(filename, query):
    try:
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    except:
        print(traceback.print_exc())
    finally:
        if conn:
            # always close connection after usage.
            conn.close()

def display_data(fileName, query):
    '''
        Display data using Pandas
        Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
            built on top of the Python programming language.
    :param fileName: db filename
    :param query: sql query
    :return: None
    '''
    try:
        conn = sqlite3.connect(fileName)
        c = conn.cursor()
        c.execute(query)
        df = pd.DataFrame(c.fetchall(), columns=['product_name'])
        print(df)
    except:
        print(traceback.print_exc())
    finally:
        if conn:
            # always close connection after usage.
            conn.close()


if __name__ == "__main__":
    createConnection(r"sqlfile.db")

    #sqlQueryCommand(r"sqlfile.db", '''DROP table Products''')

    #sqlQueryCommand(r"sqlfile.db", '''
    #                    CREATE TABLE IF NOT EXISTS Products ([product_id] INTEGER PRIMARY KEY,
    #                       [product_name] TEXT)
    #                    ''')
    
    # insert data
    #data = ''' (1,'Fruits'),
    #           (2,'Vegetables')
    #       '''
    #sqlQueryCommand(r"sqlfile.db", '''INSERT INTO Products (product_id, product_name) VALUES ''' + data)

    # display the results
    #display_data(r"sqlfile.db", '''
    #              SELECT
    #                a.product_name
    #                FROM Products a
    #              ''')
