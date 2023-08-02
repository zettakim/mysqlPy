import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error


load_dotenv()
PASSWORD = os.getenv("PASSWORD")


def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='172.17.0.3',
                                       database='python_mysql',
                                       user='zetta',
                                       password=PASSWORD)
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()


if __name__ == '__main__':
    connect()
