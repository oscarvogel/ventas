# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aberturas.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from libs import Clases
from libs.Clases import Etiqueta, EntradaTexto
from libs.Validaciones import ValidaClienteTexto, CboPago, ValidaPago, ValidaConTexto


class Ui_Aberturas(Clases.Formulario):

    def __init__(self):
        Clases.Formulario.__init__(self)
        self.setupUi(self)

    def setupUi(self, Aberturas):
        Aberturas.setObjectName("Aberturas")
        Aberturas.setWindowModality(QtCore.Qt.WindowModal)
        Aberturas.resize(731, 352)
        self.label = Etiqueta(Aberturas, texto='Cliente')
        self.label.setGeometry(QtCore.QRect(9, 9, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.horizontalLayoutWidget = QtWidgets.QWidget(Aberturas)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 0, 441, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        #self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout = ValidaClienteTexto(parent=self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.horizontalLayoutWidgetCondPago = QtWidgets.QWidget(Aberturas)
        self.horizontalLayoutWidgetCondPago.setGeometry(QtCore.QRect(100, 30, 391, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidgetCondPago")

        self.txtCondPago = ValidaPago(parent=self.horizontalLayoutWidgetCondPago)
        self.txtCondPago.setContentsMargins(0,0,0,0)
        self.txtCondPago.setObjectName("txtCondPago")

        self.label_3 = Etiqueta(Aberturas, "Cond. Pago")
        self.label_3.setObjectName("label_3")
        self.label_3.setGeometry(QtCore.QRect(10, 40, 83, 19))

        self.lineTE = EntradaTexto(Aberturas, placeholderText="Telefono cliente")
        self.lineTE.setGeometry(QtCore.QRect(553, 40, 172, 20))

        self.label_4 = Etiqueta(Aberturas, texto="TE:")
        self.label_4.setGeometry(QtCore.QRect(510, 40, 83, 19))

        QtCore.QMetaObject.connectSlotsByName(Aberturas)

        self.horizontalLayout.lineEdit.textChanged.connect(self.SaleCliente)
        Aberturas.setTabOrder(self.txtCondPago, self.lineTE)

    def SaleCliente(self):
        if self.horizontalLayout.pago:
            self.txtCondPago.lineEdit.setText(self.horizontalLayout.pago)

    def retranslateUi(self, Aberturas):
        _translate = QtCore.QCoreApplication.translate
        Aberturas.setWindowTitle(_translate("Aberturas", "Dialog"))
        self.label.setText(_translate("Aberturas", "Cliente"))
        self.lineEdit.setPlaceholderText(_translate("Aberturas", "Código cliente"))
        self.label_2.setText(_translate("Aberturas", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Aberturas = QtWidgets.QDialog()
    ui = Ui_Aberturas()
    ui.setupUi(Aberturas)
    Aberturas.show()
    sys.exit(app.exec_())

