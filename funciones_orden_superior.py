"""
* EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
"""

# Funcion de orden superior, que recibe otra funcion
def aplicar_funcion(funcion, num1, num2):
    return funcion (num1, num2)

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


print (aplicar_funcion(suma, 8, 7))
print (aplicar_funcion(resta, 10, 2))

"""
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
"""
from functools import reduce
from datetime import datetime

#extra
alumnos = [
    {"nombre": "Enzo", "cumple": "09-08-2004", "notas": [9, 10, 10, 8]},
    {"nombre": "John", "cumple": "12-12-2012", "notas": [1, 2, 3, 4]},
    {"nombre": "Luffy", "cumple": "03-01-2020", "notas": [3, 10, 10, 1]},
    {"nombre": "Gohan", "cumple": "09-05-2001", "notas": [9, 4, 6, 8]},
    {"nombre": "Washinton", "cumple": "04-11-2009", "notas": [10, 10, 10, 10]},
    ]

def promedio(notas):
    return sum(notas) / len(notas)

print(
    list(map(lambda alumnos: {
        "nombre": alumnos["nombre"],
        "promedio": promedio(alumnos["notas"])}, alumnos)
    )
)

print(
    list(map(lambda alumnos:
        alumnos["nombre"],
        filter(lambda alumnos: promedio(alumnos["notas"]) >=9, alumnos)
)
)
)

print(sorted(alumnos, key=lambda alumnos: datetime.strptime(alumnos["cumple"],"%d-%m-%Y"), reverse=True))
print(max(map(lambda alumnos: max(alumnos["notas"]), alumnos)))

