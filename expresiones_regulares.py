"""
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
import re
texto = "Mi usr de gitHub es Enzo-09, naci en 2004, tengo 21 years, esta es la practica numero 16 que realizo"
print(re.findall('\d', texto))

#extra
def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$", email)) 
print(validate_email("johndoe@gmail.com"))

def validate_phone(phone: str) -> bool:
    return bool(re.match(r"^\+?[\d\s]{3,}$", phone))


print(validate_phone("+34 901 65 89 04"))


def validate_url(url: str) -> bool:
    return bool(re.match(r"^http[s]?://(www.)?[\w]+\.[a-zA-Z]{2,}$", url))


print(validate_url("http://www.johndoe.com"))

#nota, no estoy muy seguro de haber entendido y estuvo durisimo