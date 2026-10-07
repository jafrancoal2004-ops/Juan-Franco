class Producto:
    def __init__(self, nombre, precio, stock):
        
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def calcular_total(self):
        total = self.precio * self.stock
        return total

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio: {self.precio} Gs.\n"
            f"Stock: {self.stock} unidades\n"
            f"Valor en Stock: {self.calcular_total()} Gs.\n"
            f"-----------------------------------"
        )


if __name__ == "__main__":

    producto1 = Producto("Arroz 1kg", 6000, 20)
    producto2 = Producto("Leche 1L", 7000, 15)
    producto3 = Producto("Fideo 500g", 4500, 30)
    
  
    print(producto1)
    print(producto2)
    print(producto3)
