
def menu():
    bandera = False
    num = 0
    while not bandera:
        try:
            num= int(input("Introduzca la opcion seleccionada "))
            bandera = True
        except ValueError:
            print("Valor ingresado invalido, ingrese un digito ")
    return num
def ingresarCant(mensaje):
    dato = int(input(mensaje))
    return dato
def ingresarNombre(mensaje):
    nombre = input(mensaje)
    return nombre
def multiplicacion(var1,var2):
    return var1 * var2

salir = False
while not salir:
    print("Bienvenido(a) al sistema de inventario")
    print("1. Ingresar inventario")
    print("2. Sacar de inventario")
    print("3. Editar inventario")
    print("4. Listado de inventario/ Busqueda")
    print("5. Salir")

    print("Elija una opcion ")
    opcion= menu()
    if opcion == 1:
        cantprod = ingresarCant("Ingrese la cantidad de productos a procesar ")
        cont = 1
        producto = []
        cantidad = []
        precio = []
        total = []
        while cantprod >= cont:
            nomprod = ingresarNombre("Ingrese el nombre del producto ")
            producto.append(nomprod)
            var1 = ingresarCant("Ingrese la cantidad de productos a ingresar ")
            cantidad.append(var1)
            var2 = ingresarCant("Ingrese el precio unitario ")
            precio.append(var2)
            totalprod = multiplicacion(var1, var2)
            total.append(totalprod)
            cont += 1
        ind = 1
        for productos in producto:
            print("Producto:", productos, ". Cantidad:", cantidad[ind], ". Precio:",precio[ind], ". Total: ",total[ind])
            ind += 0

    elif opcion == 2:
        print("Opcion 2")
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 5:
        salir= True
    else:
        print("Introduzca un valor entre 1 y 5")
print("Fin")
