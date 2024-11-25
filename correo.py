import smtplib
#Importamos  la librería smtplib, sin ella, esto no sería posible 🙏
# Función que envía el recordatorio, sin el parámetro 'diaDrecordatorio'
def enviar_recordatorio(tipo_pago, correo_destino, monto, fecha):
    correo = "santiago.quitof@gmail.com"  # Tu correo
    contra = "nywo wwrk vwhl ixwn"  # Contraseña generada por Google
    servi = "smtp.gmail.com"  # Servidor de Gmail
    puerto = 587  # Puerto de Gmail

    asunto = "Recordatorio de pago pendiente"  # Asunto del correo

    # Cuerpo del mensaje con formato HTML
    cuerpo = (
        f"<html>"
        f"<body>"
        f"<p>Estimado/a <strong>{correo_destino}</strong>,</p>"
        f"<p>Le recordamos que tiene un pago pendiente del siguiente tipo: <strong>{tipo_pago}</strong>.</p>"
        f"<p>El monto a pagar es: <strong>${monto}</strong>.</p>"
        f"<p>La fecha de vencimiento para realizar el pago es: <strong>{fecha}</strong>.</p>"
        f"<p>Le solicitamos amablemente que efectue el pago antes de la fecha indicada para evitar posibles inconvenientes.</p>"
        f"<p>Si ya ha realizado el pago, por favor ignore este mensaje.</p>"
        f"<br>"
        f"<p>Saludos cordiales,</p>"
        f"<p><strong>El equipo de DodoPagos</strong></p>"
        f"</body>"
        f"</html>"
)
    mensaje = f"Subject: {asunto}\nContent-Type: text/html; charset=UTF-8\n\n{cuerpo}"  # Asunto y cuerpo del mensaje con formato HTML

    try:
        conex = smtplib.SMTP(servi, puerto)
        conex.starttls()
        conex.login(correo, contra)
        conex.sendmail(correo, correo_destino, mensaje.encode('utf-8'))  # Enviar correo
        conex.quit()
        print("El correo se ha enviado correctamente")

    except smtplib.SMTPResponseException as e:
        print(f"Se ha encontrado un error: {e}")
