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
random.random ()
0.6567888091274212
lista = [1, 2, 3, 4]
random.choice(lista)
3
random.shuffle(lista)
lista
[2, 3, 1, 4]


'''Para ejecutarlo, con Visual Studio Code. Abre la terminal
py C:\Users\Viviana\Documents\Phyton\PracticasPersonales\Tema5Parte2.py
El comando py y el path'''
