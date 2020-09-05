from clases2 import Cliente
from AclientesExcel import ClientesExcel
from clases2 import Validaciones
from prestamosExcel2 import PrestamosExcel

clientesExcel = ClientesExcel()
validaciones = Validaciones()
prestamosExcel = PrestamosExcel()

def CrearCliente():

    cliente = Cliente()
    print("\n\t\tCreación de clientes\n\nIngrese los datos del nuevo cliente")
    cliente.Nombre = input("\nNombre: ")

    while not validaciones.validarCadena(cliente.Nombre):
        cliente.Nombre = input("Introduzca un nombre válido: ")

    cliente.Correo = input("Correo: ")
   
    while not validaciones.validarEmail(cliente.Correo):
        cliente.Correo = input("Introduzca un correo válido: ")

    cliente.Telefono = input("Teléfono: ")

    while not validaciones.validarNumerosInts(cliente.Telefono):
        cliente.Telefono = input("Introduzca un teléfono válido: ")
    cliente.Telefono = str(cliente.Telefono)

    cliente.Direccion = input("Dirección: ")
    cliente.Monto = input("Monto: ")
    
    while not validaciones.validarNumerosFloats(cliente.Monto):
        cliente.Monto = input("Introduzca un monto válido: ")
    cliente.Monto = float(cliente.Monto)
    
    clientesExcel.AgregarCliente(cliente)
    print("\n\t\t\t\tClientes del banco\n")
    print(clientesExcel.LeerClientes())
    print("\nSe agregó el cliente con éxito.")

def ActualizarCliente():

    print("\n\t\tActualización de clientes")
    clienteId = input("\nIngrese el Id del cliente que desea actualizar: ")
    #------------------------------------------------------------
    while not validaciones.validarNumerosInts(clienteId):
        clienteId = input("Introduzca un id válido: ")
    clienteId = int(clienteId)

    if clientesExcel.LeerClientesId(clienteId).empty:
        print("\nNo existe cliente.")
    else:
    #------------------------------------------------------------
        print("\n\t\t\t\tCliente a modificar\n")
        print(clientesExcel.LeerClientesId(clienteId))

        cliente = Cliente()
        cliente = clientesExcel.LeerClienteObjeto(clienteId)

        if cliente.Estatus == 0:
            print("El cliente ha sido eliminado y no se puede editar.")
            #Ejecutar menu anterior
        else:
            print("\nSeleccione el campo que desea actualizar")
            print("a) Nombre\nb) Correo\nc) Teléfono\nd) Dirección\ne) Monto\nr) Regresar")

            opcion = ""
            opcion = input("\nOpcion: ")

            # r - opcion que te regresa al menu del cliente
            while opcion != "r":
                if opcion == "a":
                    valor = input("\nIngrese el nuevo valor para (Nombre): ")

                    while not validaciones.validarCadena(valor):
                        valor = input("Introduzca un nombre válido: ")

                    clientesExcel.AcualizarCliente(clienteId, 'Nombre', valor)

                elif opcion == "b":
                    valor = input("\nIngrese el nuevo valor para (Correo): ")

                    while not validaciones.validarEmail(valor):
                        valor = input("Introduzca un correo válido: ")

                    clientesExcel.AcualizarCliente(clienteId, 'Correo', valor)

                elif opcion == "c":
                    valor = input("\nIngrese el nuevo valor para (Teléfono): ")
                    
                    while not validaciones.validarNumerosInts(valor):
                        valor = input("Introduzca un telefono válido: ")

                    clientesExcel.AcualizarCliente(clienteId, 'Telefono', str(valor))

                elif opcion == "d":
                    valor = input("\nIngrese el nuevo valor para (Dirección): ")
                    clientesExcel.AcualizarCliente(clienteId, 'Direccion', valor)

                elif opcion == "e":
                    valor = input("\nIngrese el nuevo valor para (Monto): ")

                    while not validaciones.validarNumerosFloats(valor):
                        valor = input("Introduzca un monto válido: ")

                    clientesExcel.AcualizarCliente(clienteId, 'Monto', float(valor))

                else:
                    print("Ingrese un valor válido")

                if opcion == "a" or opcion == "b" or opcion == "c" or opcion == "d" or opcion == "e":
                    print("\n\t\t\t\tCliente modificado\n")
                    print(clientesExcel.LeerClientesId(clienteId))
                    print("\nEl cliente se actualizó con éxito")

                print("\nSeleccione el campo que desea actualizar")
                print("a) Nombre\nb) Correo\nc) Teléfono\nd) Dirección\ne) Monto\nr) Regresar")
                opcion = input("Opcion: ")

def EliminarCliente():

    print("\n\t\tEliminación de clientes")
    clienteId = input("\nIngrese el Id del cliente que desea eliminar: ")

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
            print("El cliente ha sido eliminado previamente.")
            #Ejecutar menu anterior
        elif not prestamosExcel.LeerPrestamosActivosCliente(clienteId).empty:
            print("El cliente tiene un adeudo y no se puede eliminar.")
            #Ejecutar menu anterior
        else:
            print("\n\t\t\t\tCliente eliminado\n")
            clientesExcel.EliminarCliente(clienteId)
            print(clientesExcel.LeerClientesId(clienteId))
            print("\nEl cliente se eliminó con éxito.")