# EJEMPLO CON HERENCIA Y CLASE CARROS

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"Carro: {self.marca} {self.modelo}"


class Deportivo(Carro):
    def __init__(self, marca, modelo, velocidad_maxima):
        super().__init__(marca, modelo)
        self.velocidad_maxima = velocidad_maxima

    def descripcion(self):
        return f"{super().descripcion()}, Velocidad máxima: {self.velocidad_maxima} km/h"

class Camioneta(Carro):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga

    def descripcion(self):
        return f"{super().descripcion()}, Capacidad de carga: {self.capacidad_carga} kg"

# Ejemplo de uso
deportivo = Deportivo("Ferrari", "488 GTB", 330)
camioneta = Camioneta("Ford", "F-150", 1000)

print(deportivo.descripcion())
print(camioneta.descripcion())
