# -*- coding: utf-8 -*-

from libs.ABM import Ui_ABM
from libs.Clases import Etiqueta, EntradaTexto
from modelos import Clientes


class ClientesABM(Ui_ABM):

    def __init__(self):
        self.tabla = "Clientes"
        self.camposAMostrar = ['idCliente', 'Nombre', 'Domicilio', 'Telefono']
        self.orden = ["Nombre",]
        super().__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.setTitulo("ABM de Clientes")

    def ArmaDatos(self):
        super().ArmaDatos()
        self.label = Etiqueta(self.tabDetalle, texto="Codigo")
        self.label.setObjectName("label")
        self.grdDatos.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = EntradaTexto(self.tabDetalle)
        self.lineEdit.setObjectName("lineEdit")
        self.grdDatos.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.labelNombre = Etiqueta(self.tabDetalle, texto="Nombre")
        self.labelNombre.setObjectName("labelNombre")
        self.grdDatos.addWidget(self.labelNombre, 1, 0, 1, 1)

        self.lineEditNombre = EntradaTexto(self.tabDetalle, inputmask='[A-Z_]+')
        self.lineEditNombre.setObjectName("lineEditNombre")
        self.grdDatos.addWidget(self.lineEditNombre, 1, 1, 1, 1)

        self.labelDomicilio = Etiqueta(self.tabDetalle, texto="Domicilio")
        self.labelDomicilio.setObjectName("labelDomicilio")
        self.grdDatos.addWidget(self.labelDomicilio, 2, 0, 1, 1)

        self.lineEditDomicilio = EntradaTexto(self.tabDetalle)
        self.lineEditDomicilio.setObjectName("lineEditDomicilio")
        self.grdDatos.addWidget(self.lineEditDomicilio, 2, 1, 1, 1)

        #self.lblNombre = Etiqueta(self.tabDetalle, texto="Detalle nombre")
        #self.lblNombre.setObjectName("lblNombre")
        #self.grdDatos.addWidget(self.lblNombre, 0, 2, 1, 2)

    def Editar(self):
        super().Editar()
        cliente = Clientes.Cliente()
        cliente.tabla = self.tabla
        cliente.campoclave = 'idCliente'

        datos = cliente.BuscaPorCampoClave(self.ValorSeleccionado)

        self.lineEdit.setText(str(datos['idCliente']))
        self.lineEdit.setEnabled(False)
        self.lineEditNombre.setText(datos['Nombre'])
        self.lineEditDomicilio.setText(datos['Domicilio'])
