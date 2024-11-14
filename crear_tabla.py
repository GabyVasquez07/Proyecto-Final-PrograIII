import sqlite3

# Conectar a la base de datos (si no existe, se crea)
conn = sqlite3.connect('recordatorios.db')
c = conn.cursor()

# Crear la tabla si no existe
c.execute('''
CREATE TABLE IF NOT EXISTS recordatorios (
    tipo_pago TEXT NOT NULL,
    correo_destino TEXT NOT NULL,
    monto REAL NOT NULL,
    fecha_vencimiento TEXT NOT NULL,
    diaDrecordatorio TEXT NOT NULL
)
''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Tabla 'recordatorios' creada correctamente.")
