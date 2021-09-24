// 'use strict';


// Ejemplos de var,const y let
var edad1 = 18
const edad2 = 18

edad1 = 20
edad2 = 20

console.log(edad1)
console.log(edad2)


let edad3 = 18

edad3 = 20

console.log(edad3)


var palabra = 'Programacion'

// Acceder individualmente a una letra del string
console.log(palabra[0])

// Acceder por una porcion del string
console.log(palabra.slice(0,3))


// Lista
var lista = [1,2,3,4,5]

lista[0] = 0

// Mejora visual en terminal con console.log - Crea una tabla
console.table(lista)



// concatenacion
var palabra = 'Hola'
var palabra2 = 'Mundo'

console.log(`${palabra}` +  ' ' +  `${palabra2}`)


var numero = 3


// iterar un numero en JS
numero++
++numero
console.log(numero)



// Tipos de datos 
var numero = 5
var numero2 = '5'

console.log(typeof(numero))
console.log(typeof(numero2))


console.log(numero * numero2)


var resultado = numero * numero2

console.log(typeof(resultado))



console.log(numero === numero2)


console.log(parseInt(numero2))
console.log(String(numero))


// Objetos 

// object literal
const producto = {
    nombre: 'Computadora',
    precio: 20000,
    memororia: '1tb',
    so: '11'
}

const producto2 = {
    nombre: 'Laptop',
    precio: 20000,
    memororia: '1tb',
    so: '11'
}

// Cuando trabajamos con objetos si el objeto se declara con const aun se puede modificar, hay metodos que nos ayudar a obligarlo a no cambiar


// Object.freeze(producto) -- No permite cambiar nada del objeto
// console.log(Object.isFrozen(producto))

// object.seal(product) --permite unicamente modificar los  datos existentes del objeto


// console.log(producto.memororia = '20gb' )



// Object destructuring
// const {nombre} = producto
// console.log(nombre)



var res = Object.assign(producto,producto2)

console.table(res)





