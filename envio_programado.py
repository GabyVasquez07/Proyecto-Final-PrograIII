import sqlite3
import datetime
import time
import correo  

def verificar_y_enviar():
    conn = sqlite3.connect('recordatorios.db')
    c = conn.cursor()

    # Obtener la fecha y hora actuales en el formato YYYY-MM-DD HH:MM
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Fecha y hora actual: {now}")  # Mensaje de depuración para ver la fecha actual

    # Seleccionar recordatorios que cumplan con la condición de fecha de vencimiento
    c.execute("SELECT * FROM recordatorios WHERE diaDrecordatorio <= ?", (now,))
    recordatorios = c.fetchall()

    if not recordatorios:
        print("No hay recordatorios para enviar en este momento.")
    else:
        for record in recordatorios:
         tipo_pago, correo_destino, monto, fecha_vencimiento, diaDrecordatorio = record

            # Enviar el correo
        correo.enviar_recordatorio(tipo_pago, correo_destino, monto, fecha_vencimiento,diaDrecordatorio)

    conn.close()

# Ejecutar esta función cada 60 segundos (1 minuto) en un bucle infinito
while True:
    verificar_y_enviar()  # Verificar y enviar correos si es necesario
    time.sleep(60)  # Esperar 60 segundos antes de volver a ejecutar

