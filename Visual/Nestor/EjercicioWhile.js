/*
- - - - - - -  - - - - - -  - - - - - - 
Estiven Garces Abreo - Tecnico en Programacion de Software
Aprendiz Sena - Tecnologo en Analisis y Desarrollo de Software
- - - - - - -  - - - - - -  - - - - - -
estivengarces151@gmail.com

Jugador Profecional De Bralw Stars - Equipo: Team Herectics
- - - - - - -  - - - - - -  - - - - - -
*/ 




/* CICLO WHILE */

// PUNTO 1.

let I = 0
console.log(" 1. NUMEROS DEL 1 AL 10")
while (I < 10) {
    console.log("VALOR EN: ", I)
    console.log(" ")
    I++
}
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");



// PUNTO 2.

let J = 10
console.log("2. DECREMENTO DEL 1 AL 10")
do {
    console.log("VALOR EN: ", J)
    J--
}while(J >= 1)
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");


// 3. Suma del 1 al 100

console.log("3. Suma del 1 al 100:");
let suma = 0;
let k = 1;
while (k <= 100) {
    suma = suma + k;
    k++;
}
console.log("La suma es: " + suma);
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");



// PUNTO 5.

let sumapares = 0;
let num  = 1;

while (num <= 50) {
    if (num % 2 === 0){
        sumapares = sumapares + num;;
    }
    num++;
}
console.log("5. LA SUMA DE LOS NUMEROS PARES HASTA 50 ES: " + sumapares);
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");

// PUNTO 6

limite = 5;
while (true){
    console.log("6. LIMITE DE SEGURIDAD: " + limite);
    limite--;
    if (limite <= 0){
        console.log("LIMITE DE SEGURIDAD ALCANZADO: " + limite);
        break;
    }
}
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");


//PUNTO 7

let X = 20

while (X < 10){
    console.log(" WHILE VERIFICA Y PREGUNTA SI X ES MENOR QUE 10: " + X)
} do { 
    console.log(" DO WHILE EJECUTA EL CODIGO AL MENOS UNA VEZ: " + X)
}while (X < 10)
console.log(" - - - - - - - - - - - - - - - - - - - - - - - ");

