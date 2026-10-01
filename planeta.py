import math


class Planeta:
    def __init__(self, nombre, masa, radio, distancia_al_sol, tiene_vida=False):
        self.nombre = nombre
        self.masa = float(masa)                      # kg
        self.radio = float(radio)                    # metros
        self.distancia_al_sol = float(distancia_al_sol)  # UA
        self.tiene_vida = tiene_vida