"""
 * EJERCICIO:
 * Explora el "Principio SOLID Abierto-Cerrado (Open-Close Principle, OCP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
"""
from abc import ABC, abstractmethod

class notificador:
    @abstractmethod
    def enviar(self, mensaje: str):
        pass

class email(notificador):
    def enviar(self, mensaje):
        print(f"enviando EMAIL: {mensaje}")

class whatsapp(notificador):
    def enviar(self, mensaje):
        print(f"enviando WHATSAPP: {mensaje}")

#si quiero agregar otro tipo de mensaaje, creo otra clase y no tengo que cambiar mi codigo

class gestorNotificaciones:
    def notificar(self, canal: notificador, mensaje: str):
        canal.enviar(mensaje)

notificador_1 = gestorNotificaciones()
notificador_1.notificar(email(), "email de prueba")
notificador_1.notificar(whatsapp(), "whatsapp hello world")


"""
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla una calculadora que necesita realizar diversas operaciones matemáticas.
 * Requisitos:
 * - Debes diseñar un sistema que permita agregar nuevas operaciones utilizando el OCP.
 * Instrucciones:
 * 1. Implementa las operaciones de suma, resta, multiplicación y división.
 * 2. Comprueba que el sistema funciona.
 * 3. Agrega una quinta operación para calcular potencias.
 * 4. Comprueba que se cumple el OCP.
"""

class calculadora:
    @abstractmethod
    def operacion(self, a, b):
        pass

class suma(calculadora):
    def operacion(self, a, b):
        return a + b

class resta(calculadora):
    def operacion(self, a, b):
        return a - b
    
class multiplicacion(calculadora):
    def operacion(self, a, b):
        return a * b
    
class division(calculadora):
    def operacion(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as error:
            print(f"no se puede dividir por 0 {error}")

class potencia(calculadora):
    def operacion(self, a, b):
        return a ** b

class funciona:
    def __init__(self):
        self.operacion = {}
    def agregar_operacion(self, nombre, operacion):
        self.operacion[nombre] = operacion
    def calcular(self,nombre, a, b):
        if nombre not in self.operacion:
            raise ValueError (f"la operacion {nombre} no esta autorizada")
        return self.operacion[nombre].operacion(a, b)

# Ejemplos de uso de la calculadora
calc = funciona()
calc.agregar_operacion("suma", suma())
calc.agregar_operacion("resta", resta())
calc.agregar_operacion("multiplicacion", multiplicacion())
calc.agregar_operacion("division", division())
calc.agregar_operacion("potencia", potencia())

print("Suma 10 + 5:", calc.calcular("suma", 10, 5))
print("Resta 10 - 5:", calc.calcular("resta", 10, 5))
print("Multiplicación 10 * 5:", calc.calcular("multiplicacion", 10, 5))
print("División 10 / 5:", calc.calcular("division", 10, 5))
print("Potencia 2 ** 3:", calc.calcular("potencia", 2, 3))
print("División por cero:", calc.calcular("division", 10, 0))
    
