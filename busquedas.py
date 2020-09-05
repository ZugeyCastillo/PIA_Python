from clases2 import *
from AclientesExcel import ClientesExcel
from prestamosExcel2 import PrestamosExcel

clientesExcel = ClientesExcel()
validaciones = Validaciones()
prestamosExcel = PrestamosExcel()

# Busquedas de prestamos
def PrestamosTodos():

    print("\n\t\t\t\tClientes del banco con préstamos\n")
    print(prestamosExcel.LeerPrestamos())
    print("\n")

def PrestamosPorIdCliente():

    print("\n\t\t\t\tBúsqueda de clietes con préstamos por ID")
    clienteId = input("\nIngrese el Id del cliente que desea consultar: ")

    while not validaciones.validarNumerosInts(clienteId):
        clienteId = input("Introduzca un id válido: ")
    clienteId = int(clienteId)
    print("\n\t\t\t\tInformación del cliente\n")

    if clientesExcel.LeerClientesId(clienteId).empty:
        print("\nNo existe cliente.")
    else:
        cliente = Cliente()
        cliente = clientesExcel.LeerClienteObjeto(clienteId)

        if cliente.Estatus == 0:
            print("\nEl cliente ha sido eliminado previamente.\n")
            
        print(clientesExcel.LeerClientesId(clienteId))
        resultados = prestamosExcel.LeerPrestamosCliente(clienteId)

        if resultados.empty:
            print("\nEl cliente no tiene préstamos.")
        else:
            print("\n\t\t\t\tPréstamos del cliente\n")
            print(resultados)
            print("\n")

def PrestamosPorFecha():

    print("\n\t\t\t\tBúsqueda de clietes con préstamos por fecha")
    fechaInicial = input("\nIngrese la fecha inicial (aaaa-mm-dd): ")

    while not validaciones.validarFecha(fechaInicial):
        fechaInicial = input("Introduzca un fecha inicial válida (aaaa-mm-dd): ")
    fechaInicial = str(fechaInicial)


    fechaFinal = input("Ingrese la fecha final (aaaa-mm-dd): ")

    while not validaciones.validarFecha(fechaFinal):
        fechaFinal = input("Introduzca un fecha final válida (aaaa-mm-dd): ")
    fechaFinal = str(fechaFinal)

    resultados = prestamosExcel.LeerPrestamosFecha(fechaInicial, fechaFinal)

    if resultados.empty:
        print("\nNo se encontraron resultados.")
    else:
        print("\n\t\t\t\tClientes del banco con préstamos\n")
        print(resultados)
        print("\n")

def PrestamosActivos():

    print("\n\t\t\t\tClietes con préstamos activos\n")
    print(prestamosExcel.LeerPrestamosActivos())
    print("\n")

def PrestamosPagados():

    print("\n\t\t\t\tClietes con préstamos pagados\n")
    print(prestamosExcel.LeerPrestamosPagados())
    print("\n")

# Busquedas de clientes
def ClientesTodos():

    print("\n\t\t\t\tClientes del banco\n")
    print(clientesExcel.LeerClientes())
    print("\n")

def ClientesActivos():

    print("\n\t\t\t\tClientes activos del banco\n")
    print(clientesExcel.LeerClientesActivos())
    print("\n")

def ClientesInactivos():

    print("\n\t\t\t\tClientes eliminados del banco\n")
    print(clientesExcel.LeerClientesInactivos())
    print("\n")

def ClientesPorId():

    print("\n\t\t\t\tBúsqueda de clientes por ID")
    clienteId = input("\nIngrese el Id del cliente que desea buscar: ")

    #------------------------------------------------------------
    while not validaciones.validarNumerosInts(clienteId):
        clienteId = input("Introduzca un id válido: ")
    clienteId = int(clienteId)

    if clientesExcel.LeerClientesId(clienteId).empty:
        print("\nNo existe cliente.")
    else:
    #------------------------------------------------------------
        cliente = Cliente()
        cliente = clientesExcel.LeerClienteObjeto(clienteId)

        if cliente.Estatus == 0:
            print("\nEl cliente ha sido eliminado previamente.")

        print("\n\t\t\t\tCliente del banco\n")
        print(clientesExcel.LeerClientesId(clienteId))
        print("\n")

def ClientesPorNombre():

    print("\n\t\t\t\tBúsqueda de clientes por nombre")
    clienteNombre = input("\nIngrese el Nombre del cliente que desea buscar: ")

    #------------------------------------------------------------
    while not validaciones.validarCadena(clienteNombre):
        clienteNombre = input("Introduzca un nombre válido: ")
    clienteNombre = str(clienteNombre)

    resultados = clientesExcel.LeerClientesNombre(clienteNombre)

    if resultados.empty:
        print("\nNo se encontraron resultados.")
    else:
    #------------------------------------------------------------
        print("\n\t\t\t\tClientes del banco\n")
        print(resultados)
        print("\n")

# Búsquedas de dinero
def MontoTotal():

    print("\n\t\t\t\tMonto total en el banco\n")
    df = clientesExcel.LeerClientes()
    filt = df['Monto'].sum()
    print("$ " + str(filt) + "\n")

def ValorMaximo():

    print("\n\t\t\t\tCliente con más dinero en el banco\n")
    df = clientesExcel.LeerClientes()
    filt = df['Monto'].max()
    filt2 = (df['Monto'] == filt)
    filt3 = df[filt2]
    print(filt3)
    print("\n")