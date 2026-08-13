

# 1
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


#2
while True:
    compra = int (input("Digite el valor de la compra: (Escriba f para finalizar) "))
    if compra.lower() == "f":
        break
    if compra > 100000: 
        descuento = compra * 0.50
        totalPagar = compra - descuento 
        print(f"El descuento aplicado es de: {descuento} y el total a pagar es de: {totalPagar}")
    else: 
        print("No se aplico descuento ya que la compra no pasa el monto para aplicar descuento")


#3

cantidad_numeros = 0
sumaTotal = 0 

while True: 
    numero = int(input("Ingrese un numero (Ingrese f para finalizar) "))
    if numero.lower() == "f":
        break
    