# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("ABM")
        Dialog.resize(906, 584)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tabLista = QtWidgets.QWidget()
        self.tabLista.setObjectName("tabLista")
        self.gridLayout = QtWidgets.QGridLayout(self.tabLista)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableView = QtWidgets.QTableView(self.tabLista)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btnEditar = QtWidgets.QPushButton(self.tabLista)
        self.btnEditar.setObjectName("btnEditar")
        self.verticalLayout_2.addWidget(self.btnEditar)
        self.btnAgregar = QtWidgets.QPushButton(self.tabLista)
        self.btnAgregar.setObjectName("btnAgregar")
        self.verticalLayout_2.addWidget(self.btnAgregar)
        self.btnBorrar = QtWidgets.QPushButton(self.tabLista)
        self.btnBorrar.setObjectName("btnBorrar")
        self.verticalLayout_2.addWidget(self.btnBorrar)
        self.btnCerrar = QtWidgets.QPushButton(self.tabLista)
        self.btnCerrar.setObjectName("btnCerrar")
        self.verticalLayout_2.addWidget(self.btnCerrar)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tabLista, "")
        self.tabDetalle = QtWidgets.QWidget()
        self.tabDetalle.setObjectName("tabDetalle")
        self.tabWidget.addTab(self.tabDetalle, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "TextLabel"))
        self.btnEditar.setText(_translate("Dialog", "&Editar"))
        self.btnAgregar.setText(_translate("Dialog", "&Agregar"))
        self.btnBorrar.setText(_translate("Dialog", "&Borrar"))
        self.btnCerrar.setText(_translate("Dialog", "&Cerrar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLista), _translate("Dialog", "Tabla"))
        self.tabDetalle.setToolTip(_translate("Dialog", "Detalle de datos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDetalle), _translate("Dialog", "Detalle"))

