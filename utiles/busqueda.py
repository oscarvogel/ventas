# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from libs.Clases import Formulario, BotonCerrarFormulario, BotonAceptar, EntradaTexto
from db.SqlComandos import SQL

class Ui_Busqueda(Formulario):

    tabla = ""
    cOrden = ""
    limite = 100
    campos = []
    campoBusqueda = "nombre"
    lRetval = False
    ValorRetorno = ''
    camposTabla = None
    campoRetorno = None
    colRetorno = 0
    colBusqueda = 0
    campoRetornoDetalle = ''
    condiciones = ''

    def __init__(self):
        Formulario.__init__(self)
        self.setupUi(self)
        #self.CargaDatos()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(829, 556)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = EntradaTexto(Dialog, tooltip='Ingresa tu busqueda',
                                     placeholderText="Ingresa tu busqueda")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.tableView = QtWidgets.QTableWidget(Dialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAceptar = BotonAceptar(Dialog, textoBoton="&Seleccionar")
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = BotonCerrarFormulario(Dialog)
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.verticalLayout.addLayout(self.horizontalLayout)

        #self.retranslateUi(Dialog)
        self.btnCancelar.clicked.connect(self.Cerrar)
        self.lineEdit.textChanged.connect(self.CargaDatos)
        self.btnAceptar.clicked.connect(self.Aceptar)
        self.tableView.cellClicked.connect(self.cell_was_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Busqueda en " + self.tabla))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar"))
        self.btnCancelar.setText(_translate("Dialog", "Cerrar"))

    def Aceptar(self):
        self.lRetval = True
        self.ValorRetorno = self.tableView.currentItem().text()
        self.ValorRetorno = self.tableView.item(self.tableView.currentRow(), self.colRetorno).text()
        self.campoRetornoDetalle  = self.tableView.item(self.tableView.currentRow(), self.colBusqueda).text()
        print("Seleccionado {} columna {} fila {}".format(self.ValorRetorno,
                                                          self.tableView.currentColumn(),
                                                          self.tableView.currentRow()) )
        self.close()

    def cell_was_clicked(self, row, column):
        item = self.tableView.itemAt(row, column)

        self.ValorRetorno = item.text()
        print("Row {} and Column {} was clicked value {}".format(row, column, self.tableView.currentItem().text()))

    def CargaDatos(self):

        textoBusqueda = self.lineEdit.text()

        if self.condiciones and textoBusqueda:
            if not self.condiciones.endswith(" and "):
                self.condiciones += " and "
        else:
            if self.condiciones.endswith(" and "):
                self.condiciones = self.condiciones[:-4]

        if not self.camposTabla:
            self.camposTabla = self.campos

        if textoBusqueda:
            rows = SQL().BuscaTodo(tabla=self.tabla,
                                   cOrden=self.cOrden,
                                   limite=self.limite,
                                   cFiltro= self.condiciones +
                                            self.campoBusqueda + " like '%" + textoBusqueda + "%'",
                                   campos=self.camposTabla)
        else:
            rows = SQL().BuscaTodo(tabla=self.tabla,
                                   cFiltro=self.condiciones,
                                   cOrden=self.cOrden,
                                   limite=self.limite,
                                   campos=self.camposTabla)
        self.tableView.setColumnCount(len(self.campos))
        self.tableView.setRowCount(len(rows))
        #self.tableView.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)

        for col in range(0, len(self.campos)):
            if self.campos[col] == self.campoRetorno:
                self.colRetorno = col
            if self.campos[col] == self.campoBusqueda:
                self.colBusqueda = col

            self.tableView.setHorizontalHeaderItem(col, QTableWidgetItem(self.campos[col].capitalize()))

        fila = 0
        for row in rows:
            for col in range(0, len(self.campos)):
                if isinstance(row[self.campos[col]], int):
                    item = QTableWidgetItem(str(row[self.campos[col]]))
                else:
                    item = QTableWidgetItem(QTableWidgetItem(row[self.campos[col]]))

                item.setFlags(QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled)
                self.tableView.setItem(fila, col, item)

            fila += 1
        self.tableView.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Down:
            self.tableView.setFocus()
        elif event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
            self.btnAceptar.click()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Busqueda()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
