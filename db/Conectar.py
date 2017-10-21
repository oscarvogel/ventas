# coding=utf-8
import pymysql, sys

from utiles.Funciones import LeerIni

pymysql.install_as_MySQLdb()

import MySQLdb as mdb

class ConectarDB(object):

    servidor = LeerIni("ServerDB") or '192.168.0.200'
    basedatos = LeerIni("BaseDatos")
    usuario = 'root'
    password = 'fasca'
    puerto = 3306
    global db

    def Iniciar(self):
        # Establecer conexión a la base de datos MySql
        global db
        try:
            db = mdb.connect(host=self.servidor,
                             user=self.usuario,
                             passwd=self.password,
                             db=self.basedatos,
                             port=self.puerto,
                             charset='utf8')
        except mdb.Error as e:
            print ("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    def GetDb(self):
        global db
        if not db:
            self.Iniciar()

        return db

