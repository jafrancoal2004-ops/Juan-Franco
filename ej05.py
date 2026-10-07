class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
      
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def obtener_descripcion(self):

        return f"{self.marca} {self.modelo} {self.anio} — {self.precio:,} Gs."

    def __str__(self):
    
        return self.obtener_descripcion()

if __name__ == "__main__":
    auto1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
    auto2 = Vehiculo("Hyundai", "HB20", 2022, 78000000)
    
    print("=== PUBLICACIONES DE LA AGENCIA ===\n")
    print(auto1)
    print(auto2)
