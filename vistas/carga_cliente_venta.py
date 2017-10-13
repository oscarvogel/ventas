
from PyQt5 import QtCore, QtGui, QtWidgets

from libs.Clases import Formulario, Etiqueta, EntradaTexto, CheckBox, BotonAceptar
from libs.Validaciones import ValidaCliente, ValidaClienteTexto, CboPago, CboTipoResp


class Ui_dlgCliente(Formulario):

    def __init__(self):
        Formulario.__init__(self)
        self.setWindowTitle("Carga de datos de cliente")
        self.setupUi(self)

    def setupUi(self, dlgCliente):
        dlgCliente.setObjectName("dlgCliente")
        dlgCliente.resize(771, 244)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dlgCliente)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.lblTitulo = Etiqueta(dlgCliente, tamanio=15)
        self.lblTitulo.setObjectName("lblTitulo")
        self.verticalLayout.addWidget(self.lblTitulo)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.lblCboFormaPago = Etiqueta(dlgCliente)
        self.lblCboFormaPago.setObjectName("lblCboFormaPago")
        self.gridLayout.addWidget(self.lblCboFormaPago, 5, 0, 1, 1)

        self.lineDomicilio = EntradaTexto(dlgCliente, enabled=False)
        self.lineDomicilio.setObjectName("lineDomicilio")
        self.gridLayout.addWidget(self.lineDomicilio, 2, 2, 1, 1)

        self.cboFormaPago = CboPago(dlgCliente)
        self.cboFormaPago.setObjectName("cboFormaPago")
        self.gridLayout.addWidget(self.cboFormaPago, 5, 2, 1, 1)

        self.lblCuotaTarjeta = Etiqueta(dlgCliente)
        self.lblCuotaTarjeta.setObjectName("lblCuotaTarjeta")
        self.gridLayout.addWidget(self.lblCuotaTarjeta, 6, 0, 1, 1)

        self.lineCuotaTarjeta = QtWidgets.QLineEdit(dlgCliente)
        self.lineCuotaTarjeta.setObjectName("lineCuotaTarjeta")
        self.gridLayout.addWidget(self.lineCuotaTarjeta, 6, 2, 1, 1)

        self.lblSitFteIVA = Etiqueta(dlgCliente)
        self.gridLayout.addWidget(self.lblSitFteIVA, 3, 0, 1, 1)

        self.lineLimCredito = EntradaTexto(dlgCliente)
        self.lineLimCredito.setObjectName("lineLimCredito")
        self.gridLayout.addWidget(self.lineLimCredito, 4, 2, 1, 1)

        self.vldCliente = ValidaCliente(dlgCliente)
        self.vldCliente.setObjectName("vldCliente")
        self.gridLayout.addWidget(self.vldCliente, 0, 2, 1, 1)

        self.lblDomicilio = Etiqueta(dlgCliente)
        self.lblDomicilio.setObjectName("lblDomicilio")
        self.gridLayout.addWidget(self.lblDomicilio, 2, 0, 1, 1)

        self.lineSitFteIVA = EntradaTexto(dlgCliente)
        self.lineSitFteIVA.setObjectName("lineSitFteIVA")
        self.gridLayout.addWidget(self.lineSitFteIVA, 3, 2, 1, 1)

        self.lblLimCred = Etiqueta(dlgCliente)
        self.lblLimCred.setObjectName("lblLimCred")
        self.gridLayout.addWidget(self.lblLimCred, 4, 0, 1, 1)

        self.lblCliente = Etiqueta(dlgCliente)
        self.lblCliente.setObjectName("lblCliente")
        self.gridLayout.addWidget(self.lblCliente, 0, 0, 1, 1)

        self.lblNombreCli = Etiqueta(dlgCliente)
        self.lblNombreCli.setObjectName("lblNombreCli")
        self.gridLayout.addWidget(self.lblNombreCli, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.chkTicketFactura = CheckBox(dlgCliente)
        self.chkTicketFactura.setObjectName("chkTicketFactura")
        self.verticalLayout.addWidget(self.chkTicketFactura)
        self.pushButtonAceptar = BotonAceptar(dlgCliente)
        self.pushButtonAceptar.setObjectName("pushButtonAceptar")
        self.verticalLayout.addWidget(self.pushButtonAceptar)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(dlgCliente)
        QtCore.QMetaObject.connectSlotsByName(dlgCliente)
        dlgCliente.setTabOrder(self.vldCliente, self.lineDomicilio)
        dlgCliente.setTabOrder(self.lineDomicilio, self.lineSitFteIVA)
        dlgCliente.setTabOrder(self.lineSitFteIVA, self.lineLimCredito)
        dlgCliente.setTabOrder(self.lineLimCredito, self.cboFormaPago)
        dlgCliente.setTabOrder(self.cboFormaPago, self.lineCuotaTarjeta)
        dlgCliente.setTabOrder(self.lineCuotaTarjeta, self.chkTicketFactura)
        dlgCliente.setTabOrder(self.chkTicketFactura, self.pushButtonAceptar)

        self.vldCliente.textChanged.connect(self.CambioCliente)

    def CambioCliente(self):
        self.lblNombreCli.setText(self.vldCliente.nombre)


    def retranslateUi(self, dlgCliente):
        _translate = QtCore.QCoreApplication.translate
        dlgCliente.setWindowTitle(_translate("dlgCliente", "Carga datos de Cliente"))
        self.lblTitulo.setText(_translate("dlgCliente", "Carga datos de Cliente"))
        self.lblCboFormaPago.setText(_translate("dlgCliente", "Forma de pago"))
        self.lblCuotaTarjeta.setText(_translate("dlgCliente", "Cuotas Tarjeta"))
        self.lblSitFteIVA.setText(_translate("dlgCliente", "Sit. Fte. IVA"))
        self.lblDomicilio.setText(_translate("dlgCliente", "Domicilio"))
        self.lblLimCred.setText(_translate("dlgCliente", "Limite de credito"))
        self.lblCliente.setText(_translate("dlgCliente", "Codigo Cliente"))
        self.lblNombreCli.setText(_translate("dlgCliente", "Nombre"))
        self.chkTicketFactura.setText(_translate("dlgCliente", "Ticket Factura?"))
        self.pushButtonAceptar.setText(_translate("dlgCliente", "Aceptar"))
