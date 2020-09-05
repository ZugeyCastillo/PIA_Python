from clases2 import *
from AclientesExcel import ClientesExcel
from prestamosExcel2 import PrestamosExcel
# sirve para obtener la fecha del dia de hoy
import datetime
# sirve para añadir meses a una fecha
from dateutil.relativedelta import relativedelta

# creamos clientesExcel para utilizar metodos de la hoja clientes del excel
clientesExcel = ClientesExcel()
# creamos prestamosExcel para utilizar metodos de la hoja prestamos del excel
prestamosExcel = PrestamosExcel()
validaciones = Validaciones()

def AbonarPrestamo():
    print("\n\t\tSaldar préstamo")
    clienteId = input("\nIngrese el Id del cliente que abonará: ")
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
            print("\nEl cliente ha sido eliminado y no puede abonar.")
            #Ejecutar menu anterior
        elif prestamosExcel.LeerPrestamosActivosCliente(clienteId).empty:
            print("\nEl cliente no tiene adeudos.")
            #Ejecutar menu anterior
        else:
            print("\n\t\tDatos del préstamo del cliente")
            print(prestamosExcel.LeerPrestamosActivosCliente(clienteId))
            adeudo = prestamosExcel.LeerAdeudoCliente(clienteId)
            print("\nEl cliente " + cliente.Nombre + " tiene un adeudo por: $" + str(adeudo))

            abono = input("\nIngrese el abono: ")

            while not validaciones.validarNumerosFloats(abono):
                abono = input("Introduzca un abono valido: ")

            print("\n\t\tDatos del préstamo del cliente")
            cambio = prestamosExcel.AbonarPrestamo(clienteId, float(abono))
            print("\nSe realizó el abono con éxito, su cambio es de $" + str(cambio))
        
def CrearPrestamo():
    # es el objeto prestamo que llenaremos con la informacion que se lea
    prestamo = Prestamo()
    cliente = Cliente()
    print("\n\t\tSolicitud de préstamo")
    print("\nIngrese el id del cliente que solicita el préstamo")
    clienteId = input("Id: ")

    #------------------------------------------------------------
    while not validaciones.validarNumerosInts(clienteId):
        clienteId = input("Introduzca un id válido: ")
    clienteId = int(clienteId)
    
    if clientesExcel.LeerClientesId(clienteId).empty:
        print("\nNo existe cliente.")
    else:
    #------------------------------------------------------------
        # nos regresa un objeto cliente con la informacion del excel a partir
        # del cliente id
        cliente = clientesExcel.LeerClienteObjeto(clienteId)

        if cliente.Estatus == 0:
            print("\nCliente eliminado. No puede solicitar un préstamo.")
        else:
            # si prestamosExcel.LeerPrestamosActivosCliente(clienteId).empty es true
            # quiere decir que ese cliente no tiene prestamos activos y por lo tanto puede solicitar uno
            # si prestamosExcel.LeerPrestamosActivosCliente(clienteId).empty es false
            # quiere decir que el cliente tiene prestamos activos y no puede solicitar uno nuevo
            if prestamosExcel.LeerPrestamosActivosCliente(clienteId).empty:
                # imprime la informacion del cliente por id
                print("\n\t\tCliente que ha solicitado un préstamo")
                print(clientesExcel.LeerClientesId(clienteId))
                
                print("\nIngrese la información para el prestamo: ")
                
                monto = input("Monto del préstamo: $")
                while not validaciones.validarNumerosFloats(monto):
                    monto = input("Introduzca un monto válido: ")
                monto = float(monto)
                
                print("\nNOTA. Considere la tabla de intereses antes de ingresar el plazo.\n")
                print(prestamosExcel.LeerIntereses())
                
                plazo = input("\nPlazo (meses): ")
                while not validaciones.validarNumerosInts(plazo):
                    plazo = input("Introduzca un plazo válido: ")
                plazo = int(plazo)

                if plazo <= 2:
                    montoFinal = monto * 1.05
                    tipo = 1
                elif plazo > 2 and plazo <= 6:
                    montoFinal = monto * 1.1
                    tipo = 2
                else:
                    montoFinal = monto * 1.3
                    tipo = 3

                prestamo.IdCliente = clienteId
                prestamo.Monto = montoFinal
                prestamo.FechaCreacion = str(datetime.date.today())
                prestamo.FechaExpiracion = str(datetime.date.today() + relativedelta(months=+plazo))
                prestamo.TipoPrestamo = tipo
                prestamo.AbonoTotal = 0
                prestamo.Pagado = 0
                prestamo.NombreCliente = cliente.Nombre

                prestamosExcel.AgregarPrestamo(prestamo)
                print("\nEl préstamo se realizó con éxito.")
                print("\n\t\tDatos del préstamo al cliente\n")
                print(prestamosExcel.LeerPrestamosActivosCliente(clienteId))

            else:
                print("\nEl cliente no es candidato para un préstamo.")

def VerPrestamos():
    print("\n\t\t\tClientes con préstamos\n")
    print(prestamosExcel.LeerPrestamos())