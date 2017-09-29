# coding=utf-8
import sys

from PyQt5.QtWidgets import QApplication, QAction, qApp

from db.Conectar import ConectarDB
from utiles import Ventanas
from utiles.Funciones import LeerConf
from vistas.login import Login
from vistas.ppal import Ui_MainWindow
from utiles.Menu import GeneraMenu
from vistas.Ventas import Ui_Dialog

class Ventana(Ui_MainWindow):

    usuario = None
    idUsuario = None
    settings = None

    def __init__(self):
        Ui_MainWindow.__init__(self)
        print("Usuario {}".format(LeerConf("usuario")))
        ConectarDB().Iniciar()
        self.setWindowTitle("Sistema Ventas")
        self.showMaximized()

    def Login(self):
        ventana = Login()
        ventana.exec_()

        lRetorno = ventana.lRetval
        self.usuario = ventana.cUsuario

        print("Usuario {}".format(LeerConf("usuario")))
        ventana.close()
        return lRetorno

    def InitMenu(self):
        #Ui_MainWindow.InitMenu(self)
        menu = GeneraMenu()
        menu.nIdSistema = 7
        menu.nIdUsuario = LeerConf("idUsuario")
        menu.ventana = self
        menu.Carga()

    def SalirSistema(self):
        qApp.exit()

    def SeleccionaMenu(self, idMenu, Archivo):
        print("ID Menu {}".format(idMenu))
        if Archivo:
            ventana = eval(Archivo)
            #ventana = Ui_Dialog()
            ventana.exec_()
        else:
            Ventanas.showAlert("Error", u"Opcion de menu no establecida")

if __name__ == "__main__":
    # Instancia para iniciar una aplicación
    app = QApplication(sys.argv)
    # Crear un objeto de la clase
    _ventana = Ventana()
    # Mostra la ventana
    _ventana.show()
    if _ventana.Login():
        _ventana.InitMenu()
        # Ejecutar la aplicación
        sys.exit(app.exec_())