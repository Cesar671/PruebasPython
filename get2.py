import sqlite3
import json


def main():
    conection = sqlite3.connect('bd1.db')
    cursor = conection.cursor()
    statement = "select * from prueba"
    cursor.row_factory = sqlite3.Row

    statement2 = "insert into prueba (descripcion, precio) values (?, ?)"
    values = [("dato 1", 1),
              ("dato 2", 2),
              ("dato 3", 3),
              ("dato 4", 4)]
    cursor.executemany(statement2, values)
    response = cursor.execute(statement).fetchall()

    json_string = json.dumps([dict(i) for i in response])

    print(json_string)


if __name__ == '__main__':
    main()
