# coding=utf-8
import datetime

from PyQt5 import QtCore

from PyQt5.QtCore import QSize, Qt, QRegExp
from PyQt5.QtGui import QFont, QIcon, QRegExpValidator
from PyQt5.QtWidgets import QDialog, QPushButton, QDesktopWidget, QLabel, QLineEdit, QComboBox, QDateEdit, QTableView, \
    QTableWidget, QTableWidgetItem, QSpinBox, QDoubleSpinBox, QCheckBox, QTabWidget, QCompleter

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
        if not texto.startswith("&"):
            texto = "&" + texto

        self.setText(texto)
        if imagen:
            icono = QIcon(imagen)
            self.setIcon(icono)
            if tamanio and isinstance(tamanio,QSize):
                self.setIconSize(tamanio)


class BotonNuevo(Boton):

    def __init__(self, parent=None, textoBoton='&Nuevo'):
        texto = textoBoton
        imagen = 'imagenes\\nuevo.png'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)


class BotonCerrarFormulario(Boton):

    def __init__(self, parent=None):
        texto = '&Cerrar'
        imagen = 'imagenes\log-out.png'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)
        self.setDefault(False)


class BotonAceptar(Boton):

    def __init__(self, parent=None, textoBoton='&Aceptar'):
        texto = textoBoton
        imagen = 'imagenes\\aceptar.bmp'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)


class BotonGrabar(Boton):

    def __init__(self, parent=None, textoBoton='&Grabar'):
        texto = textoBoton
        imagen = 'imagenes\\guardar.png'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)

class BotonBorrar(Boton):

    def __init__(self, parent=None, textoBoton='&Grabar'):
        texto = textoBoton
        imagen = 'imagenes\\borrar.bmp'
        tamanio = QSize(32,32)
        super().__init__(parent, texto, imagen, tamanio)


class Etiqueta(QLabel):

    def __init__(self, parent=None, texto='', **kwargs):
        super().__init__(parent)
        self.setText(texto)
        font = QFont()
        if 'tamanio' in kwargs:
            font.setPointSizeF(kwargs['tamanio'])
        else:
            font.setPointSizeF(12)

        if 'alineacion' in kwargs:
            if kwargs['alineacion'].upper() == 'DERECHA':
                self.setAlignment(QtCore.Qt.AlignRight)
            elif kwargs['alineacion'].upper() == 'IZQUIERDA':
                self.setAlignment(QtCore.Qt.AlignLeft)
            elif kwargs['alineacion'].upper() == 'CENTRO':
                self.setAlignment(QtCore.Qt.AlignCenter)

        self.setFont(font)

class EtiquetaRoja(Etiqueta):

    def __init__(self, parent=None, texto='', **kwargs):
        super().__init__(parent, texto, **kwargs)
        self.setStyleSheet('color:red')

class EntradaTexto(QLineEdit):

    ventana = None
    proximoWidget = None

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        self.ventana = parent
        font = QFont()
        if 'tamanio' in kwargs:
            font.setPointSizeF(kwargs['tamanio'])
        else:
            font.setPointSizeF(12)
        self.setFont(font)

        if 'tooltip' in kwargs:
            self.setToolTip(kwargs['tooltip'])
        if 'placeholderText' in kwargs:
            self.setPlaceholderText(kwargs['placeholderText'])

        if 'alineacion' in kwargs:
            if kwargs['alineacion'].upper() == 'DERECHA':
                self.setAlignment(QtCore.Qt.AlignRight)
            elif kwargs['alineacion'].upper() == 'IZQUIERDA':
                self.setAlignment(QtCore.Qt.AlignLeft)

        if 'enabled' in kwargs:
            self.setEnabled(kwargs['enabled'])

        if 'inputmask' in kwargs:
            regex = QRegExp(kwargs['inputmask'])
            validator = QRegExpValidator(regex)
            self.setValidator(validator)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            if self.proximoWidget:
                self.proximoWidget.setFocus()
        QLineEdit.keyPressEvent(self, event)

    def returnPressed(self):
        if self.proximoWidget:
            self.proximoWidget.setFocus()
        else:
            self.focusNextChild()


class ComboSQL(QComboBox):

    lTodos = False
    cBaseDatos = ''
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

class Fecha(QDateEdit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

    def setFecha(self, fecha=datetime.datetime.today()):
        self.setDate(fecha)


class Grilla(QTableWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

    def ArmaCabeceras(self, cabeceras=None):

        if cabeceras:
            self.setColumnCount(len(cabeceras))

            for col in range(0, len(cabeceras)):
                self.setHorizontalHeaderItem(col, QTableWidgetItem(cabeceras[col]))

        self.resizeRowsToContents()
        self.resizeColumnsToContents()

class Spinner(QDoubleSpinBox):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)

class CheckBox(QCheckBox):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

class Paginas(QTabWidget):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)


class Autocompletar(EntradaTexto):

    completion_items = []

    def __init__(self, parent=None, *args, **kwargs):
        EntradaTexto.__init__(self, parent)
        completer = QCompleter(self.completion_items)
        self.setCompleter(completer)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Tab:
            print("Valor buscado {}".format(self.text()))
            for item in self.completion_items:
                if item.startswith(self.text()):
                    self.setText(item)
                    break
            event.accept()
        else:
            super().