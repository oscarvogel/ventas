# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from libs.Clases import Formulario, Etiqueta, EntradaTexto, Spinner


class Ui_Dialog(Formulario):

    precio = 0.00
    def __init__(self, parent=None):
        Formulario.__init__(self)
        self.setWindowTitle("Precio Producto")
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 123)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = Etiqueta(Dialog, texto="Precio Articulo")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = EntradaTexto(Dialog, placeholderText="Precio de articulo")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)

        self.lineEdit.textChanged.connect(self.CambiaPrecio)
        self.lineEdit.returnPressed.connect(self.Cerrar)

        #self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))

    def CambiaPrecio(self):
        self.precio = self.lineEdit.text()