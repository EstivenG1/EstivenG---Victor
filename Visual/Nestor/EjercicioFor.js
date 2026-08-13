/*
- - - - - - -  - - - - - -  - - - - - - 
Estiven Garces Abreo - Tecnico en Programacion de Software
Aprendiz Sena - Tecnologo en Analisis y Desarrollo de Software
- - - - - - -  - - - - - -  - - - - - -
estivengarces151@gmail.com

Jugador Profecional De Bralw Stars - Equipo: Team Herectics
- - - - - - -  - - - - - -  - - - - - -
*/ 



// PUNTO 1

lista = ["Camisa", "Pantalon", "Zapatos", "Corbata", "Chaqueta"]

let i = 0
console.log("LISTA DE ROPA:")
for (i = 0; i < lista.length ; i++){
    console.log("Objeto: " + lista[i] + " - Letras: " + lista[i].length)
}

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")



//PUNTO 2


let frase = "Dios te bendiga "
for (let letra of frase){
    console.log(letra)
}

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")


//PUNTO 3

array = ["Fresa", "Mango", "Pera", "Manzana", "Uva"]

for (let fruta of array){
    console.log("ME GUSTA MUCHO LA "+ fruta)
}

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")



//PUNTO 4

producto = {
    nombre: "Takis",
    categoria: "Snack",
    precio: 6500
}

for (let propiedad in producto){
    console.log("Propiedad: " + propiedad + " - Valor: " + producto[propiedad])
}


//PUNTO 5

listaN = [1,2,3,4,5,6,7,8,9,10]


for (let I = 0; I < listaN.length; I++){
    console.log("clasico: "+ listaN[I])
}

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")

for (let num in listaN){
    console.log("for of " + num)
}




// NO PS EL MAS FACIL DE USAR ES EL FOR OF, POR QUE NO MANEJA LA LONGITUD O POSICION DE LOS ELEMENTOS, Y AHORRA LINEAS DE CODIGO
// AUNQUE EL FOR CLASICO ES MAS UTIL A LA HORA DE DESPERTAR LOGICA Y YO DIRIA YO QUE ES MEJOR EMPEZAR POR ESTE, Y CUANDO UNO YA TAN, YA SE PUEDE USAR EL FOR OF
