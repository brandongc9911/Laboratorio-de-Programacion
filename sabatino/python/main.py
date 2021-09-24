
# Variables en Python
edad =  18
print(edad)

# Cuando trabajamos con string, o arrays(listas y tambien las tuplas) python les da un indice a cada elemento. Algo en tener en cuenta es que la manera en que enumera
# es apartir del 0. Recuerda los idices python los maneja como n-1, esto quiere decir que el elemento que tengamos le resta 1.
# 0,1,2,3,4,5
# -6,-5,-4,-3,-2,-1



palabra = 'Programacion'

# Accediendo a un elemento individualmente
print(palabra[3])

#Accediendo a una porcion (slice)
print(palabra[0:3])

#Reaccinado valor de un indice
palabra[2] = 'O'
print(palabra)


# lista
lista = [1,2,3,4,5] # mutable

# tupla
lista2 = (1,2,3,4,5) # no mutable

print(type(lista))
print(type(lista2))

# Tanto las listas y las tuplas podemos acceder a ellas indidivualmente y por slices 




# concatenacion
palabra = 'Hola'
palabra2 = 'Mundo'
print(palabra + ' ' + palabra2)



# Manera de iterar un numero en python
numero = 1
numero += 1

print(numero)


# Covertir tipo de datos en Python
numero = 5
numero2 = "5"

print(numero + int(numero2))
