import sqlite3
import json


def main():
    conect = sqlite3.connect('bd1.db')
    cursor = conect.cursor()
    cursor.row_factory = sqlite3.Row
    response = cursor.execute("Select * from prueba")
    filas = response.fetchall()
    conect.close()
    json_string = json.dumps([dict(x) for x in filas])

    str = ['uno', 'dos' , 'tres']

    print([res for res in str])

if __name__ == '__main__':
    main()