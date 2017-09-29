from PyQt5 import QtCore, QtGui, QtWidgets

from libs import Clases
from libs.Validaciones import CboUsuario
from modelos import Usuarios
from utiles import Ventanas
from utiles.Funciones import GrabaConf


class Login(Clases.Formulario):

    lRetval = False
    cUsuario = ''
    idUsuario = None

    def __init__(self):
        Clases.Formulario.__init__(self)
        self.setupUi(self)
        self.ConectarBotones()
        self.comboBox.setFocus()

    def ConectarBotones(self):
        self.btnAceptar.clicked.connect(self.Aceptar)
        self.btnCancelar.clicked.connect(self.Cancelar)

    def Cancelar(self):
        self.close()

    def Aceptar(self):
        self.lRetval, self.idUsuario = Usuarios.Usuario().ValidaContrasenia(self.comboBox.currentText(), self.txtPass.text())
        if not self.lRetval:
            Ventanas.showAlert("Error", u"Contraseña no valida")
            self.txtPass.setText("")
            self.txtPass.setFocus()
        else:
            GrabaConf("usuario", self.comboBox.currentText())
            GrabaConf("idUsuario", self.idUsuario)
            #print(self.comboBox.currentData())
            self.cUsuario = self.comboBox.currentText()
            self.hide()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(667, 188)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        #self.label = QtWidgets.QLabel(Dialog)
        self.label = Clases.Etiqueta(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAceptar = QtWidgets.QPushButton(Dialog)
        self.btnAceptar.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes/aceptar.bmp"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnAceptar.setIcon(icon)
        self.btnAceptar.setIconSize(QtCore.QSize(32, 32))
        self.btnAceptar.setFlat(False)
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout.addWidget(self.btnAceptar)
        self.btnCancelar = QtWidgets.QPushButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imagenes/log-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.btnCancelar.setIcon(icon1)
        self.btnCancelar.setIconSize(QtCore.QSize(32, 32))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        self.gridLayout.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        #self.txtPass = QtWidgets.QLineEdit(Dialog)
        self.txtPass = Clases.EntradaTexto(Dialog)
        self.txtPass.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.txtPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPass.setObjectName("txtPass")
        self.gridLayout.addWidget(self.txtPass, 6, 0, 1, 1)
        #self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2 = Clases.Etiqueta(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        #self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox = CboUsuario(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboBox, self.txtPass)
        Dialog.setTabOrder(self.txtPass, self.btnAceptar)
        Dialog.setTabOrder(self.btnAceptar, self.btnCancelar)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Usuario"))
        self.btnAceptar.setText(_translate("Dialog", "Aceptar"))
        self.btnCancelar.setText(_translate("Dialog", "Cancelar"))
        self.txtPass.setStatusTip(_translate("Dialog", "Contraseña del usuario"))
        self.txtPass.setPlaceholderText(_translate("Dialog", "Contraseña del usuario"))
        self.label_2.setText(_translate("Dialog", "Contraseña"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Login()
    #ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

