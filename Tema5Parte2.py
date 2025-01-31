# Ejercicio Tema 5 Parte 2

# Definimos una variable x con una cadena
x = "El valor de (a+b)*c es"
# Podemos realizar múltiples asignaciones
a, b, c = 4, 3, 2
# Realizamos unas operaciones con a,b,c
d = (a + b) * c
# Definimos una variable booleana
imprimir = True
# Si imprimir, print()
if imprimir:
   print(x, d)
# Salida: El valor de (a+b)*c es 14   
   

'''se puede usar el punto y coma ; para tener dos sentencias en la misma línea'''
x = 5; y = 10


'''Haciendo uso de \ se puede romper el código en varias líneas, la especificación PEP8 recomienda líneas de no más de 79 caracteres'''
x = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8


'''Si por lo contrario estamos dentro de un bloque rodeado con paréntesis (), bastaría con saltar a la siguiente línea.'''
x = (1 + 2 + 3 + 4 +
5 + 6 + 7 + 8)


'''Se puede hacer lo mismo para llamadas a funciones:'''
def funcion(a, b, c):
   return a+b+c
d = funcion(10,
23,
3)


'''podemos importar módulos externos para realizar más operaciones matemáticas'''
import math
math.pi * 4
12.566370614359172
math.pi ** 2
9.869604401089358
math.sqrt(4) # Raíz cuadrada
2
math. sqrt(12)
3.4641016151377544
#Para ver los resultados usamos print:
import math
print(math.pi * 4)  # 12.566370614359172
print(math.pi ** 2)  # 9.869604401089358
print(math.sqrt(4))  # Raíz cuadrada, resultado: 2
print(math.sqrt(12))  # 3.4641016151377544

'''Otro módulo es el random que nos permite generar y seleccionar números aleatorios, entre muchas otras opciones'''

import random

num_aleat=random.random ()
print(num_aleat)

#0.6567888091274212

lista = [1, 2, 3, 4]
random.choice(lista)
print("Valor aleatorio seleccionado",lista)

3

random.shuffle(lista)

#lista
#[2, 3, 1, 4]
print("Lista mezclada",lista)


'''Para ejecutarlo, con Visual Studio Code. Abre la terminal py camino del archivo...El comando py y el path'''


'''Para saltarnos la precedencia podemos utilizar paréntesis para aislar expresiones. En Python, las expresiones entre paréntesis se evalúan siempre antes que el resto. De esta manera, en la expresión "A", si quisiéramos evaluar antes la suma, haríamos la expresión "B "lo siguiente: A * (B + C) * D.'''
a= 2 * 3 + 3 * 4 # Expresión "A" Multiplicación precede a la suma.
14
b= 2 * (3+2) * 4 # Expresión "B" Expresiones entre paréntesis se evaluan primero
40
print (a)
print (b)

#---------------------------------------------------------------
#Tema5Parte5

'''def nombre_de_la_función(arg1, arg2, ...a
rgN):
sentencias
return #El return es opciona'''


