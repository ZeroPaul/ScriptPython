#!/usr/bin/env python3
# -*- coding: utf-8 -*-

type_sandwich = [['simple', 20], ['doble', 25], ['triple', 28], ['cuadruple', 30], ]
def buy_sandwich(ts):
    o = {}
    d = {}
    total = 0

    for t in ts:
        d['price'] = int(t[1])
        d['quantity'] = 0
        name_product = (t[0])
        o[name_product] = d
        d = {}

    p = True

    while p:
        num = 0
        print("Realize su orden")
        for product, detail in o.items():
            num += 1
            print(
                "%s. sandwich %s | cantidad %s" % 
                (num, product, detail.get('quantity'))
            )
        choice_number = input("opcion: ")
        order_quantity = input("cantidad: ")
        choice = ts[(int(choice_number)-1)]
        previous_quantity = o.get(choice[0]).get('quantity')
        o.get(choice[0])['quantity'] =  int(order_quantity) \
                                        + int(previous_quantity)

        print("deseas pedir mas sandwiches")
        op = input("si / no :")
        if op == "no":
            p = False
            print("Calculando pedido...")
        else:
            p = True
    
    print("______________________________________________________")
    print("El Nufrago Satisfecho!!!")
    print("Nota de Pedido")
    print("______________________________________________________")
    print("Cant. | Producto        | Precio Unit.  | Sub. Total")
    for pt, dl in o.items():
        if dl.get('quantity') > 0:
            st = int(dl.get('quantity')) * int(dl.get('price'))
            total += st
            print(" %s    sandwich %s     %s             %s" % 
                (dl.get('quantity'), pt, dl.get('price'), st)
            )
    print("______________________________________________________")
    print("                                 Total  |  %s" % (total))
    print("sin metodo de pago.")
    print("")
    payment_type = input("Modo de pago tarjeta(t)/efectivo(e): ")
    if payment_type == "t":
        tt = total*(5/100)
        total += tt
        print("Cobro Adicional")
        print("______________________________________________________")
        print("Metodo de Pago tarjeta                   |  %s" % (tt)) 
    elif payment_type == "e":
        tt = 0
        print("______________________________________________________")
        print("Metodo de Pago Efectivo                  |  %s" % (tt)) 

    print("______________________________________________________")
    print("                                  Total  |  %s" % (total))
    print("¡Gracias por su compra!")


type_sandwich = [['simple', 20], ['doble', 25], ['triple', 28], ['cuadruple', 30], ]
# type_sandwich = [['simple', 20], ['doble', 25], ['triple', 28], ]

buy_sandwich(type_sandwich)
