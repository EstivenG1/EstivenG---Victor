/*
- - - - - - -  - - - - - -  - - - - - - 
Estiven Garces Abreo - Tecnico en Programacion de Software
Aprendiz Sena - Tecnologo en Analisis y Desarrollo de Software
- - - - - - -  - - - - - -  - - - - - -
estivengarces151@gmail.com

Jugador Profecional De Bralw Stars - Equipo: Team Herectics
- - - - - - -  - - - - - -  - - - - - -
*/ 


/* Funciones en JavaScript */
// Reutilizar o reciclar bloques de codigo, para evitar escribir el mismo codigo varias veces, y asi optimizar el tiempo de desarrollo y mantenimiento del software.

/*

function nombreFuncion(parametros){
    // Bloque de codigo a ejecutar
}
    nombreFuncion(argumentos)
    
*/

// SIN PARAMETROS 

function saludar (){
    console.log("Hola, bienvenido a mi programa")
}

saludar()

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")



// PARAMETROS INICIALES

function saludopersonalizado(nombreUsuario){
    console.log("Hola! " + nombreUsuario + ", bienvenido a mi programa")
}

saludopersonalizado("Estiven")
saludopersonalizado("Nestor")
saludopersonalizado("Samuel")
saludopersonalizado("Juan")
saludopersonalizado("Carlos")

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")




// FUNCION QUE SUME 2 Numeoros 

function sumar (a, b){
    let resultado = a + b ;
    console.log("La suma es: " + resultado);

    return resultado;
}                   
sumar(5, 10)
sumar(9, 45)
sumar(53, 94)
sumar(45, 36)
sumar(56, 86)

console.log("- - - - - - - - - - - - - - - - - - - - - - - ")

// CON RETURN 

function sumar (a, b){
    return a + b ;
}    

console.log("La suma es: " + sumar(5, 10));
console.log("La suma es: " + sumar(9, 45));
console.log("La suma es: " + sumar(53, 94));
console.log("La suma es: " + sumar(45, 36));
console.log("La suma es: " + sumar(56, 86));


console.log("- - - - - - - - - - - - - - - - - - - - - - - ")



//FUNCION PARA CALCULAR PORCENTAJE DE DESCUENTO

function calcularPrecioDescuento(precioProducto, descuentoProducto){
    let descuento = (precioProducto * descuentoProducto) / 100;
    let Preciofinal = precioProducto - descuento;

    return Preciofinal;
}

calcularPrecioDescuento(100000, 20)
console.log("El precio final con descuento es: " + calcularPrecioDescuento(156400000, 54.1))
console.log("El precio final con descuento es: " + calcularPrecioDescuento(13400000, 99.9))
console.log("El precio final con descuento es: " + calcularPrecioDescuento(1200000, 86.0))



console.log("- - - - - - - - - - - - - - - - - - - - - - - ")


// CON RETURN

function calcularPrecioDescuento(precioProducto, descuentoProducto){
   return precioProducto - ((precioProducto * descuentoProducto) / 100) 
}

console.log("El precio final con descuento es: " + calcularPrecioDescuento(100000, 20))
console.log("El precio final con descuento es: " + calcularPrecioDescuento(37300000, 65.7))
console.log("El precio final con descuento es: " + calcularPrecioDescuento(100000, 56.8))



console.log("- - - - - - - - - - - - - - - - - - - - - - - ")


function gatosFijosMensuales(arriendo, servicios, mercado, trasnporte, suscripciones, ropas, cena, rumba){
    return arriendo + servicios + mercado + trasnporte + suscripciones + ropas + cena + rumba
}

// GASTOS ESTE MES

gastosEsteMes = gatosFijosMensuales(1200000, 350000, 400000, 150000, 200000, 300000, 250000, 500000)
console.log("Los gastos fijos mensuales son: " + gastosEsteMes)



/* FUNCIONES PURAS E IMPURAS */

// FUNCION PURA: Es una funcion que siempre devuelve el mismo resultado para los mismos argumentos, y no tiene efectos secundarios (no modifica variables externas ni interactua con el mundo exterior).
// FUNCION IMPURA: Es una funcion que puede devolver resultados diferentes para los mismos argumentos, o tiene efectos secundarios (modifica variables externas o interactua con el mundo exterior).



/* 
1. SIDE EFFECT O EFECTO SECUNDARIO: Es cualquier cambio que una funcion impura hace en el estado del programa o en el mundo exterior, como modificar una variable global, escribir en la consola, hacer una solicitud de red, etc.

a. MODIFICA VARIABLES GLOBALES: Si una funcion impura modifica una variable global, entonces tiene un efecto secundario, porque el valor de esa variable puede cambiar en diferentes partes del programa, lo que puede causar errores o comportamientos inesperados.
b. SOLICITUDES HTTP: Si una funcion impura hace una solicitud HTTP, entonces tiene un efecto secundario, porque el resultado de esa solicitud puede variar dependiendo de factores externos, como la disponibilidad del servidor, la velocidad de la red, etc.
c. IMPRIMIR EN PANTALLA O CONSOLA: Si una funcion impura imprime algo en la pantalla o en la consola, entonces tiene un efecto secundario, porque el resultado de esa impresión puede variar dependiendo del contexto, como el formato de la salida, el contenido de la impresión, etc.
d. MAINIPULACION DEL DOM: Si una funcion impura manipula el DOM (Document Object Model), entonces tiene un efecto secundario, porque el resultado de esa manipulacion puede variar dependiendo del estado del DOM, como los elementos presentes, los eventos asociados, etc.
e. OBTENER LA HORA ACTUAL: Si una funcion impura obtiene la hora actual, entonces tiene un efecto secundario, porque el resultado de esa obtencion puede variar dependiendo del momento en que se ejecute la funcion, lo que puede causar resultados diferentes para los mismos argumentos.
f. ENVIAR CORREOS ELECTRONICOS: Si una funcion impura envia correos electronicos, entonces tiene un efecto secundario, porque el resultado de ese envio puede variar dependiendo de factores externos, como la disponibilidad del servidor de correo, la direccion de destino, el contenido del correo, etc.
g. GENERAR NUMEROS ALEATORIOS: Si una funcion impura genera numeros aleatorios, entonces tiene un efecto secundario, porque el resultado de esa generacion puede variar cada vez que se ejecute la funcion, lo que puede causar resultados diferentes para los mismos argumentos.
h. MANIPULACION DE ARCHIVOS: Si una funcion impura manipula archivos (leer, escribir, eliminar, etc.), entonces tiene un efecto secundario, porque el resultado de esa manipulacion puede variar dependiendo del estado del sistema de archivos, como los permisos, la disponibilidad del archivo, el contenido del archivo, etc.
i. MANIPULACION DE BASES DE DATOS: Si una funcion impura manipula bases de datos (consultar, insertar, actualizar, eliminar, etc.), entonces tiene un efecto secundario, porque el resultado de esa manipulacion puede variar dependiendo del estado de la base de datos, como los registros presentes, los permisos, la disponibilidad del servidor de base de datos, etc.
j. MANIPULACION DE SESIONES O COOKIES: Si una funcion impura manipula sesiones o cookies, entonces tiene un efecto secundario, porque el resultado de esa manipulacion puede variar dependiendo del estado de las sesiones o cookies, como los valores almacenados, la expiracion, la disponibilidad del navegador, etc.

*/



// ESTRUCTURA DE UNA FUNCION PURA E IMPURA


function funcionPura(a, b) {
    return a + b;                      //PURA 
}

// IMPURA 

function funcionImpura(a, b) {
    console.log("Esta es una funcion impura");
    return a + b;                 //IMPURA
}

function elevaralcuadrado(Y){
    return Y * Y                //PURA
}


function sumadiez (Y){
    return Y + 10        //PURA
}





