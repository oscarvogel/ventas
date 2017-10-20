import os
from configparser import ConfigParser

from PyQt5 import QtGui
from os.path import join
from sys import argv

from PyQt5.QtCore import QSettings

EMPRESA = "servin"
SISTEMA = "sistema"

def GrabaConf(clave=None, valor=None):

    settings = QSettings(EMPRESA, SISTEMA)
    if clave:
        settings.setValue(clave, valor)

def LeerConf(clave=None):
    settings = QSettings(EMPRESA, SISTEMA)
    if clave:
        cValorRetorno = settings.value(clave)
    else:
        cValorRetorno = None

    return cValorRetorno

def BorrarConf(clave=None):
    settings = QSettings(EMPRESA, SISTEMA)
    if clave:
        settings.remove(clave)
    else:
        settings.clear()


def ubicacion_sistema():
    cUbicacion = LeerConf("InicioSistema") or os.path.dirname(argv[0])

    return cUbicacion

def imagen(archivo):
    archivoImg = ubicacion_sistema() + join("imagenes", archivo)
    if os.path.exists(archivoImg):
        return archivoImg
    else:
        return ""


def icono_sistema():

    cIcono = QtGui.QIcon(imagen("market.ico"))

    return cIcono


def LeerIni(clave=None):
    retorno = ''
    Config = ConfigParser()

    Config.read(ubicacion_sistema() + "servin.ini")
    retorno = Config.get('param', clave)

    return retorno
