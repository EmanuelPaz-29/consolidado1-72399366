class CuentaBancaria:
    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor a 0")
        self.__saldo += monto

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= monto

    def consultar_saldo(self):
        return self.__saldo

    def _modificar_saldo(self, cantidad):
        # Uso interno: permite que las subclases cambien el saldo privado
        self.__saldo += cantidad

    def __str__(self):
        return (f"Cuenta {self.numero_cuenta} | Titular: {self.titular} | "
                f"Saldo: S/ {self.consultar_saldo():.2f}")

   class CuentaAhorros(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, tasa_interes):
        super().__init__(numero_cuenta, titular)
        self.tasa_interes = tasa_interes

    def calcular_interes(self):
        return self.consultar_saldo() * self.tasa_interes / 100

    def __str__(self):
        return (f"{super().__str__()} | Tasa: {self.tasa_interes}% | "
                f"Interés anual: S/ {self.calcular_interes():.2f}") 