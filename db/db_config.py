import mysql.connector
from mysql.connector import Error

def get_connection():
    return (mysql.connector.connection(
    host="localhost",
    user="root",
    password="devanshsrm@2027",
    database="student_db"
    ))

    
    
    
