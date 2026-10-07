class CuentaCorriente:
    def __init__(self, cliente, saldo_inicial=0):
     
        self.cliente = cliente
        self.saldo = saldo_inicial

    def acreditar_saldo(self, monto):
     
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto:,} Gs. correctamente.")
        else:
            print("Error: El monto a acreditar debe ser mayor a cero.")

    def registrar_consumo(self, monto):
       
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Compra aprobada: Consumo de {monto:,} Gs. registrado.")
        else:
            print(f"AVISO: ¡Saldo insuficiente! Intento de compra por {monto:,} Gs. rechazado.")

    def __str__(self):
      
        return f"Cliente: {self.cliente} | Saldo Actual: {self.saldo:,} Gs."


if __name__ == "__main__":
  
    print("=== CONTROL DE CUENTA CORRIENTE ===\n")
    
   
    cuenta = CuentaCorriente("Diego Gómez", 50000)
    print(cuenta)
    print("-" * 45)

   
    cuenta.acreditar_saldo(100000)
    print(cuenta)
    print("-" * 45)

    cuenta.registrar_consumo(70000)
    print(cuenta)
    print("-" * 45)

   
    cuenta.registrar_consumo(120000)
    print(cuenta)
    print("-" * 45)
