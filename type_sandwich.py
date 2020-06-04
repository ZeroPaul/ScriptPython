

def invoice_sandwich():
    s = 0
    d = 0
    t = 0

    p = True

    while p:
        print("Elige tu sandwich")
        print("1. sandwich simple")
        print("2. sandwich doble")
        print("3. sandwich triple")
        c = input("sandwich: ")
        if c == 1:
            pass

        u = input("cuantos quieres:")

        print("deseas pedir mas sandwiches")
        o = input("si / no :")
        if o == "no":
            p = False
        else:
            p = True



# invoice_sandwich()

type_sandwich = ['simple', 'doble', 'triple']
# order = {}

def buy_sandwich(ts):
    o = {}
    for t in ts:
        o[t] = 0

    num = 0
    for i in ts:
        num += 1
        print("%s. sandwich %s | cantidad %s" % (num, i, o.get(i)))
    s = input("opcion: ")
    



buy_sandwich(type_sandwich)
