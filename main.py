import sqlite3


def main():
    conection = sqlite3.connect("bd1.db")
    try:
        conection.execute("""
                            create table prueba(
                               codigo integer primary key,
                               descripcion text,
                               precio real
                            )      
                        """)
        print('se creo la tabla')
    except sqlite3.OperationalError:
        print('ya existe la tabla')
    conection.close()


if __name__ == '__main__':
    main()