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


def guardar(data):
    with open("contraseñas.txt","a",encoding="utf-8") as f:
        f.write('Contraseña: ' + data)
        f.write("\n")
        f.close()


if __name__ == '__main__':
    contraseña = generadorContraseña()
    guardar(contraseña)
    

