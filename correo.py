import smtplib
#Importamos  la librería smtplib, sin ella, esto no sería posible 🙏
def enviar_recordatorio(tipo_pago, correo_destino, monto, fecha):
    correo = "santiago.quitof@gmail.com" # mi correo que me creé de onde se mandan los correos
    contra = "nywo wwrk vwhl ixwn" # mi contraseña generada por Google
    servi = "smtp.gmail.com" # Servidor
    puerto = 587 

    asunto = "Recordatorio de pago" # Nuestro asunto
    cuerpo = ( #Todo el diseño de lo que vamos a decir en el cuerpo del correo, tomando los datos almacenados en la ventana de PyQt5
        f"Estimado usuario,\n\n"
        f"Este es un recordatorio sobre el tipo de pago: {tipo_pago}.\n"
        f"Monto a pagar: {monto}\n"
        f"Fecha de vencimiento: {fecha}\n\n"
        f"Por favor, realice el pago antes de la fecha de vencimiento para evitar problemas.\n\n"
        f"Saludos cordiales."
    )
    mensaje = f"Subject: {asunto}\n\n{cuerpo}" #Almacenamos el asunto y cuerpo en esa variable

    try: #Manejo de Errores :D
        conex = smtplib.SMTP(servi, puerto) # Necesitamos el servidor y puerto D:
        conex.starttls() #Iniciamos la conexión
        conex.login(correo, contra) #Las credenciales
        conex.sendmail(correo, correo_destino, mensaje) #Los parámetros que se necesitan pa enviar un email
        conex.quit()#Enviamos el correo y cerramos la conexión
        print("El correo se ha enviado correctamente")

    except smtplib.SMTPResponseException as e:
        print(f"Se ha encontrado un error: {e}")
        #Si ocurre un error, lea esto por favor
