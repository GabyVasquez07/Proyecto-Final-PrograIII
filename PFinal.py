import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QMessageBox,
                             QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton)
from PyQt5.QtGui import QPixmap

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

        # Añadir los labels y entradas al layout vertical
        text_layout.addWidget(self.pago)
        text_layout.addWidget(self.entrada)
        text_layout.addWidget(self.destino)
        text_layout.addWidget(self.entrada2)
        text_layout.addWidget(self.monto)
        text_layout.addWidget(self.entrada3)
        text_layout.addWidget(self.fecha)
        text_layout.addWidget(self.entrada4)

        # Crear QLabel para la imagen y cargar la imagen
        self.imagen_label = QLabel()
        pixmap = QPixmap("DodoPagos.png")  # Reemplaza con la ruta de tu imagen
        self.imagen_label.setPixmap(pixmap)

        # Redimensionar la imagen (ajusta el tamaño aquí)
        self.imagen_label.setFixedSize(200, 200)  # Cambia los valores según el tamaño deseado
        self.imagen_label.setScaledContents(True)  # Ajusta la imagen al tamaño del QLabel


        # Añadir el layout de texto y la imagen al layout horizontal
        form_layout.addLayout(text_layout)
        form_layout.addWidget(self.imagen_label)

        # Añadir el layout horizontal al layout principal
        main_layout.addLayout(form_layout)

        # Crear los botones y añadirlos al layout principal
        boton_guardar = QPushButton("Guardar recordatorio")
        boton_guardar.clicked.connect(self.mostrar_mensaje)
        self.clear_button = QPushButton("Limpiar Entradas")
        self.clear_button.clicked.connect(self.clear_inputs)
        main_layout.addWidget(boton_guardar)
        main_layout.addWidget(self.clear_button)

        # Configurar el layout principal en la ventana central
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def clear_inputs(self):
        # Limpiar el texto de todas las entradas
        self.entrada.clear()
        self.entrada2.clear()
        self.entrada3.clear()
        self.entrada4.clear()

    def mostrar_mensaje(self):
    # Aquí puedes definir el mensaje que quieres mostrar
       # Mostrar mensaje de guardado
        mensaje = QMessageBox()
        mensaje.setWindowTitle("Recordatorio Guardado")
        mensaje.setText("El recordatorio ha sido guardado exitosamente.")
        mensaje.setIcon(QMessageBox.Information)
        mensaje.exec_()

# Ejecutar la aplicación
app = QApplication(sys.argv)
ventana = VentanaPrincipal()
ventana.show()
app.exec()
