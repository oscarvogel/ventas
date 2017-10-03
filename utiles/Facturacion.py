# -*- coding: utf-8 -*-
from modelos import Articulo, TipoIva, Paramfac


class facturacion(object):

    lPrecioFinal = False
    nPrecioPub = 0.00

    def CalculaPrecio(self, idArticulo=1):

        nPrecio = 0.00

        cursor = Articulo.Articulo().BuscaPorCampoClave(idArticulo)
        cursoriva = TipoIva.tipoiva().BuscaPorCampoClave(cursor['TipoIva'])
        cursorparamfac = Paramfac.paramfac()\
            .Select()\
            .From()\
            .One()

        if cursor['PrecioPub'] != 0:
            nPrecio = cursor['PrecioPub']
            self.lPrecioFinal = True
        else:
            self.lPrecioFinal = False
            nPrecio = cursor['Precio1'] + cursor['Precio1'] * cursoriva['IVA'] / 100 +\
                cursor['Precio1'] * cursorparamfac['municipal'] / 100
        self.nPrecioPub = nPrecio

        return nPrecio

