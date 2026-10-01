import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = float(masa)                      # kg
        self.radio = float(radio)                    # metros
        self.distancia_al_sol = float(distancia_al_sol)  # UA
        self.tiene_vida = tiene_vida

      def calcular_densidad(self):
        volumen = (4 / 3) * math.pi * self.radio ** 3
        return self.masa / volumen

    def es_planeta_exterior(self):
        return self.distancia_al_sol > 5.2      