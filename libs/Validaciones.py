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

    tabla = ''
    cOrden = ''
    campos = ''
    camposTabla = None
    campoRetorno = None
    campoNombre = None
    largo = 0

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        font = QFont()
        font.setPointSizeF(12)
        self.setFont(font)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F2:
            ventana = Ui_MainWindow()
            ventana.tabla = self.tabla
            ventana.cOrden = self.cOrden
            ventana.campos = self.campos
            ventana.camposTabla = self.camposTabla
            ventana.campoRetorno = self.campoRetorno
            ventana.CargaDatos()
            ventana.exec_()
            if ventana.lRetval:
                self.setText(ventana.ValorRetorno)
                QLineEdit.keyPressEvent(self, event)
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
    nombre = None

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F2:
            ventana = Ui_MainWindow()
            ventana.tabla = "clientes"
            ventana.cOrden = "Nombre"
            ventana.campos = ['idCliente','Nombre','Domicilio']
            ventana.camposTabla = ['idCliente', 'Nombre', 'Domicilio']
            ventana.campoRetorno = 'idCliente'
            ventana.campoBusqueda = "Nombre"
            ventana.CargaDatos()
            ventana.exec_()
            event.accept()
            if ventana.lRetval:
                self.setText(ventana.ValorRetorno)
                self.nombre = ventana.campoRetornoDetalle
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

    tabla = 'formapago'
    campo1 = 'Detalle'
    campovalor = 'idFormaPago'
    cOrden = 'Detalle'


class CboUsuario(ComboSQL):
    tabla = 'usuarios'
    campo1 = 'USUARIO'
    campovalor = 'USU_ID'
    condicion = 'activo=1'
    cOrden = 'usuario'

    def __init__(self, parent=None):
        super().__init__(parent)

class CboTipoResp(ComboSQL):

    tabla = 'tiporesp'
    campo1 = 'Nombre'
    campovalor = 'idTipoResp'
    cOrden = 'Nombre'