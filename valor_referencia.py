"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas. Comprueba también que se ha conservado el valor original en las primeras.
 """



#datos por valor
int_1 = 10
int_2 = int_1
int_2 = 20
print(int_1)
print(int_2)

#datos por referencia

lista_1 = [10, 20]
lista_2 = lista_1
lista_2.append(30)
print(lista_1)
print(lista_2)

#para que lista 3 != lista 4
lista_3 = [20, 30]
lista_4 = lista_3[:]
lista_4.append(40)
print(lista_3)
print(lista_4)

#funciones con datos por valor

def function1(int_1: int, int_2: int):
    valor_retorno = int_1 + int_2
    return valor_retorno
    

int_3 = 30
int_4 = function1 (int_3, int_2)
print (int_4)


#funciones con datos por referencia
def lista_ref(lista_1: list):
    lista_1.append(69)

lista_69 = lista_1
lista_69.append(99)
lista_ref(lista_69)
print(lista_69)
print(lista_1)

lista_7 = [66, 67]
lista_ref(lista_7)
print(lista_7)
print(lista_69)
print(lista_1)



""""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas. Comprueba también que se ha conservado el valor original en las primeras.
"""
#extra
def value(value_a: int, value_b:int):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b

def ref(value_a: list, value_b: list):
    temp = value_a
    value_a = value_b
    value_b = temp
    return value_a, value_b


value_1 = 30
value_2 = 69
value_3 = [440, 12, 43]
value_4 = [123, 456, 789]

print (value(value_1, value_2))
print (ref(value_3, value_4))

