class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def calcular_salario_anual(self):
        salario_anual = self.salario_mensual * 13
        return salario_anual

    def __str__(self):
      
        return (
            f"Empleado: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Salario Mensual: {self.salario_mensual} Gs.\n"
            f"Salario Anual (+ Aguinaldo): {self.calcular_salario_anual()} Gs.\n"
            f"-----------------------------------"
        )


if __name__ == "__main__":
   
    empleado1 = Empleado("Carlos Benítez", "Contador", 4500000)
    empleado2 = Empleado("Ana Espínola", "Secretaria", 3200000)
    

    print("=== LISTA DE EMPLEADOS ===\n")
    print(empleado1)
    print(empleado2)
