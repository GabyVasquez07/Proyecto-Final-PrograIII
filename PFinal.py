#Importamos las librerías necesarias :D 
import sqlite3
import datetime
import time
import correo  # Importamos el archivo donde se hizo la creación para enviar los correos :P 
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap

# Función para verificar y enviar correos automáticamente
def verificar_y_enviar():
    conn = sqlite3.connect('recordatorios.db')
    c = conn.cursor()

       # Obtener la fecha y hora actuales en el formato estándar YYYY-MM-DD HH:MM
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  # Cambiado a YYYY-MM-DD HH:MM
    print(f"Fecha y hora actual: {now}")  # Mensaje de depuración para ver la fecha actual

    # Seleccionar recordatorios que cumplan con la condición de fecha de recordatorio
    c.execute("SELECT * FROM recordatorios WHERE diaDrecordatorio <= ?", (now,))

    recordatorios = c.fetchall()

    if not recordatorios:
        print("No hay recordatorios para enviar en este momento.")
    else:
        for record in recordatorios:
            tipo_pago, correo_destino, monto, fecha_vencimiento,diaDrecordatorio = record
            print(f"Enviando correo para el recordatorio: {record}")  # Mensaje de depuración
            
            # Enviar el correo
            correo.enviar_recordatorio(tipo_pago, correo_destino, monto, fecha_vencimiento)
            
          
            

    conn.commit()
    conn.close()

# Función para ejecutar el bucle de verificación y envío
def ejecutar_bucle():
    while True:
        verificar_y_enviar()  # Verificar y enviar correos si es necesario
        time.sleep(60)  # Esperar 60 segundos antes de volver a ejecutar

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        self.setWindowTitle('Ventana de Recordatorio')

        # Crear el layout principal vertical
        main_layout = QVBoxLayout()

        # Crear un layout horizontal para etiquetas de texto y entradas
        form_layout = QHBoxLayout()

        # Crear un layout vertical para los labels y las entradas de texto
        text_layout = QVBoxLayout()
        self.pago = QLabel("Ingresa el tipo de pago:")
        self.entrada = QLineEdit()
        self.destino = QLabel("Ingresa correo electronico:")
        self.entrada2 = QLineEdit()
        self.monto = QLabel("Ingresa el monto del pago:")
        self.entrada3 = QLineEdit()
        self.fecha = QLabel("Fecha de vencimiento:") 
        self.entrada4 = QLineEdit()
        self.recordatorio = QLabel("Establecer dia y hora de recordatorio YYYY-MM-DD Y HH/MM:") 
        self.entrada5 = QLineEdit()

        # Añadir los labels y entradas al layout vertical
        text_layout.addWidget(self.pago)
        text_layout.addWidget(self.entrada)
        text_layout.addWidget(self.destino)
        text_layout.addWidget(self.entrada2)
        text_layout.addWidget(self.monto)
        text_layout.addWidget(self.entrada3)
        text_layout.addWidget(self.fecha)
        text_layout.addWidget(self.entrada4)
        text_layout.addWidget(self.recordatorio)
        text_layout.addWidget(self.entrada5)
        # Crear QLabel para la imagen y cargar la imagen
        self.imagen_label = QLabel()
        pixmap = QPixmap("DodoPagos.png")  
        self.imagen_label.setPixmap(pixmap)

        # Redimensionar la imagen
        self.imagen_label.setFixedSize(200, 200)  # Cambia los valores según el tamaño deseado
        self.imagen_label.setScaledContents(True)  # Ajusta la imagen al tamaño del QLabel


        # Añadir el layout de texto y la imagen al layout horizontal
        form_layout.addLayout(text_layout)
        form_layout.addWidget(self.imagen_label)

        # Añadir el layout horizontal al layout principal
        main_layout.addLayout(form_layout)

        # Crear los botones y añadirlos al layout principal
        boton_guardar = QPushButton("Guardar recordatorio")
        boton_guardar.clicked.connect(self.guardar_en_db)
        main_layout.addWidget(boton_guardar)

        self.clear_button = QPushButton("Limpiar Entradas")
        self.clear_button.clicked.connect(self.clear_inputs)
        main_layout.addWidget(self.clear_button)

        # Configurar el layout principal en la ventana central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Crear la tabla en la base de datos si no existe
        self.crear_tabla()

        # Iniciar el bucle en segundo plano para verificar y enviar recordatorios
        self.iniciar_bucle()

    
    def crear_tabla(self):
     conn = sqlite3.connect('recordatorios.db')  # Conectar a la base de datos
     c = conn.cursor()
     c.execute('''CREATE TABLE IF NOT EXISTS recordatorios 
                 (tipo_pago TEXT, correo_destino TEXT, monto REAL, fecha_vencimiento TEXT, diaDrecordatorio TEXT)''')
     conn.commit()
     conn.close()  # Cerrar la conexión después de ejecutar los cambios


    def guardar_en_db(self):
        # Obtener los datos de las entradas de texto
        tipo_pago = self.entrada.text()
        correo_destino = self.entrada2.text()
        monto_pago = self.entrada3.text()
        fecha_vencimiento = self.entrada4.text()
        diaDrecordatorio = self.entrada5.text()


        # Conectar con la base de datos y guardar los datos
        conn = sqlite3.connect('recordatorios.db')
        c = conn.cursor()
        c.execute("INSERT INTO recordatorios (tipo_pago, correo_destino, monto, fecha_vencimiento, diaDrecordatorio) VALUES (?, ?, ?, ?, ?) ",
                  (tipo_pago, correo_destino, monto_pago, fecha_vencimiento, diaDrecordatorio))
        conn.commit()
        conn.close()

        # Mostrar mensaje de éxito
        QMessageBox.information(self, "Guardado", "Recordatorio guardado exitosamente en la base de datos.")
        self.clear_inputs()

    def clear_inputs(self):
        # Limpiar el texto de todas las entradas
        self.entrada.clear()
        self.entrada2.clear()
        self.entrada3.clear()
        self.entrada4.clear()
        self.entrada5.clear()

    # Función para iniciar el bucle de verificación en segundo plano
    def iniciar_bucle(self):
        # Iniciar el hilo que ejecutará el bucle de verificación y envío de correos
        hilo_bucle = threading.Thread(target=ejecutar_bucle, daemon=True)
        hilo_bucle.start()

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication([])  # Crear la aplicación de Qt
    ventana = VentanaPrincipal()  # Crear la ventana principal
    ventana.show()  # Mostrar la ventana
    app.exec_()  # Ejecutar el bucle de eventos de la aplicación
