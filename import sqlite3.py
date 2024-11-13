import sqlite3

conn = sqlite3.connect('recordatorios.db')
c = conn.cursor()

# Verificar el contenido de la tabla
c.execute("SELECT * FROM recordatorios")
recordatorios = c.fetchall()
print("Contenido de la tabla 'recordatorios':", recordatorios)

conn.close()
