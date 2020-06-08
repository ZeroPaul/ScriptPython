#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def generate_table():
    num_base = int(input('ingrese el numero de la tabla a generar: '))
    num_cant =  int(input('ingrese el numero limite a generar: '))
    counter = 0
    
    print('Tabla del %s' % (num_base))
    for c in range(num_cant):
        counter += 1
        print('{0} x {1} = {2}'.format(num_base, counter, num_base * counter))

generate_table()

