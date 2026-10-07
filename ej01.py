class Cliente:
    def __init__(self, nombre, cedula, telefono):
        """Constructor: Inicializa los datos personales básicos del cliente."""
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        """Devuelve la ficha del cliente de forma ordenada y legible usando f-strings."""
        return (
            f"========================================\n"
            f"           FICHA DE CLIENTE             \n"
            f"========================================\n"
            f"Nombre   : {self.nombre}\n"
            f"Cédula   : {self.cedula}\n"
            f"Teléfono : {self.telefono}\n"
            f"========================================"
        )


if __name__ == "__main__":
  
    cliente1 = "Juan Pérez"
    cedula1 = "1.234.567"
    telefono1 = "0981-111-222"
    c1 = Cliente(cliente1, cedula1, telefono1)
    
    cliente2 = "María Rodríguez"
    cedula2 = "3.456.789"
    telefono2 = "0971-333-444"
    c2 = Cliente(cliente2, cedula2, telefono2)
    
   
    print(c1)
    print("\n")  
    print(c2)
