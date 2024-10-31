# Proyecto del Día 6
# Llegó el momento de poner todo lo que hemos aprendido en un proyecto del mundo real. Y el
# de hoy sí que nos va a tomar tiempo, porque a pesar de ser relativamente simple, implica mucho
# código, muchas funciones y es imprescindible llevar una especie de orden mental de lo que
# necesitas hacer. Hoy vas a crear un administrador de recetas. Básicamente esto es un programa
# a través del cual un usuario puede leer, crear y eliminar recetas que se encuentren en una base
# de datos.
# Entonces, antes de comenzar, es necesario que crees en tu ordenador un directorio en la carpeta
# base de tu ordenador, con una carpeta llamada Recetas, que contiene cuatro carpetas y cada
# una de ellas contiene dos archivos de texto. Dentro de los archivos puedes escribir lo que
# quieras, puede ser la receta en sí misma o no, pero eso no es importante para este ejercicio. Lo
# importante es que escribas algo para poder leerlas cuando haga falta o, si prefieres, también
# puedes directamente descargar y descomprimir el archivo adjunto a esta elección y ubicarlo en
# tu directorio raíz si no tienes ganas de crearlo tú mismo.
# Aquí viene la consigna: tu código le va a dar primero la bienvenida al usuario, le va a informar
# la ruta de acceso al directorio donde se encuentra nuestra carpeta de recetas, le va a informar
# cuántas recetas hay en total dentro de esa carpeta, y luego le va a pedir que elija una de
# estas opciones que tenemos aquí:
# 1. La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que
# el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.
# 2. En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que
# escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va
# a crear ese archivo en el lugar correcto.
# 3. La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar
# una carpeta nueva con ese nombre.
# 4. La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va
# a eliminar
# 5. La opción 5, le va a preguntar qué categoría quiere eliminar
# 6. Finalmente, la opción 6 simplemente va a finalizar la ejecución del código.
# Este programa tiene algunas cuestiones importantes a considerar:
#  Cada vez que el usuario realice exitosamente cualquiera de sus opciones, el programa le
# va a pedir que presione alguna letra para poder volver al inicio, por lo que el código se

# va a repetir una y otra vez, hasta que el usuario elija la opción 6. Esto implica que todo
# el menú debe estar dentro de un loop while que se repita una y otra vez hasta que no se
# cumpla la condición de que la elección del usuario sea 6
#  Sería genial que cada vez que el usuario vuelva al menú inicial, la consola limpie la
# pantalla para que no se acumulen las ejecuciones anteriores. Recuerda que cuentas con
# system para poder reiniciar la pantalla y comenzar a mostrar todo desde cero.
#  Si bien te he enseñado muchos métodos para administrar archivos, para este ejercicio
# vas a necesitar algunos que aún no has visto, pero que están incluidos en los objetos con
# los que hemos estado trabajando, por lo que en ocasiones deberás buscar entre los
# métodos que trae Path, por ejemplo, leer la documentación y aprender a implementarlo.
# Yo sé que sería mucho más fácil que yo te enseñe todo acerca de cada uno de los
# métodos, pero recuerda que también es importante que a medida que avanzamos vayas
# aprendiendo a gestionar tu propio aprendizaje. Es parte de la vida real y cotidiana del
# programador en el mundo en que vivimos.
#  Utiliza muchas funciones, todas las que creas necesario. Las funciones ayudan a
# compartir, mentalizar el código y hacerlo mucho más dinámico, ordenado, repetible y
# más fácil de mantener.
#  Recuerda comenzar con un diagrama de flujos o un gráfico hecho a mano que te permita
# visualizar con más facilidad el árbol de decisiones que necesitas ejecutar en tu código.
# Sin eso te vas a enredar más rápido de lo que crees y se te va a complicar bastante.
#  Y, por último, no te frustres si no logras hacerlo o completarlo. Si logras hacer una parte,
# un par de funciones, algunas cosas sí y otras no, está muy bien. Siempre estamos
# aprendiendo y parte de aprender es no saber.
# Mis desafíos siempre te van a estar ubicando en el borde de tus capacidades, sacándote del
# lugar de confort para que tu cerebro tenga que desconcertarse y descubrir cómo hacer algo
# nuevo. Tu avanza hasta donde puedas.

import os

from pathlib import Path

def abrir_leer(archivo):
    mi_archivo = open(archivo,"r")
    print(mi_archivo.read())
    mi_archivo.close()

ruta_acceso = os.getcwd()

ruta_recetas = Path(ruta_acceso,"Recetas")
os.system("cls")
print(f"""
Bienvenido al organizador de recetas

La ruta de acceso al directorio de recetas es: 
{ruta_recetas}
""")

def menu():
    opcion = int(input("""
Que desea hacer?

1) Leer una receta
2) Ingresar una nueva receta
3) Crear una categoría
4) Eliminar receta
5) Eliminar categoría
6) Salir \n

"""))
    
    if opcion > 0 and opcion < 7:
        os.system("cls")
        return opcion
    else:
        print("Opción incorrecta")
        
# def leer_una_receta(ruta):

def listar_categorias(dir):
         
    dir = Path(dir)
    entries = dir.glob("*")
    files = [f for f in entries if f.__dir__]
    nombres_carpetas = []
    
    for path in files:
        nombres_carpetas.append(path.name)
        
    return nombres_carpetas
        
    
def elegir_categorias(dir):
    os.system("cls")
    
    print("Categorías: \n \n")
    dir = Path(dir)
    entries = dir.glob("*")
    files = [f for f in entries if f.__dir__]
    nombres_carpetas = []
    
    for path in files:
        nombres_carpetas.append(path.name)
        
    for categoria in list(enumerate(nombres_carpetas,1)):
        
        print(f"{categoria[0]}) {categoria[1]}")
        
    categoria_elegida = input("Elija una categoría:\n \n")
    directorio_carpeta_seleccionada = (f"{dir}\{nombres_carpetas[int(categoria_elegida)-1]}") 
    nombre = nombres_carpetas[int(categoria_elegida)-1]
    
    return directorio_carpeta_seleccionada , nombre



# def elegir_categorias(lista):
#     for categoria in list(enumerate(lista,1)):
        
#         print(f"{categoria[0]}) {categoria[1]}")
#     categoria_elegida = input("Elija una categoría: ")
    
#     return categoria_elegida
        
def elegir_archivos(dir):
    os.system("cls")
    
    print("Recetas: \n \n")
    dir = Path(dir)
    entries = dir.glob("*.txt")
    files = [f for f in entries if f.__dir__]
    nombre_archivos = []
    
    for path in files:
        nombre_archivos.append(path.name.replace(".txt",""))
    
    for archivo in list(enumerate(nombre_archivos,1)):
        
        print(f"{archivo[0]}) {archivo[1]}")
    archivo_elegido = input("Elija una receta: \n \n ")
    
    
    # directorio_archivo_seleccionado = (f"{dir}\{nombre_archivos[int(archivo_elegido)-1]}.txt") 
    
    nombre_seleccionado = nombre_archivos[int(archivo_elegido)-1]
    
    
    directorio_archivo_seleccionado = (f"{nombre_seleccionado}.txt") 
    
    return directorio_archivo_seleccionado,nombre_seleccionado

def abrir_leer(dir,archivo):
    os.chdir(dir)
    mi_archivo = open(archivo,"r")
    print(mi_archivo.read())
    mi_archivo.close()
    
def crear_archivo(dir,nombre_archivo,contenido):
    os.chdir(dir)
    mi_archivo = open(nombre_archivo+".txt","w")
    print(mi_archivo.write(contenido))
    mi_archivo.close()
    
def leer_receta(dir):

    os.system("cls")

    categorias_selec = elegir_categorias(dir)[0]
    
    archivo_selec = elegir_archivos(categorias_selec)[0]

    os.system("cls")
    abrir_leer(categorias_selec,archivo_selec)
    
    
def ingresar_receta(dir):
    
    categorias_selec = elegir_categorias(dir)[0]
    
    nombre_receta = input("Ingrese el nombre de la receta a crear: \n")
    
    contenido_receta = input("Ingrese el contenido de la receta: \n")
    
    crear_archivo(categorias_selec,nombre_receta,contenido_receta)
    os.system("cls")
    
    print(f"La receta {nombre_receta} ha sido creada exitosamente")

def ingresar_categoria(dir):
    
    categoria_nueva = input("Ingrese el nombre de categoría que desea crear: \n")
    
    ruta_nueva = dir.joinpath(categoria_nueva)
    os.makedirs(ruta_nueva)
    
    os.system("cls")
    
    print(f"La categoría {categoria_nueva} fue creada correctamente")

def eliminar_archivo(dir,nombre_archivo):
    os.chdir(dir)
    os.remove(nombre_archivo)
    
def eliminar_receta(dir):
    print("A qué categoría pertenece la receta que desea eliminar?")
    
    categorias_selec = elegir_categorias(dir)[0]
    
    archivo_selec,nombre_selec = elegir_archivos(categorias_selec)
    
    ruta_de_archivo_a_eliminar = categorias_selec
        
    respuesta = input(f"Estás seguro que deseas eliminar la receta: {nombre_selec}? (s/n) \n \n")
    
    if respuesta == "s" or  respuesta == "S":
        eliminar_archivo(ruta_de_archivo_a_eliminar,archivo_selec)
        os.system("cls")
        print(f"Se ha eliminado correctamente la receta {nombre_selec}")
    else:
        print("No se eliminó ninguna receta")
        
    
def eliminar_categoría(dir):
    
    print("Que categoría desea eliminar? \n")
    
    categoria_eliminar,nombre = elegir_categorias(dir)
    
    respuesta = input(f"Estás seguro que deseas eliminar la categoría: {nombre}? (s/n)\n")
    
    if respuesta == "s" or  respuesta == "S":
        os.rmdir(categoria_eliminar)
        os.system("cls")
        print(f"Se ha eliminado correctamente la categoría {nombre}")
    else:
        print("No se ha eliminado ninguna categoría")
    
    
def ending():
    respuesta = input("\n \nPresione Enter para volver al menú")
        
        
        
opcion = 0
while opcion != 6:
    opcion = menu()
    
    match opcion:
        case 1:
            leer_receta(ruta_recetas)
            ending()
            os.system("cls")
        case 2:
            ingresar_receta(ruta_recetas)
            ending()
            os.system("cls")
        case 3:
            ingresar_categoria(ruta_recetas)
            ending()
            os.system("cls")
        case 4:
            eliminar_receta(ruta_recetas)
            ending()
            os.system("cls")
        case 5:
            eliminar_categoría(ruta_recetas)
            ending()
            os.system("cls")
        case _:
            continue


os.system("cls")
print("""
Muchas gracias por utilizar nuestro programa!


     ***********                  ***********
  *****************            *****************
*********************        *********************
***********************      ***********************
************************    ************************
*************************  *************************
 **************************************************
  ************************************************
    ********************************************
      ****************************************
         **********************************
           ******************************
              ************************
                ********************
                   **************
                     **********
                       ******
                         **


""")
