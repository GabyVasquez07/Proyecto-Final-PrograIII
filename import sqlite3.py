import sqlite3

conn = sqlite3.connect('recordatorios.db')
c = conn.cursor()

# Verificar el contenido de la tabla (debe estar vacío después de la eliminación)
c.execute("SELECT * FROM recordatorios")
recordatorios = c.fetchall()
print("Contenido de la tabla 'recordatorios':", recordatorios)

conn.commit()  # Asegúrate de guardar los cambios
conn.close()   # Cerrar la conexión

