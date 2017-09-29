# coding=utf-8
from PyQt5.QtWidgets import QMessageBox


def showAlert(titulo, mensaje):

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(mensaje)
    msg.setWindowTitle(titulo)
    msg.setStandardButtons(QMessageBox.Ok)

    retval = msg.exec_()

    return retval