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