class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"

    def marcar_como_atendido(self):
        self.estado = "atendido"
        print(f"Turno de las {self.hora} atendido con éxito.")

    def __str__(self):
        return f"Hora: {self.hora} | Paciente: {self.paciente} | Estado: {self.estado}"


class Agenda:
    def __init__(self):
        self.lista_turnos = []
    def agregar_turno(self, nuevo_turno):
    
        self.lista_turnos.append(nuevo_turno)
        print(f"Turno agendado para: {nuevo_turno.paciente} a las {nuevo_turno.hora}")

    def listar_pendientes(self):
        print("\n--- TURNOS PENDIENTES DE LA JORNADA ---")
        hay_pendientes = False
        for turno in self.lista_turnos:
            if turno.estado == "pendiente":
                print(turno)
                hay_pendientes = True
        
        if not hay_pendientes:
            print("No quedan turnos pendientes por hoy.")



if __name__ == "__main__":
    print("=== SISTEMA DE GESTIÓN DE TURNOS ===\n")
    mi_agenda = Agenda()
    
    turno1 = Turno("Juan Almada", "08:30")
    turno2 = Turno("María Galeano", "09:15")
    turno3 = Turno("Pedro Benítez", "10:00")
    
    mi_agenda.agregar_turno(turno1)
    mi_agenda.agregar_turno(turno2)
    mi_agenda.agregar_turno(turno3)
    
    mi_agenda.listar_pendientes()
    print("-" * 50)
    
    turno1.marcar_como_atendido()
    turno3.marcar_como_atendido()
    print("-" * 50)
    
    mi_agenda.listar_pendientes()
