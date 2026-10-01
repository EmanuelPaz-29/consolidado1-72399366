class Automovil:
    def __init__(self, marca, modelo, velocidad_max, nivel_combustible, año_fabricacion):
        self.marca = marca
        self.modelo = modelo
        # Se asignan con el setter para que se valide desde el inicio
        self.velocidad_max = velocidad_max
        self.nivel_combustible = nivel_combustible
        self.año_fabricacion = año_fabricacion

    @property
    def año_fabricacion(self):
        return self._año_fabricacion

    @año_fabricacion.setter
    def año_fabricacion(self, valor):
        if not (1886 <= valor <= 2026):
            raise ValueError("El año de fabricación debe estar entre 1886 y 2026")
        self._año_fabricacion = valor

    @property
    def nivel_combustible(self):
        return self._nivel_combustible

    @nivel_combustible.setter
    def nivel_combustible(self, valor):
        if not (0.0 <= valor <= 100.0):
            raise ValueError("El nivel de combustible debe estar entre 0.0 y 100.0")
        self._nivel_combustible = float(valor)

    @property
    def velocidad_max(self):
        return self._velocidad_max

    @velocidad_max.setter
    def velocidad_max(self, valor):
        if valor <= 0:
            raise ValueError("La velocidad máxima debe ser mayor a 0")
        self._velocidad_max = float(valor)

    def tiempo_llegada(self, distancia_km):
        return distancia_km / self.velocidad_max

    def __str__(self):
        if self.nivel_combustible < 20:
            estado = "Bajo"
        elif self.nivel_combustible < 60:
            estado = "Medio"
        else:
            estado = "Alto"
        return (f"Automóvil {self.marca} {self.modelo} | Año: {self.año_fabricacion} | "
                f"Velocidad máx: {self.velocidad_max} km/h | "
                f"Combustible: {self.nivel_combustible}% ({estado})")


# Pruebas de uso
auto = Automovil("Toyota", "Corolla", 180, 75, 2020)
print(auto)

# Uso de las propiedades (getter y setter)
print("Año:", auto.año_fabricacion)
auto.nivel_combustible = 50
print("Nuevo nivel de combustible:", auto.nivel_combustible)

# Método tiempo_llegada
print("Tiempo para 360 km:", auto.tiempo_llegada(360), "horas")

# Prueba de validación
try:
    auto.año_fabricacion = 1800
except ValueError as e:
    print("Error:", e)