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
    ultimoId = 0

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
            if not data:
                print("Query {}".format(sql))
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

    def One(self):

        if not self.db:
            self.db = ConectarDB().GetDb()

        data = None
        cur = self.db.cursor(mdb.cursors.DictCursor)
        try:
            cur.execute(self.query)
            data = cur.fetchone()
        except mdb.Error as e:
            Ventanas.showAlert("Error", "Error al realizar la consulta {}".format(self.query))

        return data

    def Limit(self, limite=50):
        self.query += " limit {}".format(limite)

        return self

    def Like(self, condiciones=None):

        if self.query.upper().find("WHERE") != -1:
            self.query += " and ".join(k + " like '%{}%' ".format(v) for k, v in condiciones.items())
        else:
            self.query += " where "
            self.query += " and ".join(k + " like '%{}%' ".format(v) for k, v in condiciones.items())

        return self

    def Insertar(self, fields, graba=False):
        sql = 'insert into ' + self.tabla + '('
        sql += ', '.join(d for d in fields)
        sql += ') values('
        sql += ','.join('%s' for d in fields)
        sql += ')'
        params = [d for d in fields.values()]

        self.query = sql
        if graba:
            if not self.db:
                self.db = ConectarDB().GetDb()
            cur = self.db.cursor(mdb.cursors.DictCursor)

            try:
                cur.execute(sql, params)
                cur.execute("SELECT LAST_INSERT_ID() as ultimo")
                data = cur.fetchone()
                self.ultimoId = data['ultimo']
            except mdb.Error as e:
                Ventanas.showAlert("Error", "Error al insertar en {} sentencia {}".format(self.tabla, self.query))

        return sql, params

    def Actualizar(self, fields, key, graba=False):

        query = 'update ' + self.tabla + ' set '
        query += ', '.join(d + ' = %s' for d in fields.keys() if d != key)
        query += ' where {} = %s'.format(key)
        params = []
        for k in fields.keys():
            if k != key:
                params.append(self.Expand(fields, k))

        params.append(fields[key])
        self.query = query

        if graba:
            if not self.db:
                self.db = ConectarDB().GetDb()
            cur = self.db.cursor(mdb.cursors.DictCursor)
            try:
                cur.execute(query, params)
            except mdb.Error as e:
                Ventanas.showAlert("Error", "Error al actualizar en {} sentencia {}".format(self.tabla, self.query))

        return query, params

    def Expand(self, fields, k):
        if not self.db:
            self.db = ConectarDB().GetDb()

        cur = self.db.cursor(mdb.cursors.DictCursor)
        sql = "DESCRIBE {} {}".format(self.tabla, k.upper())
        data = cur.execute(sql)
        if fields[k] is None:
            if data['Type'].startswith('date'):
                retvalue = '00000000'
            elif k.upper().startswith('_FECHA') \
                    or k.upper().startswith('ULAC'):
                retvalue = '00000000'
            else:
                retvalue = fields[k]
        else:
            retvalue = fields[k]

        return retvalue

    def __str__(self):

        return self.query
