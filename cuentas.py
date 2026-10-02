class CuentaBancaria:
    def __init__(self, numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.__saldo = 0.0

    def depositar(self, monto):
        # HOTFIX: se valida que el monto de depósito sea positivo
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


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero_cuenta, titular, limite_sobregiro):
        super().__init__(numero_cuenta, titular)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor a 0")
        if monto > self.consultar_saldo() + self.limite_sobregiro:
            raise ValueError("El retiro excede el límite de sobregiro")
        self._modificar_saldo(-monto)

    def permite_sobregiro(self):
        return self.consultar_saldo() < 0


# Pruebas de uso
ahorros = CuentaAhorros("AH-001", "Ana Quispe", 4.5)
ahorros.depositar(1000)
ahorros.retirar(200)
print(ahorros)
print("Interés anual:", ahorros.calcular_interes())

corriente = CuentaCorriente("CC-001", "Luis Mamani", 500)
corriente.depositar(500)
corriente.retirar(800)
print(corriente)
print("¿Está en sobregiro?", corriente.permite_sobregiro())

try:
    corriente.retirar(300)
except ValueError as e:
    print("Error:", e)