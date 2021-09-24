# Laboratorio de Programacion

# Bienvenidos a nuestro      Repositorio

Antes de iniciar recuerda tener instalado:
* Git Bash
* Vs Code

Teniendo esto instalado comencemos.

Posiblemente te pareció abrumador 😨 este mundo de Git, no te preocupes es normal, ya que es un entorno en el cual no estamos familiarizados, pero créeme con su debido tiempo lo podrás dominar, siempre y cuando practiques y que le pierdas el miedo a equivocarte, experimentar y probar. 
> No hay **Especialización** sin **Repetición**  


## Comandos Básicos de Linux
Te estaré dejando una serie de comandos básicos  de Linux para que se te facilite este entorno 😎.

|Codigo|Uso  |
|--|--|
| pwd |Nos dará la ruta en la cual nos encontramos  |
| cd |Nos permitirá movernos entre las distintas carpetas    |
| cd ..|Nos regresara al directorio anterior  |
| ls |Nos dará un listado del contenido del directorio en el que nos encontremos   |
| ls -a |Nos mostrara los archivos ocultos  |
| mkdir |Nos permite crear una nueva carpeta  |
| touch |Nos permite crear un nuevo archivo  |
| cat |Nos permite ver un archivo pero sin modificarlo|
| diff |Nos mostrara las diferencias entre dos archivos línea por línea  |

Estos son solo algunos de los comandos mas básicos de Linux y no nos seria posible verlos todos durante las clases , así que animo busca mas y conviértete   en un experto de Linux 🐧.

###  ¿Por qué usar un sistema de control de versiones como Git?
>  Un sistema de control de versiones como Git nos ayuda a guardar el historial de cambios y crecimiento de los archivos de nuestro proyecto.

> Permite mantener un histórico de todo el desarrollo del proyecto. Añade trazabilidad al desarrollo de software, ya que se puede ver qué cambios se han hecho en el código en cada versión. Permite desarrollar varias versiones de un mismo programa a la vez.
###  Ciclo Basico de trabajo en Git
Cuando nosotros inicializamos un proyecto en git sucederán principalmente dos cosas.

* Nos creara un **repositorio local**
* Nos creara el **Staging area**


###  ¿Qué es el staging y los repositorios?                  
El **Staging** es el lugar de preparación en la RAM antes de enviar los cambios de nuestro archivo en **repositorio.** 

El **repositorio** es el lugar donde se almacenan los cambios de nuestro archivo.

## Comandos Basicos de Git
|Codigo|Uso  |
|--|--|
| git init |Iniciamos un proyeto Git  |
| git add |Agrega desde carpetas o únicamente archivos que indiques al área de Staging  |
| git commit -m |Crea una nueva versión en el repositorio con todos los cambios guardados. |
| git status | Muestra el estado actual del repositorio|
| git log |Muestra el historial de commits  |
| git show | Muestra, de forma muy detallada, los cambios ocurridos entre el commit actual y el commit anterior |

Una vez que agregamos algo al staging, y que queramos hacer nuestro primer commit  nos mandara esta alerta!!

![enter image description here](https://images3.programmerclick.com/647/2a/2ad431b2529fd14bc5b3f6c7836d55af.png)

Esto pasa por que aun no hemos realizado algunas configuraciones en Git. Para esto solo realizaremos estos comandos.

    git config --global user.name "tu usuario" 
 luego..
 
    git config --global user.email "tu correo"

Y listo ya podrás realizar tu primer commit.

## Realiza el clonado de este repositorio
El saber por completo git nos llevara tiempo,  mas que nada por que no hay mejor forma de aprender que poniendo en practica lo que ya sabemos y por que son muchas las cosas que podemos hacer.
 Y es que de hecho esto que hemos estado realizando son algunas de las tareas de realiza un ingeniero de   Devops.
Pero con lo que ya sabemos por ahora es suficiente para trabajar en clase.

Así que lo único que tendrás que hacer es lo siguiente:
 

 1. Crear una nueva carpeta e inicializar un nuevo  proyecto Git
 2. Ya en el repositorio que quiera clonar, en el botón de código, copiaras el link del protocolo https



![enter image description here](https://miro.medium.com/max/1838/1*eO9a9lslGKBePNj8_CQG-w.jpeg)

3. En tu terminal lo único que harás es escribir este código:

	    git clone "codigo que copiaste"

4. Ahora cada que en el repositorio se agregue algo nuevo, en su consola pondran este codigo:

		git pull origin master 

si hay problemas entre las historias podemos poner:	

    git pull origin --allow-unrelated-histories

