

#1. Número positivo, negativo o cero Solicite un número entero al usuario y determine si es positivo, negativo o igual a cero. Muestre el resultado correspondiente.

while True:
    numero = int(input("Digite un numero: (Escriba 0 para finalizar) "))
    if numero == 0:
        break
    if numero > 0:
        print("Tu numero es positivo")
    elif numero < 0:
        print("tu numero es Negativo")
    else: 
        print("Tu numero es Cero")



#2. Descuento en una compra Solicite el valor de una compra y aplique el descuento según el monto establecido. Al finalizar, muestre el descuento aplicado y el total a pagar.

compra = float (input("Digite el valor de la compra: "))

if compra > 50000 :
    descuento = compra * 0.50 
    totalPagar = compra - descuento 
    print ("el descuento aplocado es de: " + str(descuento))
    print("El total a pagar es de: ", totalPagar)
else:
    print("La compra no a superado el precio para obtener descuento ")
    print("El total a pagar es de: ", compra)


#3. Suma de números Permita ingresar números de forma repetitiva hasta que el usuario decida finalizar. Al terminar, muestre la cantidad de números ingresados y la suma total.

cantidad_numeros = 0
suma_total = 0

while True:
    numero = input("Ingrese un número (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    try:
        numero = float(numero)
        cantidad_numeros += 1
        suma_total += numero
    except ValueError:
        print("Por favor, ingrese un número válido.")
print(f"Cantidad de números ingresados: {cantidad_numeros}")
print(f"Suma total: {suma_total}")


#4. Adivina el número Genere un número aleatorio entre 1 y 20 y permita que el usuario intente adivinarlo. El programa debe indicar la cantidad de intentos realizados hasta acertar.


import random
numero_secreto = random.randint(1, 20)
intentos = 0

while True: 
    numeroUsuario = float(input("Adivina el numero del 1 al 20: "))
    intentos += 1
    if numeroUsuario == numero_secreto: 
        print("Felicidades, Ganaste ")
        print("Cantidad de intentos realizados: ", intentos)
        break

    elif numeroUsuario < numero_secreto:
        print("El numero es mayor, intenta de nuevo")
    else:
        print("El numero es menor, intenta de nuevo")

#5. Tabla de multiplicar Solicite un número entero y muestre su tabla de multiplicar del 1 al 10 utilizando un ciclo for.


numtabla = int (input("Digite su numero a multiplicar: "))


for i in range(1, 11):
    resultado = numtabla * i
    print(f"{numtabla} x {i} = {resultado}")




#6. Promedio de estudiantes Solicite la cantidad de estudiantes y registre la nota de cada uno. Al finalizar, muestre el promedio del grupo, la nota más alta, la más baja y la cantidad de estudiantes aprobados y reprobados. sin vectores ni ciclos

cantidad_estudiantes = int(input("Digite la cantidad de estudiantes: "))
promedio = 0
nota_maxima = float('-inf')
nota_minima = float('inf')
aprobados = 0
reprobados = 0

for i in range(cantidad_estudiantes):
    nota = float(input(f"Digite la nota del estudiante {i + 1}: "))
    promedio += nota

    if nota > nota_maxima:
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota

    if nota >= 3.0:
        aprobados += 1
    else:
        reprobados += 1

promedio /= cantidad_estudiantes

print(f"Promedio del grupo: {promedio}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")
print(f"Cantidad de estudiantes aprobados: {aprobados}")
print(f"Cantidad de estudiantes reprobados: {reprobados}")
