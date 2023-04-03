import sqlite3
from BD import DB_NAME
import pytest
from usuario import Usuario


@pytest.fixture()
def iniciar_base_de_datos():
    global cursor
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.row_factory = sqlite3.Row

    yield

    connection.commit()
    connection.close()


@pytest.mark.parametrize(
    "nombre, email, telefono", [
        ('carlos', 'carlos@gmail.com', 7767777),
        ('roberto', 'roberto@gmail.com', 6783456),
        ('juan', 'juan@gmail.com', 8760982)
    ]
)
def test_crear_usuario(nombre, email, telefono, iniciar_base_de_datos):
    usuario = Usuario()
    usuario.crear_usuario(nombre=nombre, email=email, telefono=telefono)
    statement = f"SELECT * FROM {usuario.TABLE_NAME} WHERE nombreUsuario = '{nombre}'"
    response = dict(cursor.execute(statement).fetchone())
    cursor.execute(f"DELETE FROM {Usuario.TABLE_NAME} WHERE nombreUsuario = '{nombre}'")
    assert response['nombreUsuario'] == nombre


@pytest.mark.parametrize(
    "email, expected", [
        ("roberto@gmail.com", True),
        ("rodrigo@yasddas.com", True),
        ("roasdadasdad.com", False),
        ("asdasdasd@asdad", False),
        ("@asdad.com", False),
        (".com", False),
        ("RodrigoFuentes@gmail.com", True),
        ("12345678@umss.edu.com", True)
    ]
)
def test_check_email(email, expected):
    response = Usuario.check_email(email)
    assert response == expected

@pytest.mark.parametrize(
    "nombre, expected", [
        ("roberto", True),
        ("", False),
        ("aa", False),
        ("1a", False),
        ("roberto1", False),
        ("Roberto sanchez1", False),
        ("+çRoberto", False),
        ("Roberto Sanchez", True),
        ("123", False)
    ]
)
def test_check_name(nombre, expected):
    response = Usuario.check_name(nombre)
    assert response == expected

@pytest.mark.parametrize(
    "telefono, expected",[
        (12345678, True),
        (123345, False),
        (123454567, False),
        ("asd1234", False),
        ("- 123 as", False),
        (1234567, True)
    ]
)
def test_check_telf(telefono, expected):
    response = Usuario.check_telefono(telefono)
    assert response == expected