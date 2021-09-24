# carrera =  input('Cual es tu carrera: ')

# if carrera == 'Sistemas':
#     print('Los alumnos de ' + carrera + ' ' + 'estudian programacion para crear software')

# elif carrera == 'Mecatronica':
#     print('Los alumnos de ' + carrera + ' ' + 'estudian programacion para darle instrucciones a los robots')

# else:
#     print('No estudian programacion')

# numpaginas = 200

# for i in range(1, numpaginas+1):
#     if i % 2 == 0:
#         print('La pagina: ' + str(i) + ' ' + 'Contiene un problema') 


leerpagina = input('Digite una letra: ')
contador = 1
listaProblemas = []
while leerpagina != 'X':
    print('Estas en la  pagina: ' + str(contador))
    leerpagina = input('Digite una letra: ')
    if contador % 2 == 0:
        print('La pagina: ' + str(contador) + ' ' + 'Contiene un problema')
        listaProblemas.append(contador)
    contador +=1

print(listaProblemas)

