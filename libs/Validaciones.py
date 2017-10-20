# coding=utf-8
from PyQt5 import QtCore
from PyQt5.QtCore import QEvent, pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QWidget
from PyQt5.uic.properties import QtGui, QtWidgets

from db.SqlComandos import SQL
from libs.Clases import EntradaTexto, Etiqueta, ComboSQL
from utiles.busqueda import Ui_MainWindow


class Validaciones(EntradaTexto):

    #tabla sobre la que se consulta
    tabla = ''

    #orden para la busqueda si se presiona F2
    cOrden = ''

    #campos que se van a mostrar
    campos = ''

    #campos de la tabla, permite hacer uniones de campos
    camposTabla = None

    #el campo que va a retornar la busqueda
    campoRetorno = None

    #el campo del nombre
    campoNombre = None

    #largo se utiliza para la cantidad de ingreso y para el zfill y rellanar con ceros
    largo = 0

    #este es el widget que va a contener la descripcion del nombre
    widgetNombre = None

    #en caso de que necesitems hacer una condicion para mostrar los datos se utiliza esta propiedad
    condiciones = ''

    #indica si el valor obtenido es valido o no
    valido = False

    #cursor que guarda los valores obtenidos por el outfocus
    cursor = None

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)
        if self.largo != 0:
            self.setMaxLength(self.largo)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F2:
            ventana = Ui_MainWindow()
            ventana.tabla = self.tabla
            ventana.cOrden = self.cOrden
            ventana.campos = self.campos
            ventana.campoBusqueda = self.cOrden
            ventana.camposTabla = self.camposTabla
            ventana.campoRetorno = self.campoRetorno
            ventana.condiciones = self.condiciones
            ventana.CargaDatos()
            ventana.exec_()
            if ventana.lRetval:
                self.valido = True
                self.setText(ventana.ValorRetorno)
                QLineEdit.keyPressEvent(self, event)
        elif event.key() == QtCore.Qt.Key_Enter:
            if self.proximoWidget:
                self.proximoWidget.setFocus()
        else:
            QLineEdit.keyPressEvent(self, event)

    def focusOutEvent(self, QFocusEvent):
        self.setText(self.text().zfill(self.largo))


class ValidaConTexto(Validaciones):

    def __init__(self, *args, **kwargs):
        super(Validaciones, self).__init__(*args, **kwargs)
        parent = kwargs['parent']
        self.horizontalLayoutWidget = QHBoxLayout(parent)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lineEdit = Validaciones(parent)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget.addWidget(self.lineEdit)

        self.lblNombre = Etiqueta(parent)
        self.lblNombre.setObjectName("label_2")
        self.horizontalLayoutWidget.addWidget(self.lblNombre)
        self.lblNombre.setText("TextLabel")
        self.lineEdit.textChanged.connect(self.CambioTexto)

    def CambioTexto(self):
        data = SQL().BuscaUno(self.tabla, self.campoRetorno, self.lineEdit.text().zfill(self.largo))
        if data:
            self.lblNombre.setText(data[self.campoNombre])



class ValidaCliente(Validaciones):

    ventana = None
    valor = None

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F2:
            ventana = Ui_MainWindow()
            ventana.tabla = "clientes"
            ventana.cOrden = "Nombre"
            ventana.campos = ['CLIENTE','NOMBRE','IDCLIENTE']
            ventana.camposTabla = ['concat(zona,cliente) CLIENTE', 'NOMBRE', 'IDCLIENTE']
            ventana.campoRetorno = 'CLIENTE'
            ventana.CargaDatos()
            ventana.exec_()
            event.accept()
            if ventana.lRetval:
                self.setText(ventana.ValorRetorno)
            QLineEdit.keyPressEvent(self, event)
        else:
            QLineEdit.keyPressEvent(self, event)

    def focusOutEvent(self, QFocusEvent):
        self.setText(self.text().zfill(5))

class ValidaClienteTexto(QWidget):

    ventana = None
    pago = ''

    def __init__(self, parent=None, *args, **kwargs):
        super(ValidaClienteTexto, self).__init__(parent, *args, **kwargs)
        self.installEventFilter(self)
        self.horizontalLayoutWidget = QHBoxLayout(parent)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.lineEdit = ValidaCliente(parent)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget.addWidget(self.lineEdit)

        self.lblNombre = Etiqueta(parent)
        self.lblNombre.setObjectName("label_2")
        self.horizontalLayoutWidget.addWidget(self.lblNombre)
        self.lblNombre.setText("TextLabel")

        self.lineEdit.textChanged.connect(self.CambioTexto)
        self.lineEdit.returnPressed.connect(self.PresionaEnter)

    def CambioTexto(self):
        data = SQL().BuscaUno("clientes", "concat(zona,cliente)", self.lineEdit.text().zfill(5))
        if data:
            self.lblNombre.setText(data['NOMBRE'])
            self.pago = data['PAGO']

    def PresionaEnter(self):
        pass


class ValidaPago(ValidaConTexto):
    ventana = None
    largo = 2
    tabla = 'pagos'
    campoRetorno = 'PAGO'
    cOrden = 'DETALLE'
    campos = ['PAGOS', 'DETALLE']
    campoNombre = "DETALLE"


class CboPago(ComboSQL):

    tabla = 'pagos'
    campo1 = 'DETALLE'
    campovalor = 'PAGO'
    cOrden = 'detalle'
    condicion = 'lista = 1 or lista = " "'


class CboUsuario(ComboSQL):
    tabla = 'usuarios'
    campo1 = 'USUARIO'
    campovalor = 'USU_ID'
    condicion = 'activo=1'
    cOrden = 'usuario'

    def __init__(self, parent=None):
        super().__init__(parent)


class Articulos(Validaciones):
    tabla = "articulos"
