from PyQt5.QtCore import QSettings

EMPRESA = "servinlgsm"
SISTEMA = "aberturas"

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
