import random

mayusculas = ['A','B','C','D','F','G']
minusculas = ['a','b','c','d','f','g']
numero = ['1','2']
caracteres = ['#','%','!', '?']

conjunto = mayusculas + minusculas + numero + caracteres

nueva = []

def generadorContrasena():
    for i in range(12):
        aleatorio = random.choice(conjunto)
        nueva.append(aleatorio)
    
    guardar = "".join(nueva)
    return guardar



def guardar(contrasena):
    nombre = input(str('Para que utilizaras esta contraseña: '))
    with open('nocturno/contrasenas.txt','a',encoding='utf-8') as data:
        data.write(f'{nombre}: {contrasena}')
        data.write('\n')
        data.close()



if __name__ == '__main__':
    contrasena = generadorContrasena()
    guardar(contrasena)
   
    

