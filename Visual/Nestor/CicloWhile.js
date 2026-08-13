/*- - - - - - - - - - - - - - */
//  CICLO WHILE - LOOP //
/*- - - - - - - - - - - - - - */

/* ESTRUCTURA DEL CICLO WHILE *

/* WHILE (CONDICION) {
    BLOQUE DE CODIGO A EJECUTAR
} */


let contador = 0;

while (contador < 5) {                        //WHILE - SE EJECUTA MIENTRAS LA CONDICION SEA VERDADERA - SE UTILIZA CUANDO NO SE SABE CUANTAS VECES SE VA A EJECUTAR EL BLOQUE DE CODIGO
    console.log("El contador es: " + contador);
    contador++;
}

//DECREMENTO

let numero = 5;

console.log("Ahora el número es: " + numero-- )
console.log("ahora se decrementa " + (numero));


//LIMITE DE SEGURIDAD - PARA EVITAR BUCLES INFINITOS

console.log("-------------------------------------------------------")

console.log("LIMITE 1")
console.log(" ")
let Limite = 3;

while (Limite-- > 0){
    console.log("LIMITE DE SEGURIDAD: " + Limite);
}


console.log("-------------------------------------------------------")


console.log("LIMITE 2")
console.log(" ")
let Limite2 = 0;

while (Limite2 < 50){
    console.log("LIMITE DE SEGURIDAD EN: " + Limite2)
    Limite2++
}


console.log("-------------------------------------------------------")

let limite3 = 5;
let contador3 = 0;

while (contador3 < 10 && limite3 > 0){
    console.log("LIMITE DE SEGURIDAD EN: " + limite3 + " y CONTADOR EN: " + contador3); //SE PUEDE UTILIZAR MAS DE UNA CONDICION EN EL WHILE PARA CONTROLAR EL BUCLE - EN ESTE CASO SE UTILIZA UN CONTADOR Y UN LIMITE DE SEGURIDAD PARA EVITAR UN BUCLE INFINITO
    contador3++;
    limite3--;
}



console.log("-------------------------------------------------------")

/* CICLO DO WHILE */

/* DO WHILE - SE EJECUTA AL MENOS UNA VEZ, INDEPENDIENTEMENTE DE LA CONDICION - SE UTILIZA CUANDO SE QUIERE EJECUTAR EL BLOQUE DE CODIGO AL MENOS UNA VEZ */

/* DO {
    BLOQUE DE CODIGO A EJECUTAR
    CONTADOR++ - -- INCREMENTO O DECREMENTO
} WHILE (CONDICION) */


let contador4 = 567

do{
    console.log("VALOR ACTUA: " + contador4)
    contador4++;
} while (contador4 < 5)





    /*    EJERCICIO 1 - CICLO WHILE */ 

    let edadUsuario = 5;
    let limit = 1;

while (edadUsuario <18 && limit > 0){
    console.log("HOLA, ERES MENOR DE EDAD TIENES " + edadUsuario + " AÑOS")
    limit--;
}


do{
    console.log("MENOR DE EDAD, TIENES " + edadUsuario + " AÑOS")
}while(edadUsuario < 18 && limit > 0)