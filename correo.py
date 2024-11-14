import smtplib
#Importamos  la librería smtplib, sin ella, esto no sería posible 🙏
# Función que envía el recordatorio, sin el parámetro 'diaDrecordatorio'
def enviar_recordatorio(tipo_pago, correo_destino, monto, fecha):
    correo = "santiago.quitof@gmail.com"  # Tu correo
    contra = "nywo wwrk vwhl ixwn"  # Contraseña generada por Google
    servi = "smtp.gmail.com"  # Servidor de Gmail
    puerto = 587  # Puerto de Gmail

    asunto = "Recordatorio de pago"  # Asunto del correo

    # Cuerpo del mensaje
    cuerpo = (
        f"Estimado usuario,\n\n"
        f"Este es un recordatorio sobre el tipo de pago: {tipo_pago}.\n"
        f"Monto a pagar: {monto}\n"
        f"Fecha de vencimiento: {fecha}\n\n"
        f"Por favor, realice el pago antes de la fecha de vencimiento para evitar problemas.\n\n"
        f"Saludos cordiales."
    )
    mensaje = f"Subject: {asunto}\n\n{cuerpo}"  # Asunto y cuerpo del mensaje

    try:
        conex = smtplib.SMTP(servi, puerto)
        conex.starttls()
        conex.login(correo, contra)
        conex.sendmail(correo, correo_destino, mensaje)  # Enviar correo
        conex.quit()
        print("El correo se ha enviado correctamente")

    except smtplib.SMTPResponseException as e:
        print(f"Se ha encontrado un error: {e}")
