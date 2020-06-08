#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def automovil_tax():
    cant_auto = int(input('cantidad de automoviles: '))
    type_key = 0
    price = 0
    tax = 0
    total_tax = 0
    for a in range(cant_auto):
        price = int(input('Costo del auto: '))
        type_key = int(input('Elige la clave 1/2/3: '))
        if type_key == 1:
            tax = price * 0.1
        elif type_key == 2:
            tax = price * 0.07
        elif type_key == 3:
            tax = price * 0.05
        total_tax += tax 
        print('Costo del automovil: {0}'.format(price))
        print('Impuesto del automovile: {0} (clave {1})'.format(tax, type_key))
        print('________________________________________')
    print('total impuestos a pagar: {0}'.format(total_tax))


automovil_tax()
