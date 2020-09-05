from clientes2 import *
from prestamos2 import *
from busquedas import *
from AclientesExcel import *
import os

def Main():
    ver_menu = True
    opcion = "0"
    while (opcion != "4"):
        print("\n\t\tMenú Principal\n")
        print("1.- Clientes")
        print("2.- Préstamos")
        print("3.- Búsquedas")
        print("4.- Salir\n")
        opcion = input("Ingrese una opción: ")
        if (opcion == "1"):
            os.system("cls")
            Clientes()
            os.system("pause")
            os.system("cls")
        elif (opcion == "2"):
            os.system("cls")
            Prestamos()
            os.system("pause")
            os.system("cls")
        elif (opcion == "3"):
            os.system("cls")
            Busquedas()
            os.system("pause")
            os.system("cls")
        elif (opcion == "4"):
            print("\nRegrese pronto")
            os.system("pause")
            exit()
            ver_menu = False
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Clientes():
    ver_menu = True
    opcion = "0"
    while (opcion != "4"):
        print("\n\tMenú de clientes\n")
        print("1.- Nuevo cliente")
        print("2.- Editar cliente")
        print("3.- Eliminar cliente")
        print("4.- Regresar\n")
        opcion = input("Ingrese una opción: ")
        if (opcion == "1"):
            os.system("cls")
            CrearCliente()
            os.system("pause")
            os.system("cls")
        elif (opcion == "2"):
            os.system("cls")
            ActualizarCliente()
            os.system("pause")
            os.system("cls")
        elif (opcion == "3"):
            os.system("cls")
            EliminarCliente()
            os.system("pause")
            os.system("cls")
        elif (opcion == "4"):
            ver_menu = False
            os.system("cls")
            Main()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Prestamos():
    ver_menu = True
    opcion = "0"
    while (opcion != "4"):
        print("\n\tMenú de préstamos\n")
        print("1.- Dar un préstamo")
        print("2.- Abonar al préstamo")
        print("3.- Ver préstamos")
        print("4.- Regresar\n")
        opcion = input("Ingrese una opción: ")
        if (opcion == "1"):
            os.system("cls")
            CrearPrestamo()
            os.system("pause")
            os.system("cls")
        elif (opcion == "2"):
            os.system("cls")
            AbonarPrestamo()
            os.system("pause")
            os.system("cls")
        elif (opcion == "3"):
            os.system("cls")
            VerPrestamos()
            os.system("pause")
            os.system("cls")
        elif (opcion == "4"):
            ver_menu = False
            os.system("cls")
            Main()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Busquedas():
    ver_menu = True
    opcion = "0"
    while (opcion != "4"):
        print("\n\tMenú de búsquedas\n")
        print("1.- Clientes")
        print("2.- Préstamos")
        print("3.- Dinero")
        print("4.- Regresar\n")
        opcion = input("Ingrese una opción: ")
        if (opcion == "1"):
            os.system("cls")
            Busqueda_Clientes()
            os.system("pause")
            os.system("cls")
        elif (opcion == "2"):
            os.system("cls")
            Busqueda_Prestamos()
            os.system("pause")
            os.system("cls")
        elif (opcion == "3"):
            os.system("cls")
            Busqueda_Dinero()
            os.system("pause")
            os.system("cls")
        elif (opcion == "4"):
            ver_menu = False
            os.system("cls")
            Main()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Busqueda_Clientes():
    ver_menu = True
    op = "0"
    while (op != "6"):
        print("\n\tMenú búsqueda de clientes\n")
        print("1.- Todos")
        print("2.- Activos")
        print("3.- Inactivos")
        print("4.- Por nombre")
        print("5.- Por id")
        print("6.- Regresar\n")
        op = input("Ingrese una opción: ")
        if (op == "1"):
            os.system("cls")
            ClientesTodos()
            os.system("pause")
            os.system("cls")
        elif (op == "2"):
            os.system("cls")
            ClientesActivos()
            os.system("pause")
            os.system("cls")
        elif (op == "3"):
            os.system("cls")
            ClientesInactivos()
            os.system("pause")
            os.system("cls")
        elif (op == "4"):
            os.system("cls")
            ClientesPorNombre()
            os.system("pause")
            os.system("cls")
        elif (op == "5"):
            os.system("cls")
            ClientesPorId()
            os.system("pause")
            os.system("cls")
        elif (op == "6"):
            ver_menu = False
            os.system("cls")
            Busquedas()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Busqueda_Prestamos():
    ver_menu = True
    op = "0"
    while (op != "6"):
        print("\n\tMenú búsqueda de prestamos\n")
        print("1.- Todos")
        print("2.- Por id cliente")
        print("3.- Por fecha")
        print("4.- Activos")
        print("5.- Pagados")
        print("6.- Regresar\n")
        op = input("Ingrese una opción: ")
        if (op == "1"):
            os.system("cls")
            PrestamosTodos()
            os.system("pause")
            os.system("cls")
        elif (op == "2"):
            os.system("cls")
            PrestamosPorIdCliente()
            os.system("pause")
            os.system("cls")
        elif (op == "3"):
            os.system("cls")
            PrestamosPorFecha()
            os.system("pause")
            os.system("cls")
        elif (op == "4"):
            os.system("cls")
            PrestamosActivos()
            os.system("pause")
            os.system("cls")
        elif (op == "5"):
            os.system("cls")
            PrestamosPagados()
            os.system("pause")
            os.system("cls")
        elif (op == "6"):
            ver_menu = False
            os.system("cls")
            Busquedas()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

def Busqueda_Dinero():
    ver_menu = True
    op = "0"
    while (op != "3"):
        print("\n\tMenú búsqueda de dinero\n")
        print("1.- Monto total en el banco")
        print("2.- Cliente con más dinero")
        print("3.- Regresar\n")
        op = input("Ingrese una opción: ")
        if (op == "1"):
            os.system("cls")
            MontoTotal()
            os.system("pause")
            os.system("cls")
        elif (op == "2"):
            os.system("cls")
            ValorMaximo()
            os.system("pause")
            os.system("cls")
        elif (op == "3"):
            ver_menu = False
            os.system("cls")
            Busquedas()
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            os.system("pause")
            os.system("cls")

Main()