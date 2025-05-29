import psycopg2
from psycopg2 import pool

class ConexionBD:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__pool = psycopg2.pool.SimpleConnectionPool(
                1, 10,  # min y max conexiones
                user="tu_usuario",
                password="tu_password",
                host="localhost",
                port="5432",
                database="tu_basededatos"
            )
        return cls.__instance

    def obtener_conexion(self):
        return self.__pool.getconn()

    def liberar_conexion(self, conexion):
        self.__pool.putconn(conexion)

    def cerrar_todas(self):
        self.__pool.closeall()