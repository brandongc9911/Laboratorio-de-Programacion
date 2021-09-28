
import random

mayusculas = ['A','B','C','D','F','G']
minusculas = ['a','b','c','d','f','g']
numero = ['1','2','3','4','5']
caracteres = ['#','%','!', '?']

conjunto = mayusculas + minusculas + numero + caracteres

numero = []

def crearContrasena():
    for i in range(8):
        aletorio = random.choice(conjunto)
        numero.append(aletorio)
    nuevaContra = ''.join(numero)
    return nuevaContra



print(__name__)

if __name__ == '__main__':
    contra = crearContrasena()
    print(f'Esta es tu nueva {contra}')
else:
    print('Este es un archivo importado')



