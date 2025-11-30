"""
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
"""

import requests

my_URL = requests.get("https://www.google.com/")
if my_URL.status_code == 200:
    print(my_URL.text)
else:
    print(f"error con codigo {my_URL.status_code} al realizar la peticion")


#extra
pokemon = input("ingresa el nombre del pokemon que desea buscar: ")
response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/")
data = response.json()
print("nombre:", data["name"])
print("id:", data["id"])
print("peso", data["weight"])
print("altura", data["height"])
print("Tipo(s):" )
for type in data["types"]:
    print(type["type"]["name"])
print("juegos:")
for game in data["game_indices"]:
    print(game["version"]["name"])
response = requests.get (f"https://pokeapi.co/api/v2/pokemon-species/{pokemon}/")
if response.status_code == 200:
    url = response.json()["evolution_chain"]["url"]
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("cadena de evolucion")
        def get_evolves(data):
            print(data["species"]["name"])
            if "evolves_to" in data:
                for evolve in data["evolves_to"]:
                    get_evolves(evolve)

        get_evolves(data["chain"])
    else:
            print(f"Error {response.status_code} obteniendo las evoluciones.")
else:
        print(f"Error {response.status_code} obteniendo las evoluciones.")
#nota: tuve mucha ayuda para hacer esto porque estaba durisimo
