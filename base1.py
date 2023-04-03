import sqlite3
import json


class Persona:
    TABLE_NAME = "Persona"
    DB_NAME = "persona.db"

    def __init__(self):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        statement = f"""
                    CREATE TABLE IF NOT EXISTS {self.TABLE_NAME}(
                        ci integer primary key,
                        nombre text,
                        apellido text,
                        telefono text,
                        edad integer
                    )
        """
        cursor.execute(statement)
        connection.commit()
        connection.close()

    def get_all(self):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        statement = f"SELECT * FROM {self.TABLE_NAME}"
        response = cursor.execute(statement).fetchall()
        lista = [dict(x) for x in response]
        return json.dumps(lista)

    def insert_persona(self, ci, nombre, apellido, telefono, edad):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        statement = f"""
                    INSERT INTO {self.TABLE_NAME} (ci, nombre, apellido, telefono, edad) 
                    VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(statement, [ci, nombre, apellido, telefono, edad])
        connection.commit()
        connection.close()
        return True

    def obtener_por_ci(self, ci):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        statement = f"SELECT * FROM {self.TABLE_NAME} WHERE ci = {ci}"
        response = cursor.execute(statement).fetchone()
        elemento = dict(response) if response is not None else []
        return json.dumps(elemento)

    def escribirJson(self):
        connection = sqlite3.connect(self.DB_NAME)
        cursor = connection.cursor()
        cursor.row_factory = sqlite3.Row
        statement = f"SELECT * FROM {self.TABLE_NAME}"
        response = cursor.execute(statement).fetchall()
        respuesta = [dict(x) for x in response]
        file = open("tablas.json", 'w')
        json.dump(respuesta, file, skipkeys=True)
        file.close()
        connection.close()

    def limpiarTabla(self):
        if input("estas seguro de eliminar la tabla?").lower() == "si":
            connection = sqlite3.connect(self.DB_NAME)
            cursor = connection.cursor()
            statement = f"DELETE FROM {self.TABLE_NAME}"
            cursor.execute(statement)
            connection.commit()
            connection.close()


def main():
    persona = Persona()
    # persona.insert_persona(ci=12345, nombre="alberto", apellido="perez", telefono=77777, edad=27)
    # print(persona.obtener_por_ci(ci=1234567))
    persona.limpiarTabla()
    print(persona.get_all())


if __name__ == '__main__':
    main()
