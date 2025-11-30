"""
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
"""

import time
import random
import threading

def proceso_saludo(name: str, callback):
    print("Ejecutando proceso de saludo...")
    callback(name)

def proceso_callback(name: str):
    print(f"Hola, {name}")

proceso_saludo("Enzo", proceso_callback)

#extra
def proceso_orden(plato: str, callback_confirmacion, callback_listo, callback_entrega):
    def process():
        callback_confirmacion(plato)
        time.sleep(random.randint(1, 10))
        callback_listo(plato)
        time.sleep(random.randint(1, 10))
        callback_entrega(plato)
        time.sleep(random.randint(1, 10))
    threading.Thread(target=process).start()

def callback_confirmacion(plato: str):
    print(f"se confirma la reserva de tu plato de {plato}")

def callback_listo(plato: str):
    print(f"Tu pedido {plato}, esta listo: ")
    
def callback_entrega(plato: str):
    print(f"Tu pedido de {plato} fue entregado")


proceso_orden("fideos", callback_confirmacion, callback_listo, callback_entrega)
proceso_orden("hamburguesas", callback_confirmacion, callback_listo, callback_entrega)


