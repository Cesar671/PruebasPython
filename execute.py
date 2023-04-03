import sqlite3


def main():
    conect = sqlite3.connect("bd1.db")
    conect.execute("""insert into prueba(descripcion, precio)
                                  values('prueba de bd', 13)""")
    conect.commit()
    conect.close()


if __name__ == '__main__':
    main()
