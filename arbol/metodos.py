inicio = None
raiz = None
reco = None
raiz = None
der = None
izq = None


def insertar():
    with open('prueba.txt', 'a') as f:
        clave = input("Ingresa la clave: ")
        curp = input("Ingresa la curp: ")
        nombre = input("Ingresa tu nombre: ")
        escolaridad = input("Ingresa nivel de estudios: ")
        ingreso = input("Ingresa el ingreso mensual: ")
        f.write(clave+","+nombre+","+curp+","+escolaridad+","+ingreso+"\n")


#insertar()


def recolectar():
    with open('prueba.txt', 'r') as f:
        lista = []
        for cad in f:
            lista = cad.split(',', 5)
            clave = lista[0]
            nombre = lista[1]
            curp = lista[2]
            escolaridad = lista[3]
            ingreso = lista[4]

    print(lista)
    print(clave)
    print(nombre)
    print(curp)
    print(escolaridad)
    print(ingreso)


#recolectar()


def arbol(curp):
    if raiz == None:
        raiz = curp
    else:
        padre = None
        reco = raiz
        while reco != None:
            padre = reco
            if curp < reco.curp:
                reco = reco.izq
            else:
                reco = reco.der
        if curp < padre.curp:
            padre.izq = curp
        else:
            padre.der = curp
