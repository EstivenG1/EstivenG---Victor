/* - - Estiven Garces abreo - -  Tecnico en Programacion de Software - -
- - Aprendiz Sena - - Tecnologo en analisis y desarrollo de sofware - -  */



/*- - - - - - - - - - - - - - - - - - - - - - - - - - - */ 
/*- -  CICLO FOR CLASICO - ITERACION DE LISTAS - - */
/*- - - - - - - - - - - - - - - - - - - - - - - - - - - */ 

//ITERAR - RECORRER DE FORMA SECUENCIAL

/* ESTRUCTURA DEL CICLO FOR */

/* FOR (INICIALIZACION; CONDICION; INCREMENTO){
      BLOQUE DE CODIGO A EJECUTAR 
      }   */


Local = ["pantalon", "camisa", "zapatos", "corbata", "sombrero"];

for (let i = 0; i < Local.length; i++) {                             //CICLO FOR - RECORRE DE INICIO A FIN DE UNA LISTA (SE PUEDEN CAMBIAR LOS VALORES) - SE UTILIZA CUANDO SE QUIERE RECORRER TODOS LOS ELEMENTOS DE UNA LISTA
    console.log(Local[i]);
}


console.log("- - - - - - - - - - - - - - - - - - - - - - - - - - - - --");


numero = [1, 2, 3 ,4, 5, 6]

for (let J =0; J < numero.length; J++){
    console.log(numero[J]);
}



console.log("- - - - - - - - - - - - - - - - - - - - - - - - - - - - --");

/*- - - - - - - - - - - - - - - - - - - - - - - - - - - - */ 
/* - - CICLO FOR - OF - ITERACION DE LISTAS - -  */
/*- - - - - - - - - - - - - - - - - - - - - - - - - - - - */ 

/* ESTRUCTURA DEL CICLO FOR - OF */
/* FOR ( VARIABLE OF LISTA) {
    // BLOQUE DE CODIGO A EJECUTAR
} */

colores = ["rojo", "azul", "verde", "amarillo", "morado"];

for (let color of colores) { //color = i
    console.log(color);                                              //FOR OF - RECORRE DE INICIO A FIN DE UNA LISTA - SE UTILIZA CUANDO SE QUIERE RECORRER TODOS LOS ELEMENTOS DE UNA LISTA
}


console.log("- - - - - - - - - - - - - - - - - - - - - - - - - - - - -");

/*- - - - - - - - - - - - - - - - - - - - - - - - - - - */ 
/* - - CICLO FOR - IN - ITERACION DE OBJETOS - -  */
/* - - - - - - - - - - - - - - - - - - - - - - - - - - - */


//FOR IN - SIRVE PARA COSAS ENUMERABLES - SE UTILIZA PARA RECORRER LOS ELEMENTOS DE UN OBJETO
//FOR IN - OBJECTS

/* FOR ( VARIABLE IN OBJETO) {
    // BLOQUE DE CODIGO A EJECUTAR
} */


const tiendaCelulares = {
    //PROPIEDAD (CLAVE) - VALOR
    Samsung: "Galaxy S21",
    Apple: "iPhone 13",
    Xiaomi: "Redmi Note 10",
}

for (let marca in tiendaCelulares) {
    console.log(marca + ": " + tiendaCelulares[marca]);
}