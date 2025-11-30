"""
* EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 """

import logging
def sumar(a, b):
    print(a + b)
    logging.info(f"se esta intentando sumar")
    logging.debug(f"el programa funciona joya")

def dividir(a, b):
    try:
        logging.warning(f"asegurese que el segundo numero no sea 0")
        print (a / b)
    except ZeroDivisionError:
        logging.error(f"esta intentando dividir por 0")
        logging.critical(f"deteniendo el programa") 

num = int(input("ingrese el numerador: "))
numero = int(input("ingrese el denominador: "))
sumar(num, numero)
dividir(num, numero)