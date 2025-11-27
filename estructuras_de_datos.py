#   
# EJERCICIO:
# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.
#
# DIFICULTAD EXTRA (opcional):
# - Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# - y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más
# -  de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.

#tipos de datos
unInt = 1
unString = "hello world"
unFloat = 1.1
unBoolean = True
unFloat = 3.14
unaLista = ["sangre", "goat", 1, 89.1, True]
listaDesordenada = [7, 9, 0, 18, 391, 931, 92, 31, 43123, 777, 7777,1]
unDiccionario = {}
otroDiccionario = {
    "nombre": "enzo",
    "apodo": "sangre",
    "apellido": "goat",
    "edad": 21,
    "ciudad": "rosario",
    "peso": 89.3
}
unaTupla = (1, 5, 7, 8, 2)
listaDeTuplas = [(1, 2), (3, 4), (5, 6)]
unSet = {"Enzo", 34, "brasil", "king", 90.123, False}

#nota: la diferencia entre set y diccionario es que el set no tiene pares clave-valor, solo valores
#nota 2: la diferencia entre tupla y lista es que la tupla es inmutable, es decir, no se puede modificar

#operaciones de insercion, borrado, actualizacion y ordenacion
#listas
unaLista.append("enzo") #insercion
unaLista.remove("sangre") #borrado
print(unaLista[-2]) #acceso
print(unaLista)
print(listaDesordenada)
listaOrdenada = sorted(listaDesordenada)
print(listaOrdenada)
listaOrdenadaAlReves = listaOrdenada[::-1]
print(listaOrdenadaAlReves)
unaLista[2] = 3.141592653589793 #actualizacion
print(unaLista)

#diccionarios
otroDiccionario["edad"] = 22 #actualizacion
print(otroDiccionario)
otroDiccionario["ocupacion"] = "programador" #insercion
print(otroDiccionario)
print(otroDiccionario["nombre"])
sorted(otroDiccionario) #ordenacion
del otroDiccionario["ocupacion"] #borrado
print(otroDiccionario)

#tuplas
#nota: las tuplas no se pueden modificar con metodos como append o remove, pero podemos hacer lo siguiente:
tuplaConvertidaEnLista = list(unaTupla)
tuplaConvertidaEnLista.append(8)
tuplaConvertidaEnLista.remove(1)
tuplaConvertidaEnLista.sort()
tuplaConvertidaEnLista.reverse()
tuplaConvertidaEnLista[2] = 3.141592653589793 #actualizacion pero de la lista convertida en tupla
print(tuplaConvertidaEnLista)
print(unaTupla)
tuplaOrdenada = sorted(unaTupla) #ordenacion
print(tuplaOrdenada)
print(unaTupla[3]) #acceso

#sets
unSet.add("argentina") #insercion
print(unSet)
unSet.remove("brasil") #borrado
print(unSet)


# DIFICULTAD EXTRA (opcional):
# - Crea una agenda de contactos por terminal.
# - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
# - Cada contacto debe tener un nombre y un número de teléfono.
# - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
# - y a continuación los datos necesarios para llevarla a cabo.
# - El programa no puede dejar introducir números de teléfono no numéricos y con más
# -  de 11 dígitos (o el número de dígitos que quieras).
# - También se debe proponer una operación de finalización del programa.

def agenda():
    agenda = {}

    def insertar_contacto():
        nombre = input("Ingrese el nombre: ")
        telefono = input("Ingrese el numero de telefono: ")
        if telefono.isdigit() and len(telefono) <= 11:
            agenda[nombre] = telefono
        else: 
            print("Error: ingrese otro numero de telefono")
    def buscar_contacto():
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda:
            print(f"El numero de telefono de {nombre} es {agenda[nombre]}")
        else:
            print("Error: el nombre no se encuentra en la agenda")
    def actualizar_contacto():
        nombre = input("Ingrese el nombre del contacto que desea actualizar: ")
        if nombre in agenda:
            telefono = input("Ingrese el nuevo numero de telefono: ")
            if telefono.isdigit() and len(telefono) == 11:
                agenda[nombre] = telefono
            else: 
                print("Error: ingrese otro numero de telefono")
        else:
            print("Error: el nombre no se encuentra en la agenda")
    def eliminar_contacto():
        nombre = input("Ingrese el nombre del contacto que desea eliminar: ")
        if nombre in agenda:
            del agenda[nombre]
        else:
            print("Error: el nombre no se encuentra en la agenda")
    while True:
        print("\nMenu")
        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        opcion = input("Ingrese una opcion: ")
        match opcion:
            case "1": insertar_contacto()
            case "2": buscar_contacto()
            case "3": actualizar_contacto()
            case "4": eliminar_contacto()
            case "5": break
            case default: print("Error: opcion invalida")
agenda()
