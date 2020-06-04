

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
        u = input("cuantos quieres:")

        print("deseas pedir mas sandwiches")
        o = input("si / no :")
        if o == "no":
            p = False
        else:
            p = True



invoice_sandwich()

