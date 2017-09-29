# coding=utf-8
from db.SqlComandos import SQL

class Cliente(SQL):
    tabla = "clientes"
    campoclave = "IDCLIENTE"

