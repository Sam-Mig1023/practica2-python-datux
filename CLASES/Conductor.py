class Conductor:
    def __init__(self, dni, nombre):
        self.dni= dni
        self.nombre = nombre
        self.horarios=[]

    def asignar_horario(self, hora):
        if hora in self.horarios:
            print(f"El horario {hora} ya ha sido registrado.")
        else:
            self.horarios.append(hora)
            print(f"El horario {hora} se registró exitosamente.")
    
    def __str__(self):
        return f"\n\tConductor:\nDNI:{self.dni}\nNombre: {self.nombre}\nHorario: {self.horarios}"
