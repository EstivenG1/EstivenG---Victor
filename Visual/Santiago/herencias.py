

class hablar: 
    
    def hablar(self):
        return "Hola, estoy hablando"


class persona: 


    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nAltura: {self.altura}"


    
    def hablar(self):
            return "Hola, estoy hablando como empleado"
    

class empleado(persona): 
    def __init__(self, nombre, edad, altura, trabajo, salario):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.trabajo = trabajo
        self.salario = salario



    def __str__(self):
         return f"{super().__str__()},\nTrabajo: {self.trabajo}\nSalario: {self.salario}"


EstivenG = empleado("Estiven", 30, 1.75, "Ingeniero", 50000)
print(EstivenG)




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
