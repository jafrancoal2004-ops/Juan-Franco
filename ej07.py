class ProductoStock:
    def __init__(self, nombre, stock_inicial, stock_minimo):
   
        self.nombre = nombre
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
    
        if cantidad > 0:
            self.stock += cantidad
            print(f"Reposición: Se ingresaron {cantidad} unidades de {self.nombre}.")
        else:
            print("Error: La cantidad a ingresar debe ser mayor a cero.")

    def registrar_venta(self, cantidad):
        # Validamos que tengamos suficientes unidades para vender
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta: Se vendieron {cantidad} unidades de {self.nombre}.")
            
           
            if self.stock < self.stock_minimo:
                print(f"⚠️ ¡ALERTA DE REPOSICIÓN! El stock de {self.nombre} quedó en {self.stock} unidades (Mínimo: {self.stock_minimo}).")
        else:
            print(f"Error: No se puede vender {cantidad} unidades. Stock insuficiente (Disponible: {self.stock}).")

    def __str__(self):
       
        return f"Producto: {self.nombre} | Stock Actual: {self.stock} unidades"


if __name__ == "__main__":
    print("=== CONTROL DE STOCK CON ALERTAS ===\n")
    

    prod = ProductoStock("Leche Entera 1L", 15, 5)
    print(prod)
    print("-" * 50)

    prod.registrar_venta(8)
    print(prod)
    print("-" * 50)

    prod.registrar_venta(10)
    print("-" * 50)

    prod.registrar_venta(4)
    print(prod)
    print("-" * 50)


    prod.ingresar_mercaderia(20)
    print(prod)
    print("-" * 50)
