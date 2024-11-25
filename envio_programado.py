import sqlite3
import datetime
import time
import correo  

def verificar_y_enviar():
    conn = sqlite3.connect('recordatorios.db')
    c = conn.cursor()

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"Fecha y hora actual: {now}")

    # Seleccionar recordatorios que no han sido enviados
    c.execute("SELECT * FROM recordatorios WHERE diaDrecordatorio <= ? AND enviado = 0", (now,))
    recordatorios = c.fetchall()

    if not recordatorios:
        print("No hay recordatorios para enviar en este momento.")
    else:
        for record in recordatorios:
            tipo_pago, correo_destino, monto, fecha_vencimiento, diaDrecordatorio, _ = record
            correo.enviar_recordatorio(tipo_pago, correo_destino, monto, fecha_vencimiento)

            # Marcar el recordatorio como enviado
            c.execute("UPDATE recordatorios SET enviado = 1 WHERE tipo_pago = ? AND correo_destino = ?", (tipo_pago, correo_destino))

    conn.commit()
    conn.close()

  


# Ejecutar esta función cada 60 segundos (1 minuto) en un bucle infinito
while True:
    verificar_y_enviar()  # Verificar y enviar correos si es necesario
    time.sleep(60)  # Esperar 60 segundos antes de volver a ejecutar


