#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def counter_quantities():
    list_number = []
    flag = True
    while flag:
        print("Para dejar de introducir numero escriba (x)")
        numb_inp = input("Introduce un numero:")
        if numb_inp == "x":
            flag = False
        elif type(int(numb_inp)) == int:
            list_number.append(numb_inp)
    
    equal_counter = 0
    less_counter = 0
    greater_counter = 0
    
    for numb in list_number:
        if int(numb) == 0:
            equal_counter += 1
        elif int(numb) > 0:
            greater_counter += 1
        elif int(numb) < 0:
            less_counter += 1

    print(list_number)
    print("_________________________________")
    print("")
    print("            Details")
    print("_________________________________")
    print("")
    print("menores a cero: %s" % (less_counter))
    print("iguales a cero: %s" % (equal_counter))
    print("mayores a cero: %s" % (greater_counter))
    print("_________________________________")

counter_quantities()
