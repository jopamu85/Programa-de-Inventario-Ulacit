import pandas as pd
import numpy as np
import csv



producto = []
cantidad = []
precio = []
total = []
inventario = {"Producto": producto, "Cantidad": cantidad, "Precio": precio, "Total": total}



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
    bandera = False
    while not bandera:
        try:
            dato = int(input(mensaje))
            bandera = True
        except ValueError:
            print("Valor ingresado no esta correcto, intente de nuevo")
    return dato
def ingresarNombre(mensaje):
    nombre = input(mensaje)
    return nombre
def multiplicacion(var1,var2):
    return var1 * var2
def busqueda(mensaje):
    bandera1 = False
    while not bandera1:
        try:
            elemenbus= producto.index(input(mensaje))
            bandera1 = True
        except ValueError:
            print("El producto ingresado no se encuentra en la lista, verifique el producto en inventario e intente de nuevo")
    return elemenbus
def resta(var1, var2):
    return var1 - var2

salir = False
while not salir:
    print("Bienvenido(a) al sistema de inventario")
    print("Creado por Jose Pablo Muñoz, Emanuel Blanco y Laura Vargas")
    print("1. Ingresar inventario")
    print("2. Sacar de inventario")
    print("3. Editar inventario")
    print("4. Listado de inventario/ Busqueda")
    print("5. Salir")

    print("Elija una opcion ")
    opcion = menu()
    if opcion == 1:
        print("Ingreso de inventario")
        cantprod = ingresarCant("Ingrese la cantidad de productos a procesar ")
        cont = 1
        while cantprod >= cont:
            nomprod = ingresarNombre("Ingrese el nombre del producto ")
            if nomprod not in producto:
                producto.append(nomprod)
                var1 = ingresarCant("Ingrese la cantidad de productos a ingresar ")
                cantidad.append(var1)
                var2 = ingresarCant("Ingrese el precio unitario ")
                precio.append(var2)
                totalprod = multiplicacion(var1, var2)
                total.append(totalprod)
            else:
                prodagre = producto.index(nomprod)
                cantagre = cantidad[prodagre] + ingresarCant("Ingrese la cantidad a adicionar")
                cantidad[prodagre] = cantagre
                totalprod = cantagre * precio[prodagre]
                total[prodagre] = totalprod
            cont +=1
            ind = 0
        print(pd.DataFrame(inventario))

    elif opcion == 2:
        print("Salida de inventario")
        retprod = busqueda("Ingrese el nombre del producto a retirar ")
        retcant = ingresarCant("Cuantos productos desea retirar? ")
        var1 = cantidad[retprod]
        var2 = retcant
        resresta = resta(var1, var2)
        cantidad[retprod] = resresta
        nuevprecio = precio[retprod]*resresta
        total[retprod] = nuevprecio
        ind = 0
        print(pd.DataFrame(inventario))

    elif opcion == 3:
        salir2 = False
        while not salir2:
            print("Menu de edicion de inventario")
            print("Indique el valor que desea editar")
            print("1. Nombre")
            print("2. Cantidad")
            print("3. Precio unitario")
            print("4. Salir Edicion de productos")

            print("Elija una opcion ")
            opcion2 = menu()

            if opcion2 == 1:
                editprod = busqueda("Indique cual producto desea editar ")
                edicnombre = ingresarNombre("Indique el nuevo nombre ")
                producto[editprod] = edicnombre
                ind = 0
                print(pd.DataFrame(inventario))
            elif opcion2 == 2:
                editprod = busqueda("Indique cual producto desea editar ")
                ediccant = ingresarCant("Indique la nueva cantidad ")
                cantidad[editprod] = ediccant
                nuevtotal = cantidad[editprod] * precio[editprod]
                total[editprod] = nuevtotal
                ind = 0
                print(pd.DataFrame(inventario))
            elif opcion2 == 3:
                editprod = busqueda("Indique cual producto desea editar ")
                edicprec = ingresarCant("Indique el nuevo precio ")
                precio[editprod] = edicprec
                nuevtotal = cantidad[editprod] * precio[editprod]
                total[editprod] = nuevtotal
                ind = 0
                print(pd.DataFrame(inventario))
            elif opcion2 == 4:
                salir2 = True
            else:
                print("Introduzca un valor entre 1 y 4")

    elif opcion == 4:
        salir3 = False
        while not salir3:
            print("Menu de listado / busqueda de inventario")
            print("Indique la funcion que desea seleccionar")
            print("1. Busqueda de producto en inventario")
            print("2. Listado de inventario")
            print("3. Salir de listado / busqueda de inventario")

            print("Seleccione una opcion")
            opcion3 = menu()
            if opcion3 == 1:
                opbusqueda = busqueda("Ingrese el nombre del producto a buscar ")
                print("Producto:", producto[opbusqueda], ". Cantidad", cantidad[opbusqueda], ". Precio unitario", precio[opbusqueda], ". Total", total[opbusqueda])
            elif opcion3 ==2:
                ind = 0
                print(pd.DataFrame(inventario))
            elif opcion3 == 3:
                salir3 = True
            else:
                print("Introduzca un valor entre 1 y 3")
    elif opcion == 5:
        df = pd.DataFrame(inventario)
        df.to_csv("inventario.csv")
        salir= True
    else:
        print("Introduzca un valor entre 1 y 5")
print("Gracias por utilizar el programa de inventario")

