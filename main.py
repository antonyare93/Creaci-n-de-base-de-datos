import sqlite3
import pysqlite3

def main():
    with sqlite3.connect('curso.db', isolation_level=None) as conn:
        cursor = conn.cursor()
        qry_crear = """CREATE TABLE alumnos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL
            );"""
        try:
            cursor.execute(qry_crear)
        except sqlite3.OperationalError:
            pass
        indices = [1,2,3,4,5,6,7,8]
        nombres = ['Alvaro', 'Beatriz', 'Carlos', 'Daniela', 'Esteban', 'Flor', 'Gerardo', 'Hilda']
        apellidos = ['Hernandez', 'García', 'Fajardo', 'Estrada', 'Diaz', 'Carreño', 'Bolivar', 'Arias']

        for indice in indices:
            qry_insertar = f"INSERT INTO alumnos(id, nombre, apellido) VALUES({indice}, '{nombres[indice-1]}', '{apellidos[indice-1]}');"
            cursor.execute(qry_insertar)

        consultar = input('Ingrese el id del alumno a consultar: ')

        qry_consulta = f"SELECT * FROM alumnos WHERE id IN ('{consultar}');"
        print(cursor.execute(qry_consulta).fetchall())
        cursor.close()



if __name__ == '__main__':
    main()