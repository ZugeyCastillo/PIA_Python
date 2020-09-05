import re
import datetime

class Cliente:
    Id = 0
    Nombre = None
    Correo = None
    Telefono = None
    Direccion = None
    Monto = 0.0
    Estatus = None

class Prestamo:
    IdCliente = 0
    Monto = 0.0
    FechaCreacion = None
    FechaExpiracion = None
    TipoPrestamo = None
    AbonoTotal = 0
    Pagado = 0
    NombreCliente = None

class Validaciones:
        
    # Validación para que se escriba algo forzosamente cambio
    def validarCadena(self, cadena):
        esCadena = True
        if cadena == "":
            return False
        for numero in cadena:
            if not numero.isalpha():
                if numero != " ":
                    esCadena = False
                    break
        return esCadena

    # Validación para que se escriba algo forzosamente
    def validarNumerosInts(self, cadena):
        esNumero = True
        if cadena == "":
            return False
        for letra in cadena:
            if not letra.isdigit():
                esNumero = False
                break
        return esNumero

    # Validación para que se escriba algo forzosamente
    def validarNumerosFloats(self, cadena):
        esNumero = True
        if cadena == "":
            return False
        for letra in cadena:
            if not letra.isdigit():
                if letra != ".":
                    esNumero = False
                    break
        return esNumero
        
    def validarEmail(self, email): 
        regex = '^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(regex, email)): 
            return True
        else: 
            return False 
    
    def validarFecha(self, fecha):
        #2020-10-01
        try:
            datetime.datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False
 