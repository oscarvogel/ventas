# coding=utf-8
from db.SqlComandos import SQL


class Usuario(SQL):

    tabla = 'usuarios'
    campo = 'usuario'
    campoclave = 'usu_id'

    def ValidaContrasenia(self, usuario = '', password = ''):

        lRetorno = False
        idUsuario = None
        cursor = SQL().BuscaUno(self.tabla, self.campo, usuario)

        if cursor['CLAVE'].strip() == password.upper().strip():
            lRetorno = True
            idUsuario = cursor['USU_ID']

        return lRetorno, idUsuario

    def IsAdmin(self, idUsuario = 1):

        lRetorno = False
        data = self.BuscaUno(valorbuscado=idUsuario)

        if data:
            if data['USER_LEVEL'] == '01':
                lRetorno = True

        return lRetorno
