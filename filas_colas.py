"""
 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

#ejercicio
lista_prueba = [12, 34, 431, 13241, 123]
print(lista_prueba[-1])
print(lista_prueba[0])
lista_prueba.pop()
print(lista_prueba)


""" 
* - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
"""

#ejercicio extra 1
def navegacion():
    pila = []

    while True:
        accion = input("agrega una URL o interactua con las palabras adelante/atras/salir:")

        if accion == "salir":
            print("saliendo del navegador web")
            break
        elif accion == "adelante":
            pass
        elif accion == "atras":
            if len(pila) > 0:
                pila.pop()
        else:
            pila.append(accion)
        if len(pila) > 0:
            print(f"has navegado a la web correctamente")
        else:
            print("estas en la pagina de inicio")
navegacion()


#ejercicio extra 2
""" 
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""

def impresion():
    colaImpresion = []
    while True:
        unaPalabra = input("ingrese un documento, si quiere imprimir, escriba la palabra imprimir, si quiere salir escriba salir:")
        if unaPalabra == "salir":
            print("saliendo del programa")
            break
        if unaPalabra == "imprimir":
            print("documento impresos correctamente, no hay documentos en espera")
            colaImpresion = []
            break
        else:
            print("documento agregado a la cola")
            colaImpresion.append(unaPalabra)
        
    print(colaImpresion)

impresion()
        
#nota: lo hice asi suponiendo al escribir imprimir, se imprimen todo los documentos de la cola, por eso vacio la cola pero no la elimino