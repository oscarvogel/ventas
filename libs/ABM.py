# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from libs.Clases import Etiqueta, Grilla, EntradaTexto, Boton, Formulario
from db.SqlComandos import SQL

class Ui_ABM(Formulario):

    #tabla sobre la que se va a hacer el ABM
    tabla = ''

    #campos que se van a mostrar en la grilla
    camposAMostrar = ''

    #si necesitamos filtar por algun campo se establece con esta propiedad
    condiciones = None

    #orden en que se mostrara los datos, tambien se toma el primer elemento como campo para la busqueda
    orden = None

    #limites de datos a mostrar en la pantalla principal
    limite = 50

    controles = {}

    ValorSeleccionado = None

    def __init__(self, parent=None):
        QDialog.__init__(self, parent=None)
        self.setWindowModality(Qt.ApplicationModal)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(906, 584)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitulo = Etiqueta(Dialog, tamanio=15)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabLista = QtWidgets.QWidget()
        self.tabLista.setObjectName("tabLista")
        self.gridLayout = QtWidgets.QGridLayout(self.tabLista)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditBusqueda = EntradaTexto(self.tabLista, placeholderText="Busqueda")
        self.lineEditBusqueda.setObjectName("lineEditBusqueda")
        self.gridLayout.addWidget(self.lineEditBusqueda, 0, 0, 1, 1)

        self.tableView = Grilla(self.tabLista)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btnAgregar = Boton(self.tabLista, imagen="imagenes\\nuevo.png", tamanio=QSize(32,32))
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout.addWidget(self.btnAgregar)

        self.btnEditar = Boton(self.tabLista, imagen="imagenes\modificar.png", tamanio=QSize(32,32))
        self.btnEditar.setObjectName("btnEditar")
        self.horizontalLayout.addWidget(self.btnEditar)

        self.btnBorrar = Boton(self.tabLista, imagen="imagenes\\borrar.png", tamanio=QSize(32,32))
        self.btnBorrar.setObjectName("btnBorrar")
        self.horizontalLayout.addWidget(self.btnBorrar)

        self.btnCerrar = Boton(self.tabLista, imagen="imagenes\log-out.png", tamanio=QSize(32,32))
        self.btnCerrar.setObjectName("btnCerrar")
        self.horizontalLayout.addWidget(self.btnCerrar)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tabLista, "")
        self.tabDetalle = QtWidgets.QWidget()
        self.tabDetalle.setObjectName("tabDetalle")
        self.tabWidget.addTab(self.tabDetalle, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.grdDatos = QtWidgets.QGridLayout()

        self.tabDetalle.setEnabled(False)

        self.ArmaDatos()

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.lineEditBusqueda.textChanged.connect(self.Busqueda)
        self.btnCerrar.clicked.connect(self.Cerrar)
        self.btnEditar.clicked.connect(self.Editar)

        Dialog.setTabOrder(self.lineEditBusqueda, self.btnEditar)
        Dialog.setTabOrder(self.btnEditar, self.btnAgregar)
        Dialog.setTabOrder(self.btnAgregar, self.btnBorrar)
        Dialog.setTabOrder(self.btnBorrar, self.btnCerrar)
        Dialog.setTabOrder(self.btnCerrar, self.tableView)
        Dialog.setTabOrder(self.tableView, self.tabWidget)

        self.ArmaTabla()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lblTitulo.setText(_translate("Dialog", "TextLabel"))
        self.btnEditar.setText(_translate("Dialog", "&Editar"))
        self.btnAgregar.setText(_translate("Dialog", "&Agregar"))
        self.btnBorrar.setText(_translate("Dialog", "&Borrar"))
        self.btnCerrar.setText(_translate("Dialog", "&Cerrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLista), _translate("Dialog", "Tabla"))
        self.tabDetalle.setToolTip(_translate("Dialog", "Detalle de datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetalle), _translate("Dialog", "Detalle"))
        self.btnAceptar.setText(_translate("Dialog", "&Aceptar"))
        self.btnCancelar.setText(_translate("Dialog", "&Cancelar"))

    def setTitulo(self, texto=None):
        _translate = QtCore.QCoreApplication.translate
        if not texto:
            titulo = _translate("Abm de " ) + self.tabla

        self.lblTitulo.setText(texto)
        self.setWindowTitle(texto)

    def ArmaTabla(self):
        lista = {}
        #selecciono todos los campos de la tabla
        query = SQL().Select().From(self.tabla)

        #si tengo una condicion para el filtro la aplico, se debe pasar un diccionario estilo campo:valor
        if self.condiciones:
            query.Where(self.condiciones)

        #si estoy buscando algo hago una busqueda con like sobre el campo de orden
        if self.lineEditBusqueda.text() != '':
            lista[self.orden[0]] = self.lineEditBusqueda.text()
            query.Like(condiciones=lista)

        if self.orden:
            query.OrderBy(self.orden)

        query.Limit(self.limite)

        cursor = query.All()

        self.tableView.setColumnCount(len(self.camposAMostrar))
        self.tableView.setRowCount(len(cursor))

        for col in range(0, len(self.camposAMostrar)):
            self.tableView.setHorizontalHeaderItem(col, QTableWidgetItem(self.camposAMostrar[col].capitalize()))

        fila = 0
        for row in cursor:
            for col in range(0, len(self.camposAMostrar)):
                if isinstance(row[self.camposAMostrar[col]], int):
                    item = QTableWidgetItem(str(row[self.camposAMostrar[col]]))
                else:
                    item = QTableWidgetItem(QTableWidgetItem(row[self.camposAMostrar[col]]))

                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableView.setItem(fila, col, item)

            fila += 1
            self.tableView.resizeRowsToContents()
            self.tableView.resizeColumnsToContents()

    def Busqueda(self):
        self.ArmaTabla()

    def ArmaDatos(self):
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabDetalle)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grdDatos.setObjectName("grdDatos")
        fila = 0

        #self.label = Etiqueta(self.tabDetalle, texto="Etiqueta")
        #self.label.setObjectName("label")
        #self.grdDatos.addWidget(self.label, 0, 0, 1, 1)
        #self.lineEdit = EntradaTexto(self.tabDetalle)
        #self.lineEdit.setObjectName("lineEdit")
        #self.grdDatos.addWidget(self.lineEdit, 0, 1, 1, 1)

        #self.lblNombre = Etiqueta(self.tabDetalle, texto="Detalle nombre")
        #self.lblNombre.setObjectName("lblNombre")
        #self.grdDatos.addWidget(self.lblNombre, 0, 2, 1, 2)

        self.verticalLayout_2.addLayout(self.grdDatos)

        self.grdBotones = QtWidgets.QGridLayout()
        self.grdBotones.setObjectName("grdBotones")
        self.btnAceptar = Boton(self.tabDetalle, imagen="imagenes\\aceptar.bmp", tamanio=QSize(32,32))
        self.btnAceptar.setObjectName("btnAceptar")
        self.grdBotones.addWidget(self.btnAceptar, 0, 0, 1, 1)

        self.btnCancelar = Boton(self.tabDetalle, imagen="imagenes\log-out.png", tamanio=QSize(32,32))
        self.btnCancelar.setObjectName("btnCancelar")
        self.grdBotones.addWidget(self.btnCancelar, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.grdBotones)
        self.tabWidget.addTab(self.tabDetalle, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.btnCancelar.clicked.connect(self.btnCancelarClicked)


    def btnCancelarClicked(self):
        self.tabWidget.setCurrentIndex(0)
        self.tabDetalle.setEnabled(False)

    def Editar(self):
        self.ValorSeleccionado = self.tableView.item(self.tableView.currentRow(), 0).text()
        self.tabDetalle.setEnabled(True)
        self.tabWidget.setCurrentIndex(1)
