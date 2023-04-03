import sqlite3
from BD import DB_NAME
import re


class Usuario:
    TABLE_NAME = 'usuarios'

    def __init__(self):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        statement = f"""
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}(
                idUsuario integer primary key,
                nombreUsuario text,
                telefono integer,
                email text
            )
        """
        cursor.execute(statement)
        connection.commit()
        connection.close()

    def crear_usuario(self, nombre, email, telefono):
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        statement = f"""
                        INSERT INTO {self.TABLE_NAME}(nombreUsuario, telefono, email)
                        VALUES(?, ?, ?)
        """
        cursor.execute(statement, [nombre, telefono, email])
        connection.commit()
        connection.close()

    @staticmethod
    def check_email(email):
        regex = '^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]?\w*[.]\w{2,3}$'

        return re.search(regex, email) is not None

    @staticmethod
    def check_name(name):
        regex = '^[A-Za-z]{3,15}[ ]?[A-Za-z]*$'

        return re.search(regex, name) is not None

    @staticmethod
    def check_telefono(telefono):
        telefono = str(telefono)
        regex = '^[0-9]{7,8}$'
        return re.search(regex, telefono) is not None
