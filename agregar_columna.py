import sqlite3

# Eliminar la tabla y crearla nuevamente con la columna
def recrear_tabla():
    conn = sqlite3.connect('recordatorios.db')
    c = conn.cursor()
    
    # Eliminar la tabla si existe
    c.execute("DROP TABLE IF EXISTS recordatorios")
    
    # Crear la tabla nuevamente con la columna faltante
    c.execute('''CREATE TABLE recordatorios (
                     tipo_pago TEXT NOT NULL,
                     correo_destino TEXT NOT NULL,
                     monto REAL NOT NULL,
                     fecha_vencimiento TEXT NOT NULL,
                     diaDrecordatorio TEXT NOT NULL
                 )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    recrear_tabla()

