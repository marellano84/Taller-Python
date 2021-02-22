import metodos as m 
print("1. Ingresar nuevo registro")
print("2. Mostrar registros en el archivo")
opcion = input("Digite su elección: ")

if int(opcion) == 1:
    m.insertar()
else:
    m.recolectar()