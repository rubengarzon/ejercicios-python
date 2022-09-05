# En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido que también será de tipo texto.
#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

# Conectamos con la base de datos
conexion = sqlite3.connect("ejercicio17.db")

# Creamos el cursor
cursor = conexion.cursor()

# Creamos la tabla
cursor.execute("CREATE TABLE IF NOT EXISTS Alumnos (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)")

# Insertamos datos
cursor.execute("INSERT INTO Alumnos VALUES (1, 'Juan', 'Perez')")
cursor.execute("INSERT INTO Alumnos VALUES (2, 'Maria', 'Gomez')")
cursor.execute("INSERT INTO Alumnos VALUES (3, 'Pedro', 'Gonzalez')")
cursor.execute("INSERT INTO Alumnos VALUES (4, 'Jose', 'Rodriguez')")
cursor.execute("INSERT INTO Alumnos VALUES (5, 'Luis', 'Fernandez')")
cursor.execute("INSERT INTO Alumnos VALUES (6, 'Ana', 'Martinez')")
cursor.execute("INSERT INTO Alumnos VALUES (7, 'Laura', 'Sanchez')")
cursor.execute("INSERT INTO Alumnos VALUES (8, 'Pablo', 'Lopez')")

# Guardamos los cambios
conexion.commit()

# buscar un alumno por nombre
cursor.execute("SELECT * FROM Alumnos WHERE nombre = 'Pablo'")
alumno = cursor.fetchone()
print(alumno)

# Cerramos la conexión
conexion.close()