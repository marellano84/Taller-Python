import math
figuras = []

def crear_cuadrado(lado):
    cuadrado = {}
    def area_cuadrado(lado):
        a = lado*lado
        return a

    def perimetro_cuadrado(lado):
        p = lado*4
        return p

    cuadrado.update({"Tipo": "Cuadrado", "Area": area_cuadrado(lado), "Perimetro": perimetro_cuadrado(lado)})
    lista_figuras(cuadrado)

def crear_triangulo(lado_a, lado_b, lado_c):
    triangulo = []
    a, b, c = lado_a, lado_b, lado_c
    medidas = [a, b, c]
    for i in medidas:
        menor = medidas[0]
        for x in range(1, 3):
            if medidas[x] < menor:
                menor = medidas[x]
            base = menor

    """
    if a == b and b == c:
        tipo = "equilatero"
    elif a == b or a == c or b == c:
        tipo = "isoceles"
    elif a != b or a != c or b != c:
        tipo = "escaleno"
    """
    
                
    def area_equilatero(a, b, c):
        #global base
        altura = (math.sqrt(3)*a)/2
        area = (base*altura)/2
        return area
    
    def per_equilatero(a, b, c):
        per = a*3
        return per

    def area_isoceles(a, b, c):
        altura = math.sqrt((math.pow(a, 2)-math.pow(b, 2))/4)
        area = (b*altura)/2
        return area
    
    def per_isoceles(a, b, c):
        per = a+b+c
        return per
    
    def area_escaleno(a, b, c):
        sp = (a+b+c)/2
        area = math.sqrt(sp*(sp-a)*(sp-b)*(sp-c))
        return area

    def per_escaleno(a, b, c):
        per = a+b+c
        return per

    def selector(tipo):
        if tipo == "equilatero":
            area_equilatero(a, b, c)
            per_equilatero(a, b, c)
            triangulo.append({"Tipo": "Triangulo Equilatero", "Area": area_equilatero(a, b, c), "Perimetro": per_equilatero(a, b, c)})
        elif tipo == "isoceles":
            area_isoceles(a, b, c)
            per_isoceles(a, b, c)
            triangulo.append({"Tipo": "Triangulo Isoceles", "Area": area_isoceles(a, b, c), "Perimetro": per_isoceles(a, b, c)})
        elif tipo == "escaleno":
            area_escaleno(a, b, c)
            per_escaleno(a, b, c)
            triangulo.append({"Tipo": "Triangulo Escaleno", "Area": area_escaleno(a, b, c), "Perimetro": per_escaleno(a, b, c)})

    if a == b and b == c:
        tipo = "equilatero"
        selector(tipo)
    elif a == b or a == c or b == c:
        tipo = "isoceles"
        selector(tipo)
    elif a != b or a != c or b != c:
        tipo = "escaleno"
        selector(tipo)

    """
    equilatero = {"Tipo": "Triangulo Equilatero", "Area": area_equilatero(a, b, c), "Perimetro": per_equilatero(a, b, c)}
    isoceles = {"Tipo": "Triangulo Isoceles", "Area": area_isoceles(a, b, c), "Perimetro": per_isoceles(a, b, c)}
    escaleno = {"Tipo": "Triangulo Equilatero", "Area": area_escaleno(a, b, c), "Perimetro": per_escaleno(a, b, c)}
    """

    lista_figuras(triangulo)

def crear_circulo(radio):
    def area_circulo(radio):
        area = math.pi*(math.pow(radio, 2))
        return area

    def per_circulo(radio):
        per = 2*math.pi*radio
        return per

    circulo = {"Tipo": "Circulo", "Area": area_circulo(radio), "Perimetro": per_circulo(radio)}
    lista_figuras(circulo)

def lista_figuras(insercion):
    global figuras
    figuras.append(insercion)

def mostrar_figuras():
    #opcion = input("Que categoria de figuras desea mostrar? ")
    if len(figuras) == 0:
        print("No hay nada por aqui! ")
    else:
        print(figuras)


def menu_figuras():
    print("1.- Cuadrado\t2.- Triangulo\t 3.- Circulo")
    opcion = float(input("Ingresa la opcion deseada: "))
    if opcion == 1:
        lado = float(input("Ingresa el valor para 'lado': "))
        crear_cuadrado(lado)
    elif opcion == 2:
        lado_a, lado_b, lado_c = float(input("ingresa el lado 'a': ")), float(
            input("ingresa el lado 'b': ")), float(input("ingresa el lado 'c': "))
        crear_triangulo(lado_a, lado_b, lado_c)
    elif opcion == 3:
        radio = float(input("Ingresa el valor del radio: "))
        crear_circulo(radio)



def main():
    op = ""
    while op != 0:
        print("1.- Crear Figura")
        print("2.- Listar una clasificacion de figuras")
        print("3.- Listar todas las figuras")
        print("4.- Mostrar suma de todas las areas")
        print("5.- Mostrar la suma de todos los perimetros")
        print("6.- Limpiar lista")
        print("0.- Salir")
        op = int(input("Ingresa la opcion deseada: "))
        if op == 1:
            menu_figuras()   
        elif op == 2:
            mostrar_figuras()   
        #elif op == 3:
        #elif op == 4:
        #elif op == 5:
        #elif op == 6:
        elif op == 0:
            break

main()