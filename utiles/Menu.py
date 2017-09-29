# -*- coding: utf-8 -*-
import functools

from PyQt5.QtWidgets import QAction

from modelos import Formula, Usuarios
from utiles.Funciones import LeerConf


class GeneraMenu(object):

    nIdSistema = 0
    nIdUsuario = 0
    ventana = None

    def __init__(self):
        pass

    def Carga(self):

        self.datos_menu = Formula.Formula()
        self.datos_menu.Select()
        self.datos_menu.From()

        if Usuarios.Usuario().IsAdmin(LeerConf('idUsuario')):
            self.datos_menu.Where({'formula.sis_id':self.nIdSistema})
        else:
            self.datos_menu.InnerJoin('accesos', 'for_id')
            self.datos_menu.Where({'accesos.usu_id':self.nIdUsuario, 'formula.sis_id':self.nIdSistema})

        self.datos_menu.WhereAnd({'formula.for_pare':0})
        data = self.datos_menu.All()
        for d in data:
            menubar = self.ventana.menuBar()
            fileMenu = menubar.addMenu(d['for_nomb'].strip())
            self.CargaHijos(d, fileMenu)

    def CargaHijos(self, d, fileMenu):
        hijos = self.datos_menu.Select()\
            .From()\
            .Where({'for_pare':d['for_id']}) \
            .OrderBy(['for_orde']) \
            .All()
        for h in hijos:
            if h['tfo_id'] == 5: #separador de menu
                fileMenu.addSeparator()
            else:
                subhijo = self.datos_menu.Select()\
                    .From()\
                    .Where({'for_pare':h['for_id']})\
                    .All()
                if subhijo:
                    fileSub = fileMenu.addMenu(h['for_nomb'].strip())
                    self.CargaHijos(h, fileSub)
                else:
                    menuAct = QAction(h['for_nomb'].strip(), self.ventana)
                    menuAct.setStatusTip(h['for_nomb'])
                    if h['tfo_id'] == 2:
                        #pass
                        menuAct.triggered.connect(eval('self.ventana.'+h['for_arch'].strip()))
                    else:
                        #pass
                        menuAct.triggered.connect(functools.partial(self.ventana.SeleccionaMenu, h['for_id'], h['for_arch']))
                    fileMenu.addAction(menuAct)

