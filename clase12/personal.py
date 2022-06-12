from random import randint
from permanentes import empleadoPermanente
from eventuales import empleadoEventual
import names

class personal:
    def __init__(self):
        empleados = []
        for i in range(10):
            temp = {
                'nombre': names.get_first_name(),
                'apellido': names.get_last_name(),
                'dni': randint(10000000, 99999999),
                'salario': randint(10000, 99999),
            }
            aux = randint(0, 1)
            if (aux == 1):
                # auxVentas = randint(1, 99)
                auxVentas = randint(1, 9)
                temp['ventas'] = []
                for i in range(auxVentas):
                    temp['ventas'].append(randint(1000, 9999))
                    
            else:
                temp['antiguedad'] = randint(0, 9)
            
            empleados.append(temp.copy())
        self.empleados = empleados.copy()

    def verificaDni(self, dni):
        retorna = None
        for empleado in self.empleados:
            if empleado['dni'] == dni:
                if (empleado.has_key('ventas')):
                    retorna = empleadoEventual(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['ventas']) 
                else:   
                    retorna = empleadoPermanente(empleado['nombre'], empleado['apellido'], empleado['dni'], empleado['salario'], empleado['antiguedad'])
                    
        return retorna
    
    def listarEmpleados(self):
        for empleado in self.empleados:
            print(empleado)
    
    def agregarEmpleado(self, nombre, apellido, dni, salario, extra):
        if (self.verificaDni(dni) == None):
            if (type(extra) is list):
                temp = empleadoEventual(nombre, apellido, dni, salario, extra)            
                self.empleados.append(temp)
                retorna = temp
            else:   
                temp = empleadoPermanente(nombre, apellido, dni, salario, extra)
                self.empleados.append(temp)
                retorna = temp
        else:
            retorna = 'Usuario existente'
        return retorna

    def verificaString(self, str):
        aux = []
        for empleado in self.empleados:
            if (str in empleado['nombre'] or str in empleado['apellido']):
                aux.append(empleado.copy())
        return aux