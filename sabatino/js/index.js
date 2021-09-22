// 'use strict';
// var edad1 = 18
// const edad2 = 18

// edad1 = 20
// // edad2 = 20

// console.log(edad1)
// console.log(edad2)


// let edad3 = 18

// edad3 = 20

// console.log(edad3)


// var palabra = 'Programacion'

// console.log(palabra[0])

// console.log(palabra.slice(0,3))


// var lista = [1,2,3,4,5]

// lista[0] = 0

// console.table(lista)




var palabra = 'Hola'
var palabra2 = 'Mundo'


console.log(`${palabra}` +  ' ' +  `${palabra2}`)


var numero = 3

// numero++
// ++numero
// console.log(numero)


var numero = 5
var numero2 = '5'

console.log(typeof(numero))
console.log(typeof(numero2))


// console.log(numero * numero2)


// var resultado = numero * numero2

// console.log(typeof(resultado))



// console.log(numero === numero2)


// console.log(parseInt(numero2))
// console.log(String(numero))


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
// Object.freeze(producto)
// console.log(Object.isFrozen(producto))

// object.seal(product)
// console.log(producto.memororia = '20gb' )


// const {nombre} = producto
// console.log(nombre)



var res = Object.assign(producto,producto2)

console.table(res)





