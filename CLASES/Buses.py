from Conductor import Conductor
class Buses:
    def __init__(self, placa):
        self.placa = placa
        self.ruta = ""
        self.horarios = []
        self.conductoresAsignado=[]

    def agregar_ruta(self, ruta):
        if self.ruta:
            print(f"La ruta {ruta} ya ha sido asignada al bus de placa {self.placa}.")
        else:
            self.ruta = ruta
            print(f"La ruta {ruta} se ha asignado exitosamente al bus de placa {self.placa}.")
    
    def asignar_horario(self, horario):
        if horario in self.horarios:
            print(f"El horario {horario} ya ha sido asignado para el bus de placa {self.placa}.")
        else:
            self.horarios.append(horario)
            print(f"El horario {horario} se ha asignado exitosamente para el bus de placa {self.placa}.")

    def agregar_conductor(self, conductor, horario):
        if conductor in self.conductoresAsignado:
                print(f"El conductor {conductor.nombre} ya ha sido asignado al horario {horario}.")
                return
        conductor.asignar_horario(horario)
        self.conductoresAsignado.append(conductor)

        print(f"El conductor {conductor.nombre} se ha asignado exitosamente al bus de placa {self.placa} en el horario {horario}.")

    def __str__(self):
        if self.conductoresAsignado:
            conductor = self.conductoresAsignado[0].nombre
        else:
            conductor = "Ninguno"
        return f"\n\tBus:\nPlaca:{self.placa}\nRuta: {self.ruta}\nHorarios: {self.horarios} \nConductor: {conductor}"


