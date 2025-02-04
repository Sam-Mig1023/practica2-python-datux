#prueba
from Buses import Buses
from Conductor import Conductor

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa):
        if self.buscar_bus(placa):
            print(f"Error: El bus con placa {placa} ya existe.")
        else:
            bus = Buses(placa)
            self.buses.append(bus)
            print(f"El bus con placa {placa} se ha agregado exitosamente.")

    def agregar_conductor(self, dni, nombre):
        if self.buscar_conductor(dni):
            print(f"Error: El conductor con DNI {dni} ya existe.")
        else:
            conductor = Conductor(dni, nombre)
            self.conductores.append(conductor)
            print(f"El conductor {nombre} se ha agregado exitosamente.")

    def asignar_horario_conductor (self, dni, horario):
        # Verificar si el horario ya está asignado a otro conductor diferente
        for conductor in self.conductores:
            if horario in conductor.horarios and conductor.dni != dni:
                print(f"El horario {horario} ya ha sido asignado al conductor {conductor.nombre}.")
                return False  

        # Si no está asignado a otro, lo asignamos al conductor actual
        conductor_actual = self.buscar_conductor(dni)
        if conductor_actual:
            conductor_actual.asignar_horario(horario)
            return True

        print("No se encontró el conductor con el DNI proporcionado.")
        return False 

    def buscar_bus(self, placa):
        for bus in self.buses:
            if bus.placa == placa:
                return bus
        print(f"No se encontró un bus con placa {placa}.")
        return None

    def buscar_conductor(self, dni):
        for conductor in self.conductores:
            if conductor.dni == dni:
                return conductor
        print(f"No se ha encontrado al conductor con DNI {dni}.")
        return None