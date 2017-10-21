# -*- coding: utf-8 -*-

import winsound
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QTableWidgetItem, QStatusBar

from libs.Clases import Formulario, EtiquetaRoja, EntradaTexto, BotonCerrarFormulario, Etiqueta, Fecha, Grilla

from modelos import Clientes, Articulo
from utiles import Ventanas, Facturacion
from utiles.busqueda import Ui_Busqueda
from vistas import precio_articulo


class Ui_Dialog(Formulario):

    cliente = 1
    lBalanza = False
    facturacion = None
    cursorart = None
    nCant = 0.0000
    nPrecio = 0.0000
    lFactura = False
    defaultColor = None

    def __init__(self):
        Formulario.__init__(self)
        self.setWindowTitle("Ventas")
        self.setupUi(self)
        self.facturacion = Facturacion.facturacion()
        self.defaultColor = self.palette().color(QPalette.Background)

    def keyPressEvent(self, event):
        teclas = [QtCore.Qt.Key_Escape, QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter]
        if event.key() == QtCore.Qt.Key_F5:
            _ventana = Ui_Busqueda()
            _ventana.tabla = "clientes"
            _ventana.cOrden = "nombre"
            _ventana.campos = ['idCliente','Nombre','Domicilio']
            _ventana.campoRetorno = 'idCliente'
            _ventana.campoBusqueda = 'Nombre'
            _ventana.CargaDatos()
            _ventana.exec_()
            if _ventana.lRetval:
                self.lblCliente.setText(_ventana.campoRetornoDetalle)
                self.cliente = _ventana.ValorRetorno
        elif event.key() == QtCore.Qt.Key_F2:
            _ventana = Ui_Busqueda()
            _ventana.tabla = "articulos"
            _ventana.cOrden = "Nombre"
            _ventana.campos = ['CodBarraArt', 'nombre', 'idArticulo', 'unidad', 'stock']
            _ventana.campoRetorno = 'CodBarraArt'
            _ventana.campoBusqueda = 'nombre'
            _ventana.CargaDatos()
            _ventana.exec_()
            if _ventana.lRetval:
                valor = self.lineEditCodBarra.text()
                self.lineEditCodBarra.setText(valor + _ventana.ValorRetorno)
        elif event.key() == QtCore.Qt.Key_F8:
            self.lFactura = not self.lFactura
            if self.lFactura:
                self.setStyleSheet('background:orange')
            else:
                self.setStyleSheet('background:rgb({},{},{})'.format(self.defaultColor.red(),
                                                                     self.defaultColor.green(),
                                                                     self.defaultColor.blue()))
        elif event.key() not in teclas:
            super(Formulario, self).keyPressEvent(event)

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

        self.tableView = Grilla(Dialog, tamanio=10)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.lineEditCodBarra = EntradaTexto(Dialog,
                                             placeholderText='Ingrese cantidad y codigo de barra',
                                             tamanio=15)
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
        self.graphicsView = Etiqueta(Dialog, texto='Imagen')
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

        self.btnSalir.clicked.connect(self.Cerrar)
        #self.lineEditCodBarra.textChanged.connect(self.CargaArticulo)
        self.lineEditCodBarra.returnPressed.connect(self.CargaPrecioArticulo)

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
        self.tableView.ArmaCabeceras(['Cant.', 'UN', 'Detalle', 'Unitario', 'Total',
                                      'Neto', 'IVA', 'DGR', 'idArticulo'])
        self.tableView.columnasOcultas = [5,6,7,8]
        self.tableView.OcultaColumnas()

    def CargaPrecioArticulo(self):
        codigobarra = self.lineEditCodBarra.text()
        self.lBalanza = False

        if codigobarra.startswith("+"):
            monto = codigobarra[1:]
            if float(monto) >= self.lineEditTotal.text():
                self.Procesatotales()
            else:
                Ventanas.showAlert("El monto es menor al total de la compra")
                winsound.PlaySound("*", winsound.SND_ASYNC)

        #si tiene incluido el * indica que la cantidad es mas que uno
        if codigobarra.find("*") == -1:
            articulo = codigobarra
            self.nCant = "1"
        else:
            articulo = codigobarra[codigobarra.find("*") + 1:]
            self.nCant = codigobarra[:codigobarra.find("*")]

        self.cursorart = Articulo.Articulo().BuscaUno(campo = 'CodBarraArt', valorbuscado=articulo)
        if not self.cursorart:
            self.cursorart = Articulo.Articulo().BuscaUno(campo='PLU', valorbuscado=codigobarra[1:7])
            if not self.cursorart:
                winsound.PlaySound("*", winsound.SND_ASYNC)
                return
            else:
                self.lBalanza = True

        if Articulo.Articulo().ModificaPrecios(self.cursorart['idArticulo']) or \
                        self.facturacion.CalculaPrecio(self.cursorart['idArticulo']) == 0:
            #carga el precio del articulo
            _ventana = precio_articulo.Ui_Dialog()
            _ventana.exec_()
            self.nPrecio = _ventana.lineEdit.text()
        else:
            self.nPrecio = self.facturacion.nPrecioPub
        self.CargaArticulo()
        self.SumaTodo()
        self.lineEditCodBarra.setText("")
        self.lblTitulo.setText("Ultimo articulo: " + self.cursorart['NombreTicket'].strip())
        if self.cursorart['Imagen'].strip() != '':
            image = QtGui.QImage(self.cursorart['Imagen'].strip())
        else:
            image = QtGui.QImage('imagenes\market.png')

        if not image.isNull():
            self.pixmap = QtGui.QPixmap(image)
            self.graphicsView.setScaledContents(True)
            self.graphicsView.setPixmap(self.pixmap)
            self.graphicsView.setMinimumSize(1,1)
            self.graphicsView.installEventFilter(self)
            #self.graphicsView.setScaledContents(True)

    def eventFilter(self, source, event):
        if (source is self.graphicsView and event.type() == QtCore.QEvent.Resize):
            # re-scale the pixmap when the label resizes
            self.graphicsView.setPixmap(self.pixmap.scaled(
                self.graphicsView.size(), QtCore.Qt.KeepAspectRatio,
                QtCore.Qt.SmoothTransformation))
        return super(Formulario, self).eventFilter(source, event)

    def CargaArticulo(self):
        fila = self.tableView.rowCount() + 1
        self.tableView.setRowCount(fila)
        print("Fila {}".format(fila))
        self.tableView.setItem(fila - 1, 0, QTableWidgetItem(self.nCant))
        self.tableView.setItem(fila - 1, 1, QTableWidgetItem(self.cursorart['Unidad']))
        self.tableView.setItem(fila - 1, 2, QTableWidgetItem(self.cursorart['NombreTicket'].strip()))
        self.tableView.setItem(fila - 1, 3, QTableWidgetItem(str(self.nPrecio)))
        self.tableView.setItem(fila - 1, 4, QTableWidgetItem(str(float(self.nPrecio) * float(self.nCant))))

        self.tableView.resizeColumnsToContents()

    def SumaTodo(self):
        nTotal = 0.00
        data = self.RecorreTableView()
        for x in data:
            nTotal += float(x[3])

        self.lineEditTotal.setText(str(nTotal))


    def RecorreTableView(self):
        data = []
        model = self.tableView.model()
        for row in range(model.rowCount()):
            data.append([])
            for column in range(model.columnCount()):
                index = model.index(row, column)
                # We suppose data are strings
                data[row].append(model.data(index))
        return data


    def Procesatotales(self):
        pass

