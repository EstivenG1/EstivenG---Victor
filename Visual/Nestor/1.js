console.log("=== 7 EJERCICIOS FÁCILES CON WHILE ===\n");

// 1. Números del 1 al 10
console.log("1. Números del 1 al 10:");
let i = 1;
while (i <= 10) {
    console.log(i);
    i++;
}

console.log("-------------------");

// 2. Conteo regresivo del 10 al 1
console.log("2. Conteo regresivo:");
let j = 10;
do {
    console.log(j);
    j--;
} while (j >= 1);

console.log("-------------------");

// 3. Suma del 1 al 100
console.log("3. Suma del 1 al 100:");
let suma = 0;
let k = 1;
while (k <= 100) {
    suma = suma + k;
    k++;
}
console.log("La suma es: " + suma);

console.log("-------------------");

// 4. Pedir número mayor a 10
console.log("4. Número mayor a 10:");
let numero;
do {
    numero = parseInt(prompt("Ingresa un número mayor a 10:"));
} while (numero <= 10);

console.log("Número correcto: " + numero);

console.log("-------------------");

// 5. Tabla de multiplicar
console.log("5. Tabla de multiplicar:");
let num = parseInt(prompt("Ingresa un número:"));
let m = 1;
while (m <= 10) {
    console.log(num + " x " + m + " = " + (num * m));
    m++;
}

console.log("-------------------");

// 6. Números pares hasta 50
console.log("6. Números pares hasta 50:");
let p = 2;
while (p <= 50) {
    console.log(p);
    p = p + 2;
}

console.log("-------------------");

// 7. Factorial de un número
console.log("7. Factorial:");
let n = parseInt(prompt("Ingresa un número para el factorial:"));
let factorial = 1;
let f = 1;

while (f <= n) {
    factorial = factorial * f;
    f++;
}
console.log("El factorial es: " + factorial);

console.log("\n=== TERMINADO ===");