# pip instal pymsql or pip install mariadb

# Module Imports
import os
import pymysql
from dotenv import load_dotenv, dotenv_values

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DATABASE = os.getenv('DATABASE')
DB_TABLE = os.getenv('DB_TABLE')

# Connect to MariaDB Platform
def connectionSQL():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DATABASE
        )
        print('\nMariaDB connected...\n')
        return conn
    except pymysql.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    # Get Cursor
    cursor = conn.cursor()
    
def add_user(iid, fname, lname, bdate):
   print('\nAdding...\n')
   
   sql_query = f"INSERT INTO {DB_TABLE} () VALUES ({iid}, '{fname}', '{lname}', '{bdate}')"
   
   conn = connectionSQL()
   
   try:
        if conn != None:
            cur = conn.cursor()
            cur.execute(sql_query)
            conn.commit()
            conn.close()
            print(cur.rowcount, "record inserted.")
        else:
            print("Error connecting to db...")
   except Exception as e: 
        print(e)