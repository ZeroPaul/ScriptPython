#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ex_cube():
    numbers = []
    flag = True
    while flag:
        number_cube = input(
            'Ingrese numeros positivos enteros o (x) para terminar: '
        )
        
        if number_cube == 'x':
            flag = False
        else:
            numbers.append(int(number_cube))

    print('Calculando el Cubo ;)')
    for n in numbers:
        print('{0} al cubo es {1}'.format(n, n**3))

ex_cube()
