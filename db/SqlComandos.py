# coding=utf-8
import pymysql

from utiles import Ventanas
from .Conectar import ConectarDB
pymysql.install_as_MySQLdb()

import MySQLdb as mdb

class SQL(object):

    db = None
    tabla, campo, campoclave = None, None, None
    query = ''

    def Existe(self, valorbuscado = ''):

        if not self.db:
            self.db = ConectarDB().GetDb()
        lRetorno = False
        try:
            if self.BuscaUno(valorbuscado=valorbuscado):
                lRetorno = True
        except mdb.Error as e:
            Ventanas.showAlert("Error", e.args[0])

        return lRetorno

    def BuscaUno(self, tabla = '', campo = '', valorbuscado = ''):

        data = None

        if not tabla:
            tabla = self.tabla

        if not campo:
            campo = self.campoclave

        if not self.db:
            self.db = ConectarDB().GetDb()
        sql = """
            select *
                from {}
                where {} = '{}'
        """.format(tabla, campo, valorbuscado)
        cur = self.db.cursor(mdb.cursors.DictCursor)

        try:
            cur.execute(sql)
            data = cur.fetchone()
        except mdb.Error as e:
            Ventanas.showAlert("Error", sql)
        return data

    def BuscaTodo(self, tabla = '', cOrden = None, cFiltro = None, limite = None, campos = None):
        data = None
        if not self.db:
            self.db = ConectarDB().GetDb()

        if not tabla:
            tabla = self.tabla

        if campos:
            sql = "select "
            sql += " ,".join(k for k in campos)
            sql += " from {}".format(tabla)
        else:
            sql = """
                select *
                    from {}
            """.format(tabla)

        if cFiltro:
            sql += " where {}".format(cFiltro)

        if cOrden:
            sql += " order by {}".format(cOrden)

        if limite:
            sql += " limit {}".format(limite)

        cur = self.db.cursor(mdb.cursors.DictCursor)
        try:
            cur.execute(sql)
            data = cur.fetchall()
        except mdb.Error as e:
            print(sql)
            #Ventanas.showAlert("Error", e.args[0])
        return data

    """
    Busca por campo clave, debe estar establecido el campo clave
    """
    def BuscaPorCampoClave(self, valorbuscado=None):

        if not self.db:
            self.db = ConectarDB().GetDb()
        data = None
        try:
            data = self.BuscaUno(campo=self.campoclave, valorbuscado=valorbuscado)
        except mdb.Error as e:
            Ventanas.showAlert("Error", e.args[0])

        return data

    def Select(self, campos=None):
        if campos:
            self.query = "select "
            self.query += ', '.join(d for d in campos)
        else:
            self.query = "select * "
        return self

    def From(self, tabla=''):
        if tabla:
            self.query += " from {}".format(tabla)
        else:
            self.query += " from {}".format(self.tabla)
        return self

    def Where(self, condiciones=None):

        if condiciones:
            self.query += " where "
            self.query += " and ".join(k + " = {} ".format(v) for k, v in condiciones.items())
        return self

    def All(self):

        if not self.db:
            self.db = ConectarDB().GetDb()
        data = None
        cur = self.db.cursor(mdb.cursors.DictCursor)
        try:
            cur.execute(self.query)
            data = cur.fetchall()
        except mdb.Error as e:
            Ventanas.showAlert("Error", "Error al realizar la consulta " + self.query)
        return data

    def InnerJoin(self, related_table=None, relation=None):

        self.query += " inner join " + related_table + \
            " on " + self.tabla + "." + self.campoclave + \
                      " = " + related_table + "." + relation
        return self

    def WhereAnd(self, condiciones=None):

        self.query += " and "
        self.query += " and ".join(k + " = {} ".format(v) for k, v in condiciones.items())
        return self

    def WhereOr(self, condiciones=None):

        self.query += " or "
        self.query += " or ".join(k + " = {} ".format(v) for k, v in condiciones.items())
        return self

    def OrderBy(self, orders=None):
        self.query += " ORDER BY "
        self.query += " , ".join(k for k in orders)

        return self