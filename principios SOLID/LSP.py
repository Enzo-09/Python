"""
* EJERCICIO:
 * Explora el "Principio SOLID de Sustitución de Liskov (Liskov Substitution Principle, LSP)"
 * y crea un ejemplo simple donde se muestre su funcionamiento
 * de forma correcta e incorrecta.
 """

# Incorrecto


class Bird:
    def fly(self):
        return "Flying"


class Chicken(Bird):
    def fly(self):
        raise Exception("Los pollos no vuelan")
# Correcto

class Bird:
    def move(self):
        return "Moving"


class Chicken(Bird):
    def move(self):
        return "Walking"


bird = Bird()
print(bird.move())
chicken = Chicken()
print(chicken.move())

bird = Chicken()
print(bird.move())
chicken = Bird()
print(chicken.move())


"""
 * DIFICULTAD EXTRA (opcional):
 * Crea una jerarquía de vehículos. Todos ellos deben poder acelerar y frenar, así como
 * cumplir el LSP.
 * Instrucciones:
 * 1. Crea la clase Vehículo.
 * 2. Añade tres subclases de Vehículo.
 * 3. Implementa las operaciones "acelerar" y "frenar" como corresponda.
 * 4. Desarrolla un código que compruebe que se cumple el LSP.
 """

class vehiculo:
    def __init__(self, velocidad: str):
        self.velocidad = velocidad
    def acelerar(self, aumento):
        self.velocidad += aumento
        print(f"acelera {aumento} km/h")
    def frenar(self, decremento):
        self.velocidad -= decremento
        if self.velocidad <= 0:
            self.velocidad = 0
        print(f"el auto se tiene una velocidad de {self.velocidad} km/h")


class auto(vehiculo):
    def acelerar(self, aumento):
        print("el auto esta acelerando")
        super().acelerar(aumento)
    def frenar(self, decremento):
        print("el auto esta frenando")
        super().frenar(decremento)


class moto(vehiculo):
    def acelerar(self, aumento):
        print("la moto esta acelerando")
        super().acelerar(aumento)
    def frenar(self, decremento):
        print("la moto esta frenando")
        super().frenar(decremento)

class camion(vehiculo):
    def acelerar(self, aumento):
        print("el camion esta acelerando")
        super().acelerar(aumento)
    def frenar(self, decremento):
        print("el camion esta frenando")
        super().frenar(decremento)


un_auto = auto(230)
un_auto.acelerar(20)
un_auto.frenar(100)
una_moto = moto(32)
una_moto.acelerar(10)
una_moto.frenar(50)
un_camion = camion(30)
un_camion.acelerar(2)
un_camion.frenar(2)