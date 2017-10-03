# coding=utf-8
from db.SqlComandos import SQL

class Articulo(SQL):

    campoclave = 'idArticulo'
    tabla = 'articulos'

    def ModificaPrecios(self, valorbuscado=''):
        lRetorno = False

        cursor = self.BuscaPorCampoClave(valorbuscado)
        if cursor['ModificaPrecios'] == b'\x01':
            lRetorno = True

        return lRetorno
