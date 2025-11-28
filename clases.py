""""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 """

class programador:
    apellido = None

    def __init__(self, name: str, age: int, lenguajes: list):
        self.name = name
        self.age = age
        self.lenguajes = lenguajes
        
    def print(self):
        print(f"Nombre: {self.name}, Apellido: {self.apellido}, lenguajes: {self.lenguajes}")
programador_1 = programador("Enzo",21,["python", "typescript", "react"])
programador_1.print()
programador_1.apellido = "Ferrari"
programador_1.print()

#Extra
class pila:
    def __init__(self):
        self.pila = []
    
    def push(self, item):
        self.pila.append(item)

    def pop(self):
        if self.pila.count == 0:
            return None
        return self.pila.pop()
    
    def count(self):
        return len(self.pila)
    
    def print(self):
        for item in reversed(self.pila):
            print(pila)

pila = pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila.count)
pila.print()
pila.pop()
#me quede sin ganas de terminarlo xd