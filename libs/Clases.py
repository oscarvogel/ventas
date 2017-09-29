# coding=utf-8
from PyQt5 import QtCore

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QPushButton, QDesktopWidget, QLabel, QLineEdit, QComboBox

from db.SqlComandos import SQL


class Formulario(QDialog):

    def __init__(self, parent=None):
        QDialog.__init__(self, parent=None)
        self.setWindowModality(Qt.ApplicationModal)

    def Cerrar(self):
        self.close()

    def exec_(self):
        self.Center()
        super().exec_()

    def Center(self):
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())



class Boton(QPushButton):

    def __init__(self, parent=None, texto='', imagen=None, tamanio=None):
        super().__init__(parent)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)
        self.setText(texto)
        if imagen:
            icono = QIcon(imagen)
            self.setIcon(icono)
            if tamanio and isinstance(tamanio,QSize):
                self.setIconSize(tamanio)

class BotonCerrarFormulario(Boton):

    def __init__(self, parent=None):
        texto = '&Cerrar'
        imagen = 'imagenes\log-out.png'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)

class BotonAceptar(Boton):

    def __init__(self, parent=None, textoBoton='&Aceptar'):
        texto = textoBoton
        imagen = 'imagenes\\aceptar.bmp'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)

class Etiqueta(QLabel):

    def __init__(self, parent=None, texto='', **kwargs):
        super().__init__(parent)
        self.setText(texto)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

class EntradaTexto(QLineEdit):

    ventana = None
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ventana = parent
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

        if 'tooltip' in kwargs:
            self.setToolTip(kwargs['tooltip'])
        if 'placeholderText' in kwargs:
            self.setPlaceholderText(kwargs['placeholderText'])

class ComboSQL(QComboBox):

    lTodos = False
    cBaseDatos = 'steffenhnos'
    cSentencia = ''
    campo1 = ''
    campo2 = ''
    campovalor = ''
    condicion = ''
    tabla = ''
    cOrden = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)
        self.CargaDatos()

    def CargaDatos(self):
        cursor = SQL().BuscaTodo(tabla=self.tabla,
                                 cOrden=self.cOrden,
                                 cFiltro=self.condicion)

        for r in cursor:
            self.addItem(r[self.campo1], r[self.campovalor])

    def GetDato(self):
        return self.currentData()

