import random

mayusculas = ['A','B','C','D','F','G']
minusculas = ['a','b','c','d','f','g']
numero = ['1','2']
caracteres = ['#','%','!', '?']

conjunto = mayusculas + minusculas + numero + caracteres

nueva = []

def generadorContraseña():
    for i in range(8):
        aleatorio = random.choice(conjunto)
        nueva.append(aleatorio)
    
    guardar = "".join(nueva)
    return guardar





contrasena = generadorContraseña()
print(contrasena)

# if  __name__== '__main__':
#     contrasena = generadorContraseña()
#     print(contrasena)