
numeros = [8, 1, 6, 17, 9, 14, 10, 3]


def separar(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    pares.sort()
    impares.sort()
    print(pares)
    print(impares)


separar(numeros)

