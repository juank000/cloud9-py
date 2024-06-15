# pip instal pymsql or pip install mariadb

# Module Imports
import os
import pymysql
from dotenv import load_dotenv, dotenv_values

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')

# Connect to MariaDB Platform
def connectionSQL():
    try:
        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS
        )
        print('\nMariaDB connected...\n')
    except pymysql.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
    # Get Cursor
    cursor = conn.cursor()