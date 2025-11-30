"""
 * EJERCICIO:
 * Explora el "Principio SOLID de Segregación de Interfaces
 * (Interface Segregation Principle, ISP)", y crea un ejemplo
 * simple donde se muestre su funcionamiento de forma correcta e incorrecta.
"""

from abc import ABC, abstractmethod

# Sin ISP


class WorkerInterface(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Human(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")

class Robot(WorkerInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        # Los robots no comen
        pass


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()
robot.eat()  # error

# Con ISP


class WorkInterface(ABC):

    @abstractmethod
    def work(self):
        pass


class EatInterface(ABC):

    @abstractmethod
    def eat(self):
        pass


class Human(WorkInterface, EatInterface):

    def work(self):
        print("Trabajando")

    def eat(self):
        print("Comiendo")


class Robot(WorkInterface):

    def work(self):
        print("Trabajando")


human = Human()
human.work()
human.eat()

robot = Robot()
robot.work()



"""
 * DIFICULTAD EXTRA (opcional):
 * Crea un gestor de impresoras.
 * Requisitos:
 * 1. Algunas impresoras sólo imprimen en blanco y negro.
 * 2. Otras sólo a color.
 * 3. Otras son multifunción, pueden imprimir, escanear y enviar fax.
 * Instrucciones:
 * 1. Implementa el sistema, con los diferentes tipos de impresoras y funciones.
 * 2. Aplica el ISP a la implementación.
 * 3. Desarrolla un código que compruebe que se cumple el principio.
 """

class impresion_normal(ABC):
    @abstractmethod
    def print(self, documento):
        pass

class impresion_color(ABC):
    @abstractmethod
    def print_color(self, documento):
        pass

class escanear(ABC):
    @abstractmethod
    def scan(self, documento):
        pass

class fax(ABC):
    @abstractmethod
    def fax(self, documento):
        pass

class impresora_basica(ABC):
    def print(self, documento):
        print(f"se esta imprimiendo el {documento}")

class impresora_color(ABC):
    def print(self, documento):
        print(f"se esta imprimiendo el {documento}")
    def print_color(self, documento):
        print(f"se esta imprimiendo el {documento} a color")

class impresora_mutlifuncion(ABC):
    def print(self, documento):
        print(f"se esta imprimiendo el {documento}")
    def print_color(self, documento):
        print(f"se esta imprimiendo el {documento} a color")
    def scan(self, documento):
        print(f"se esta scaneando el {documento}")
    def fax(self, fax):
        print(f"enviando el {fax}")

basica = impresora_basica()
basica.print("documento 1")
color = impresora_color()
color.print("documento 2")
color.print_color("documento 2 a color")
multifuncion = impresora_mutlifuncion()
multifuncion.print("documento 3")
multifuncion.print_color("documento 3 a color")
multifuncion.scan("documento a scanear")
multifuncion.fax("documento de fax")