# ============================================
# CLASE DISPOSITIVO
# ============================================

class Dispositivo:
    def __init__(self, tipo, marca, modelo, año_compra):
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.año_compra = año_compra

    def mostrar_info(self):
        print("   -", self.tipo, self.marca, self.modelo, "(", self.año_compra, ")")

    def actualizar_año(self, nuevo_año):
        self.año_compra = nuevo_año
        print("Año actualizado a:", nuevo_año)


# ============================================
# CLASE ESTUDIANTE
# ============================================

class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        self.lista_dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.lista_dispositivos.append(dispositivo)

    def mostrar_dispositivos(self):
        print("")
        print("Estudiante:", self.nombre)
        print("Edad:", self.edad)
        print("Grado:", self.grado)
        print("Dispositivos:")

        if len(self.lista_dispositivos) == 0:
            print("   (No tiene dispositivos)")
        else:
            for d in self.lista_dispositivos:
                d.mostrar_info()

        print("Cantidad de dispositivos:", self.contar_dispositivos())

    def contar_dispositivos(self):
        return len(self.lista_dispositivos)


# ============================================
# FUNCIONES DE GESTIÓN
# ============================================

def crear_dispositivo():
    print("")
    print("--- Crear nuevo dispositivo ---")

    tipo = input("Tipo (celular/tablet/laptop): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")

    while True:
        try:
            año = int(input("Año de compra: "))
            break
        except ValueError:
            print("Ingrese un año válido.")

    nuevo = Dispositivo(tipo, marca, modelo, año)
    return nuevo


def mostrar_todos_los_estudiantes(lista_estudiantes):
    print("")
    print("========================================")
    print("LISTA DE ESTUDIANTES Y DISPOSITIVOS")
    print("========================================")

    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        for est in lista_estudiantes:
            est.mostrar_dispositivos()
            print("----------------------------------------")


def buscar_por_grado(lista_estudiantes, grado):
    encontrados = []

    for est in lista_estudiantes:
        if est.grado.lower() == grado.lower():
            encontrados.append(est)

    return encontrados


def contar_estudiantes_con_mas_de_dos(lista_estudiantes):
    contador = 0

    for est in lista_estudiantes:
        if est.contar_dispositivos() > 2:
            contador += 1

    return contador


# ============================================
# CASO PRÁCTICO
# ============================================

# --- Dispositivos de Dylan ---
disp1 = Dispositivo("celular", "Samsung", "Galaxy S21", 2021)
disp2 = Dispositivo("tablet", "Apple", "iPad Air", 2022)

# --- Dispositivos de Salome ---
disp3 = Dispositivo("laptop", "HP", "Pavilion", 2023)
disp4 = Dispositivo("celular", "Xiaomi", "Redmi Note 10", 2022)

# --- Dispositivo de Alejandro ---
disp5 = Dispositivo("tablet", "Lenovo", "Tab P11", 2023)

# --- Estudiantes ---
dylan = Estudiante("Dylan Hinestroza", 12, "6to grado")
dylan.agregar_dispositivo(disp1)
dylan.agregar_dispositivo(disp2)

salome = Estudiante("Salome Jimenez", 13, "7mo grado")
salome.agregar_dispositivo(disp3)
salome.agregar_dispositivo(disp4)

alejandro = Estudiante("Alejandro Varela", 11, "5to grado")
alejandro.agregar_dispositivo(disp5)

# --- Lista general ---
estudiantes = [dylan, salome, alejandro]

# ============================================
# MOSTRAR TODOS LOS ESTUDIANTES
# ============================================

mostrar_todos_los_estudiantes(estudiantes)

# ============================================
# BUSCAR POR GRADO (USUARIO INGRESA EL GRADO)
# ============================================

print("")
print("--- Buscar estudiantes por grado ---")

grado_buscar = input("Ingrese el grado que desea buscar: ")

resultado = buscar_por_grado(estudiantes, grado_buscar)

print("")
print("Resultados encontrados:")

if len(resultado) == 0:
    print("No se encontraron estudiantes en ese grado.")
else:
    for e in resultado:
        print("  *", e.nombre)

# ============================================
# CREAR NUEVO ESTUDIANTE
# ============================================

print("")
print("--- Crear nuevo estudiante ---")

nombre = input("Nombre: ")

while True:
    try:
        edad = int(input("Edad: "))
        break
    except ValueError:
        print("Ingrese una edad válida.")

grado = input("Grado: ")

nuevo_estudiante = Estudiante(nombre, edad, grado)

# Agregar dispositivo al nuevo estudiante
dispositivo_nuevo = crear_dispositivo()
nuevo_estudiante.agregar_dispositivo(dispositivo_nuevo)

# Agregar a la lista general
estudiantes.append(nuevo_estudiante)

print("")
print("Estudiante agregado correctamente:")
nuevo_estudiante.mostrar_dispositivos()

# ============================================
# AGREGAR DISPOSITIVO A ESTUDIANTE EXISTENTE
# ============================================

print("")
print("--- Agregar dispositivo a estudiante existente ---")

print("Estudiantes registrados:")
for est in estudiantes:
    print("-", est.nombre)

nombre_buscar = input("Ingrese el nombre del estudiante: ")

encontrado = False

for est in estudiantes:
    if est.nombre.lower() == nombre_buscar.lower():

        nuevo_dispositivo = crear_dispositivo()
        est.agregar_dispositivo(nuevo_dispositivo)

        print("")
        print("Dispositivo agregado correctamente a", est.nombre)

        print("")
        print("Información actualizada:")
        est.mostrar_dispositivos()

        encontrado = True
        break

if encontrado == False:
    print("No se encontró un estudiante con ese nombre.")

# ============================================
# CONTAR ESTUDIANTES CON MÁS DE 2 DISPOSITIVOS
# ============================================

total = contar_estudiantes_con_mas_de_dos(estudiantes)

print("")
print("Estudiantes con más de 2 dispositivos:", total)

# ============================================
# MOSTRAR ESTADO FINAL DEL SISTEMA
# ============================================

print("")
print("ESTADO FINAL DEL SISTEMA")

mostrar_todos_los_estudiantes(estudiantes)