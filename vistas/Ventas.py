# -*- coding: utf-8 -*-
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from libs.Clases import Formulario, EtiquetaRoja, EntradaTexto, BotonCerrarFormulario, Etiqueta, Fecha, Grilla

from modelos import Clientes

class Ui_Dialog(Formulario):

    cliente = 1

    def __init__(self):
        Formulario.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(934, 642)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lblTitulo = EtiquetaRoja(Dialog, texto="Ultimo articulo:", tamanio=15)
        self.lblTitulo.setObjectName("lblTitulo")
        self.gridLayout_4.addWidget(self.lblTitulo, 0, 0, 1, 1)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.tableView = Grilla(Dialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.lineEditCodBarra = EntradaTexto(Dialog, placeholderText='Ingrese cantidad y codigo de barra')
        self.lineEditCodBarra.setObjectName("lineEditCodBarra")
        self.gridLayout_3.addWidget(self.lineEditCodBarra, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnSalir = BotonCerrarFormulario(Dialog)
        self.btnSalir.setObjectName("btnSalir")
        self.gridLayout.addWidget(self.btnSalir, 0, 1, 1, 2)
        self.lblFecha = Etiqueta(Dialog, texto='Fecha:')
        self.lblFecha.setObjectName("lblFecha")
        self.gridLayout.addWidget(self.lblFecha, 1, 0, 1, 1)
        self.dateEdit = Fecha(Dialog)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setFecha()
        self.dateEdit.setEnabled(False)

        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 2)
        self.graphicsView = QtWidgets.QGraphicsView(Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 2, 0, 1, 3)

        self.ArmaSubTotal(Dialog)

        self.lblTotal = EtiquetaRoja(Dialog, texto='Total')
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout.addWidget(self.lblTotal, 7, 1, 1, 1)
        self.lineEditTotal = EntradaTexto(Dialog)
        self.lineEditTotal.setObjectName("lineEditTotal")
        self.lineEditTotal.setEnabled(False)
        self.gridLayout.addWidget(self.lineEditTotal, 7, 2, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lblCliente = EtiquetaRoja(Dialog, texto="Cliente:")
        self.lblCliente.setObjectName("lblCliente")
        self.gridLayout_2.addWidget(self.lblCliente, 0, 0, 1, 1)
        self.lblInfo = EtiquetaRoja(Dialog, texto="F2 Busqueda Articulo / F5 Carga Cliente")
        self.lblInfo.setObjectName("lblInfo")
        self.gridLayout_2.addWidget(self.lblInfo, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 2, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_4)

        #self.retranslateUi(Dialog)
        Dialog.setTabOrder(self.lineEditCodBarra, self.tableView)
        Dialog.setTabOrder(self.tableView, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.graphicsView)
        Dialog.setTabOrder(self.graphicsView, self.lineEditTotal)
        Dialog.setTabOrder(self.lineEditTotal, self.btnSalir)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.ArmaCabeceraGrilla()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTitulo.setText(_translate("Dialog", "TextLabel"))
        self.btnSalir.setText(_translate("Dialog", "&Salir"))
        self.lblFecha.setText(_translate("Dialog", "Fecha comprobante"))
        self.lblTotal.setText(_translate("Dialog", "Total"))
        self.lblCliente.setText(_translate("Dialog", "TextLabel"))
        self.lblInfo.setText(_translate("Dialog", "TextLabel"))

    def ArmaSubTotal(self, Dialog):

        if Clientes.Cliente().Discrimina(self.cliente):
            self.lblSubTotal = Etiqueta(Dialog, texto='Sub Total')
            self.gridLayout.addWidget(self.lblSubTotal, 3, 1, 1, 1)
            self.lineEditSubTotal = EntradaTexto(Dialog)
            self.lineEditSubTotal.setEnabled(False)
            self.gridLayout.addWidget(self.lineEditSubTotal, 3, 2, 1, 1)

            self.lblIVA = Etiqueta(Dialog, texto='IVA')
            self.gridLayout.addWidget(self.lblIVA, 4, 1, 1, 1)
            self.lineEditIVA = EntradaTexto(Dialog)
            self.lineEditIVA.setEnabled(False)
            self.gridLayout.addWidget(self.lineEditIVA, 4, 2, 1, 1)

            self.lblPercepDGR = Etiqueta(Dialog, texto='Percep. DGR')
            self.gridLayout.addWidget(self.lblPercepDGR, 5, 1, 1, 1)
            self.lineEditPercepDGR = EntradaTexto(Dialog)
            self.lineEditPercepDGR.setEnabled(False)
            self.gridLayout.addWidget(self.lineEditPercepDGR, 5, 2, 1, 1)

    def ArmaCabeceraGrilla(self):
        self.tableView.ArmaCabeceras(['Cant.', 'UN', 'Detalle', 'Unitario', 'Total'])