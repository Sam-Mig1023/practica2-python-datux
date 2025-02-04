from Admin import Admin
def Menu():
    mensaje="""
        \n\t\tMENÚ
        1. Agregar bus
        2. Agregar Ruta a Bus
        3. Registrar Horario a Bus
        4. Agregar Conductor
        5. Agregar Horario a Conductor
        6. Asignar Bus a Conductor
        7. Salir
        """
    print(mensaje)

if __name__=="__main__":
    admin = Admin()
    
    while True:
        Menu()
        try:
            opcion= int(input("\n\tIngrese una opcion: "))
            match opcion:
                case 1:
                    placa = input("Ingrese la placa del bus: ").strip()
                    admin.agregar_bus(placa)
                    
                case 2:
                    placa = input("Ingrese la placa del bus: ").strip()
                    bus = admin.buscar_bus(placa)
                    if bus:
                        ruta = input("Ingrese la ruta: ").strip()
                        bus.agregar_ruta(ruta)
                    else:
                        print("No se encontró el bus.")
                case 3:
                    placa = input("Ingrese la placa del bus: ").strip()
                    bus = admin.buscar_bus(placa)
                    if bus:
                        horario = input("Ingrese el horario (HH:MM-HH:MM): ").strip()
                        bus.asignar_horario(horario)
                    else:
                        print("No se encontró el bus.")
                case 4:
                    dni = input("Ingrese el DNI del conductor: ").strip()
                    nombre = input("Ingrese el nombre del conductor: ").strip()
                    admin.agregar_conductor(dni, nombre)
                case 5:
                    dni = input("Ingrese el DNI del conductor: ").strip()
                    horario = input("Ingrese el horario (HH:MM-HH:MM): ").strip()
                    admin.asignar_horario_conductor(dni, horario)
                case 6:
                    placa = input("Ingrese la placa del bus: ").strip()
                    bus = admin.buscar_bus(placa)
                    if bus:
                        dni = input("Ingrese el DNI del conductor: ").strip()
                        conductor = admin.buscar_conductor(dni)
                        if conductor:
                            horario = input("Ingrese el horario (HH:MM-HH:MM): ").strip()
                            if admin.asignar_horario_conductor(dni, horario):
                                bus.agregar_conductor(conductor, horario)
                        else:
                            print("No se encontró el conductor.")
                    else:
                        print("No se encontró el bus.")
                case 7:
                    print("Saliendo...")
                    break
                case _:
                    print("Ingrese una opcion valida.")
        except ValueError:
            print("Ingrese un numero.")
    