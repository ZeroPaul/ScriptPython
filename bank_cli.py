#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def deposit():
    flag = True
    num = 0
    ye = 1
    yea = []
    mont = []
    while flag:
        num += 1
        money = input("(Año %s)(Mes %s) Monto a depositar: " % (ye,num,))

        if num <= 12:
            mont.append(int(money))

        if num == 12:
            ye += 1
            num = 0
            yea.append(mont)
            mont = []
            ey = input("desea continuar con una año mas ? si/no: ")
            if ey == "no":
                flag = False

    return yea

def bank_deposit(d_money):
    money_years = []
    counter = 0
    for m in d_money:
        counter += 1
        detail = {}
        only_year = 0
        f_interest = 0
        for d in m:
            only_year += d
        f_interest = only_year*0.1
        detail['yea'] = counter
        detail['money_total'] = only_year
        detail['fixed_interest'] = f_interest
        money_years.append(detail)
    print("Haciendo Cuentas Anuales")
    t_all = 0
    for a in money_years:
        print("Año(%s) total" % (a.get('yea')))
        print("___________________")
        print("Dinero ahorrado  : %s" % (a.get('money_total')))
        print("Interes fijo     : %s" % (a.get('fixed_interest')))
        t = int(a.get('money_total'))+int(a.get('fixed_interest'))
        t_all += t
        print("Total de dinero  : %s" % (t))
        print("")
        print("___________________")
    print("TOTAL DE DINERO      : %s" % (t_all))



save_money = deposit()
bank_deposit(save_money)
