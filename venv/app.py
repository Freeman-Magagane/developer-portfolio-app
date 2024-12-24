
from flask import Flask
import cx_Oracle
import secrets
import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()

secret_key = secrets.token_hex(32)
print(secret_key)
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)


oracle_host = os.getenv("ORACLE_HOST")
oracle_port = os.getenv("ORACLE_PORT")
oracle_service_name = os.getenv("ORACLE_SERVICE_NAME")
USERNAME = os.get('USERNAME')
PASSWORD = os.get('PASSWORD')

try:
    # Establish connection
    connection = cx_Oracle.connect(user=USERNAME, password=PASSWORD, dsn=oracle_port)
    print("Connected to Oracle Database")

    # Execute a query
    cursor = connection.cursor()
    cursor.execute("SELECT * employers")
    for row in cursor:
        print(row)

except cx_Oracle.DatabaseError as e:
    print("Error:", e)

finally:
    if 'connection' in locals():
        connection.close()
        print("Connection closed")


def login_manager():
 return None


def db():
 return None


def bcrypt():
 return None


def f():
    return None