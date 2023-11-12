import sqlite3
import pandas as pd
import traceback

# use sqlitestudio to open the db
class db:
    def createConnection(fileName):
        '''
            Create database connection to sqlite database
            If the file does not exist, it will create the new database
        :param filename: db filename
        :return: None
        '''
        try:
            conn = sqlite3.connect(fileName)
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
            result = c.fetchone()
            conn.commit()
            if result == None:
                return 0
            else:
                return result
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
            #df = pd.DataFrame(c.fetchall(), columns=['product_name'])
            df = pd.DataFrame(c.fetchall())
            #print(df)
        except:
            print(traceback.print_exc())
        finally:
            if conn:
                # always close connection after usage.
                conn.close()
