# -*- coding: utf-8 -*-
from db.SqlComandos import SQL


class Proveedor(SQL):
    tabla = 'proveedores'
    campoclave = 'idProveedor'