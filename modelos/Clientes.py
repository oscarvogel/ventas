# coding=utf-8
from db.SqlComandos import SQL

class Cliente(SQL):
    tabla = "clientes"
    campoclave = "idCliente"

    def Discrimina(self, idCliente=1):
        lRetorno = False
        dato = self.BuscaPorCampoClave(idCliente)
        if dato:
            if dato['tiporesp'] == 1:
                lRetorno = True

        return lRetorno
