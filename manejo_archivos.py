import os
"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 """

"""
file_name = "Enzo-09.txt"

with open (file_name, "w") as file:
    file.write("Enzo")
    file.write("21")
    file.write("Python")
with open(file_name, "r") as file:
    print(file.read())
os.remove(file_name)
"""

"""
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 """
# ejercicio extra
file_name = "gestion_ventas.txt"
open (file_name, "a")


while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar producto")
    print("4. Borrar producto")
    print("5. Mostrar productos")
    print("6. Calcular venta total")
    print("7. Calcular venta por producto")
    print("8. Salir")

    option = input("Selecciona una opción: ")

    match option:
        case "1":
            name = input("ingrese el nombre del producto: ")
            cantidad = input("ingrese la cantidad vendida: ")
            precio = input ("ingrese el precio del producto: ")
            with open (file_name, "a") as file:
                file.write(f"{name}, {cantidad}, {precio}")
        case "2": 
            name = input("nombre:")
            with open(file_name, "r") as file:
                for line in file.readlines():
                    if line.split(", ")[0] == name:
                        print(line)
                        break
        case "3": #no funciona
            parametro = input("ingrese el parametro del producto que desea actualizar")
            if parametro == "nombre":
                name = input("ingrese el nuevo nombre")
            elif parametro == "cantidad":
                cantidad = input("ingrese la cantidad nueva")
            elif parametro == "precio":
                precio = input("ingrese el nuevo precio")
            else:
                break
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] == name:
                        file.write(f"{name}, {parametro}, {cantidad}")
                    else:
                        file.write(line)
        case "4":
            name = input("Nombre: ")
            with open(file_name, "r") as file:
                lines = file.readlines()
            with open(file_name, "w") as file:
                for line in lines:
                    if line.split(", ")[0] != name:
                        file.write(line)
        case "5":
            with open(file_name, "r") as file:
                print(file.read())
        case "6":
            total == 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    cantidad = int(components[1])
                    precio = int(components[2])
                    total += cantidad * precio
                print (total)
        case "7":
            name = input("Nombre: ")
            total = 0
            with open(file_name, "r") as file:
                for line in file.readlines():
                    components = line.split(", ")
                    if components[0] == name:
                        quantity = int(components[1])
                        price = float(components[2])
                        total += quantity * price
                        break
        case "8":
            os.remove(file_name)
            break
