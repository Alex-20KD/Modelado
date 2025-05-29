# db.py
import psycopg2

def conectar():
    return psycopg2.connect(
        dbname="RegistroRol",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
