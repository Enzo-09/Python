"""
* EJERCICIO:
 * Utilizando tu lenguaje, crea un programa capaz de ejecutar de manera
 * asíncrona una función que tardará en finalizar un número concreto de
 * segundos parametrizables. También debes poder asignarle un nombre.
 * La función imprime su nombre, cuándo empieza, el tiempo que durará
 * su ejecución y cuando finaliza.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando el concepto de asincronía y la función anterior, crea
 * el siguiente programa que ejecuta en este orden:
 * - Una función C que dura 3 segundos.
 * - Una función B que dura 2 segundos.
 * - Una función A que dura 1 segundo.
 * - Una función D que dura 1 segundo.
 * - Las funciones C, B y A se ejecutan en paralelo.
 * - La función D comienza su ejecución cuando las 3 anteriores han finalizado.
 """

import asyncio
import datetime

async def func_asinc(name: str, duracion:int):
    print(f"Tarea: {name}, duracion: {duracion} segundos, Inicio: {datetime.datetime.now()}")
    await asyncio.sleep(duracion)
    print(f"tarea:{name}, fin:{datetime.datetime.now()}")
asyncio.run(func_asinc("lol",4))

#Extra

async def async_func_asinc():
    await asyncio.gather(func_asinc("c", 3),func_asinc("b", 2), func_asinc ("a", 1))
    await func_asinc("d", 1)

asyncio.run(async_func_asinc())