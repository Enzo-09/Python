""""
* EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 """



try:
    print(10/0)
except Exception as error:
    print(f"no se puede dividir por 0, ya que tenemos un error del tipo {error}")

miLista = ["enzo", "hello world", 69]
try:
    miLista[5]
except Exception as error:
    print(f"no se puede acceder a ese indice, ya que tenemos un error del tipo {error}")


#extra

class errorTipoString(Exception):
    pass

def procesar_parametros(parametros: list):
    if len(parametros) < 3:
        raise IndexError()
    elif parametros[1] == 0:
        raise ZeroDivisionError
    elif type(parametros[2]) == str:
        raise errorTipoString ("el tercer elemento no puede ser una cadena de texto")
    print(parametros[2])
    print(parametros[0]/parametros[1])
    print(parametros[2]+5)

try:
    procesar_parametros([1,2,3,4])
except IndexError as error:
    print("el numero de elementos en la lista debe ser mayor que 2")
except ZeroDivisionError as error:
    print("el segundo elemento de la lista no puede ser un 0")
except errorTipoString as error:
    print(f"{error}")
else:
    print("no se ha producido ningun error")
finally:
    print("el programa finaliza sin detenerse")
#nota: probado y funciona :)