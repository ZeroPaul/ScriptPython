#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sale_land():
    sale_year = 1961
    now_year = 2020

    price_sale = 1500
    cant_year = now_year - sale_year
    percent_year = 1500 * 0.15
    percent_total = cant_year * percent_year
    print('________________________________________________________')
    print('Año de venta ({0})/ Año Actual ({1}) | Cantidad de años({2})'.format(
                sale_year, now_year, cant_year
                ))
    print('Pago del 15 % de (${0}) en los ({1}) años '.format(price_sale,
    cant_year))
    print('Inversion total sin el dinero inicial (${0})'.format(percent_total))

sale_land()



