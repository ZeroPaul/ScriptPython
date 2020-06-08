#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def coin_master():

    coin_ten = input("Introduzca monedas de 10 pesos (cant.): ")
    coin_five = input("Introduzca monedas de 5 pesos (cant.): ")
    coin_one = input("Introduzca monedas de 1  pesos (cant.): ")

    bills_ten = input("Introduzca billetes de 10 pesos (cant.): ")
    bills_twn = input("Introduzca billetes de 20 pesos (cant.): ")
    bills_fiv = input("Introduzca billetes de 50 pesos (cant.): ")

    coin_ten = int(coin_ten) * 10
    coin_five = int(coin_five) * 5
    coin_one = int(coin_one) * 1

    bills_ten = int(bills_ten) * 10
    bills_twn = int(bills_twn) * 20
    bills_fiv = int(bills_fiv) * 50

    coins = coin_ten + coin_five + coin_one
    bills = bills_ten + bills_twn + bills_fiv

    print('total en monedas : {0} pesos'.format(coins))
    print('total en billetes : {0} pesos'.format(bills))
    print('total dinero : {0} pesos'.format(coins + bills))

coin_master()
