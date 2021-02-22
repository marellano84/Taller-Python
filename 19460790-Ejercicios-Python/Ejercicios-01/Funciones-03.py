
a = int(input("Ingresa el primer valor: "))
b = int(input("Ingresa el segundo valor: "))


def relacion(a, b):
    if a > b:
        return 1   
    elif a < b:
        return -1
    elif a == b:
        return 0


print(relacion(a, b))
