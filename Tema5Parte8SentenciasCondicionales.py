# Control de Flujo en Python

# La sentencia if
# Permite ejecutar trozos de código condicionalmente, ejemplo
a = 10
b = 3
if a > b:
    print ('SI se cumple la condición') # Bloque identado 4 espacios
print ('Ya estamos fuera del if')
# SI se cumple la condición
# Ya estamos fuera del if


# Sintaxis y anidamiento.
# Diferencias con C++, en Python: 1) añade los dos puntos (:) al final de la evaluación condicional para indicar que va a empezar un bloque nuevo 2) Paréntesis en la evaluación. En Python son opcionales 3) Llaves que encierran el bloque. Python no utiliza llaves para separar bloques de código. En su lugar, la anidación se indica mediante el uso de bloques indentados, normalmente por cuatro espacios 4) Punto y coma. En Python es opcional y se usa normalmente para delimitar varias sentencias en una misma línea (una práctica nada recomendada).

# Múltiples ramas condicionales: palabras clave else y elif (else if)
a = 10
b = 3
if a > b:
    print ('Se ha cumplido la condición')
else:
    print ('No se ha cumplido la condición')
    print ('Ya estamos fuera del if')
# No se ha cumplido la condición
# Ya estamos fuera del if

a = 10
b = 10
if a > b:
    print ('A es menor que B')
elif a == b:
    print ('A es igual a B')
else:
    print ('A es mayor que B')
    print ('Ya hemos salido del condicional')
# A es igual a B
# Ya hemos salido del condicional
# La palabra clave elif nos permite hacer evaluaciones alternativas a la del if.


# Expresiones condicionales: Si hemos programado en C/C++ o javascript es muy probable que conozcamos el operador ternario:
# (a > b) ? 20: 30.
# devuelve 20 si a es mayor que b o 30 si no lo es. En Python tenemos un operador equivalente
a = 10
b = 3
20 if a > b else 30
20
#A pesar de que la expresión se lea de izquierda a derecha, realmente se evalúa en el siguiente orden. Primero se evalúa condición. Si ésta es verdadera, entonces se devuelve true_value. Si no lo es, se devuelve false_value. Ejemplo 1:Un usuario introduce texto desde teclado y queremos averiguar si es un número entero. Si es entero lo añadiremos a una variable tipo lista de números enteros.
# Cómo introducir texto desde teclado Se realiza con la sentencia:
a = input ("Introduce un número: ")
# ¿Cómo saber si un texto se corresponde a un número?. Para ello utilizamos la siguiente instrucción:
l = list() #Creamos una lista vacia
texto = input ("Introduce un texto por el teclado: ")
if texto.isnumeric():
    num = int(texto)
    l.append(num)
    print("Número " + str(num) + " añadido a la lista")
else:
    print("No has añadido un número entero")

#Otro Ejemplo
d = { "50862634" : 37 , "43394932" : 32} # Creamos diccionario
texto = input("Introduce un documento de identidad: ")
if texto in d: #Comprobamos si esta en el diccionario
    print("La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no existe. Introduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("Añadido al diccionario")

print(d) # Mostramos por pantalla el diccionario


#Ejemplo 2: Tenemos un diccionario en el que asociamos los números de los documentos de identidad de ciertas personas con su edad. Realizar un programa en el que el usuario introduzca el número de un documento. Si el número ya está en el diccionario debe mostrar la edad, en caso contrario debe solicitarnos que introduzcamos la edad, que posteriormente añadiremos al diccionario.
d = { "50862634" : 37 , "43394932" : 32} #Creamos el diccionario

texto = input("Introduce un número de documento de identidad: ")
if texto in d: #Comprobamos si está en el diccionario
    print( "La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("El documento no existe. Introduce la edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] =  num
        print("Añadido al diccionario")

print(d) #Mostramos en pantalla el diccionario


#Ejemplo 3:¿Si quisiéramos guardar este diccionario en un archivo y posteriormente abrirlo siempre que queramos consultarlo? Para ello usamos el paquete Path y Pickle (los veremos más detalladamente en otro momento). Pickle nos ofrece procedimientos para poder leer y escribir diccionarios en archivos. El paquete Path lo utilizamos para comprobar si el archivo existe. Veamos un ejemplo sencillo para leer un archivo y guardarlo en un diccionario:
#Read Python dict from a file. Atencion en el apunte está diferente.
import pickle
# Escribir el diccionario en el archivo (esto crea 'myfile.pkl')
mydict = {'a': 7, 'b' : 8, 'c' : 9}
with open('myfile.pkl' , 'wb') as output:
    pickle.dump(mydict, output)
# Leer el diccionario desde el archivo
with open('myfile.pkl', 'rb') as pkl_file:
    mydict2 = pickle.load(pkl_file)
print(mydict2) # Debería mostrar {'a': 7, 'b': 8, 'c': 9}


# Ejemplo 4: (En el apunte 6.3 hoja 11)
import pickle
from pathlib import Path

#Create an empty dictionary
d = dict()

#Ask for file name to load dictionary from
file_name = input('introduce el nombre del archivo con los datos: ')

#Comprobamos que existe
path = Path(file_name)
if path.is_file():
    # Open file in reading mode
    input_file = open(file_name, 'rb')
    d = pickle.load(input_file)
    #Close de file
    input_file.close()
else:
    print('El file no existe, creamos diccionario vacio')

#Check for values or add new ones
document_number = input('Introduce un documento de identidad ')

if document_number in d: #Check whether it is on dict or not
    print('La edad de ' + document_number + ' es '+ str(d[document_number]))
else:
    age = input('Documento no existente. Introduce la edad: ')
    if age.isnumeric():

        num = int(age)
        d[document_number] = num
        print('Añadido al diccionario')

# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()


# Bucle while
# Al igual que en otros lenguajes de programación, el bucle while repite un trozo de código iterativamente mientras se cumpla una determinada condición

### a = 0
### while a<3:
###     print (a, end=' ') # Acabamos con espacios en lugar de salto de línea
### a += 1 # Equivalente a: a = a + 1
### print (a) # Estamos fuera del while
### print('Hemos salido fuera del while')
### # 0 1 2 3 Hemos salido fuera del while

# Al comenzar cada iteración la expresión de inicio del while es evaluada. Si la expresión se cumple (devuelve True), se vuelve a entrar en el while. Si no se cumple (devuelve False), el while deja de ejecutarse y pasamos a la siguiente sentencia tras el while.

# BUCLES y las sentencias CONTINUE, BREAK, PASS y los bloques ELSE
# Sentencias que permiten alterar el flujo natural de los mismos:
# break: Interrumpe el flujo y sale fuera de bucle.
# continue: Salta al comienzo de la siguiente iteración del bucle.
# pass: No hace nada. Es una sentencia vacía.
# else: Al finalizar un bucle: Se ejecuta sólo si el bucle ha finalizado con normalidad. Es decir, se ejecuta si el bucle finaliza sin haber ejecutado un break.

# Sentencia break:
a = 5
while a: # Utilizamos la propia variable como condición
    print (a, end=' ')
    if a == 2: 
        break
    a -= 1
print ('\nFuera del Bucle por break.')
print('Valor de "a": {}'.format(a))
# 5 4 3 Fuera del Bucle.

#Sentencia continue: permite interrumpir la iteración actual
a = 7
while bool(a):
    a -= 1
    if a % 2 == 0:
        continue # Saltamos a la siguiente iteracción si es a es par
    print (a, end=' ')
print ('\nFuera del Bucle por continue.')
# 5 3 1 Fuera del Bucle

# La sentencia pass: no hace absolutamente nada. Es un marcador de posición para dejar bucles vacíos
#
### a = 5
### while a:
###     pass # Presiona Ctrl-C para abortar la ejecución

# Bloques else al finalizar bucles: tenemos dos maneras de finalizar bucles. La primera es una finalización limpia, sin interrupciones, y la segunda es mediante el uso de la sentencia break. Para saber si bucle ha finalizado de cierta manera, en muchos lenguajes de programación se utilizan flags (banderas) en el código que luego hay que evaluar. En Python, esto no es necesario ya que podemos utilizar bloques else al final de un bucle.
a = 13
b = a // 2 # División entera. P. ej. 13 // 2 == 6
while b > 1:
    if a % b == 0: # % es el operador resto. P. ej. 10 % 5 == 0
        print('{b} es factor de {a}'.format(b,a))
    break
    b -= 1
else:
    print('{} es primo'.format(a))
print ('\nFuera del Bucle por sentencia else.')
# 13 es primo Fuera del Bucle.

# El bucle FOR: La sintaxis del bucle for es muy sencilla y parecida a la del bucle while, con la excepción que en la cabecera del for, en lugar de evaluar una expresión en cada iteración, vamos asignando elementos de un iterador a una variable.
# Ejemplo 1: 
for s in ['Me', 'gusta', 'Python!']:
    print(s, end=' ')
# Me gusta Python!

#Ejemplo 2:
a = 0
for x in [1, 2, 3, 4]:
    a += x
print(a)
# Salida: 10

#Ejemplo 3:
for c in 'Me gusta Python!':
    print(c, end=' ')
# M e g u s t a P y t h o n ! Recorre el string y agrega una espacio entre cada letra

#Ejemplo 4:
for k in d:
    print(k, end=' ')
# Apellidos edad nombre.
# Al pasarle un diccionario a un for, lo recorremos por sus claves. Hay varias maneras de extraer los valores de un diccionario. Más adelante, veremos cómo recorrer simultáneamente las claves y valores, pero de momento veamos una manera muy sencilla de hacerlo:
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
d = dict(zip(keys, values)) # Creamos el diccionario
for k in d:
    info = '{}: {}'.format(k, d[k]) # Texto formateado con claves y valores
    print(info) # Imprimimos dentro del bucle
# Apellidos: van Rossum
# edad: 60
# nombre: Guido

# Asignación en TUPLAS: Python permite la asignación en tuplas. Es decir, que podemos asignar los elementos de una tupla a varias variables a la vez.
a, b = (3, 4) # Asignamos los elementos de la tupla a cada variable
print ('Ejemplo 1 - Tuplas')
print(+ a, b)
# 3 4

# De momento nos basta con conocer que esto es muy conveniente en bucles for. Por ejemplo:
t = [(1, 2), (3, 4), (5, 6)]
for x, y in t:
    print ('Ejemplo 2 - Tuplas')
    print (x + y, end= ' ')
# 3 7 11
# En este ejemplo estamos recorriendo una lista de tuplas y las vamos asignando a dos variables simultáneamente (x, e y) que luego utilizamos dentro del for para ir sumándolas. Este proceso se llama desempaquetado en tuplas. Es muy útil en muchas situaciones como, por ejemplo, cuando queremos recorrer dos listas en paralelo:
la = [10, 20, 30, 40]
lb = [5, 25, 50, 10]
for a, b in zip(la, lb):
    m = max(a, b) # max(a, b) devuelve el máximo entre a y b
    print(m , end=' ')
print('Son los máximos entre a y b, comparando el elemento 0 del la con el elemento 0 de lb y así con los siguientes pares de elemetos')
# 10 25 50 40
# En este ejemplo recorremos dos listas usando la función zip (cremallera) que, en cada iteración, nos devuelve una tupla cogiendo un elemento de cada una de las listas. Luego, dentro del for, comparamos cuál de los dos elementos es mayor con la función max y lo mostramos por pantalla.

# Otro uso muy común del desempaquetado en tuplas es navegar por los objetos de un diccionario. Anteriormente vimos un ejemplo donde recorríamos un diccionario a través de sus claves. Ahora vamos a ver cómo recorrer todos sus elementos a la vez:
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', 60]
d = dict(zip(keys, values))
for k, v in d.items(): # d.items devuelve tupla con clave, valor
    print('{}: {}'.format(k, v))
# apellidos: van Rossum
# edad: 60
# nombre: Guido
# Vemos que el método dict.items nos devuelve una tupla (clave, valor) correspondiente a una entrada del diccionario en cada iteración del for.

# Vistas en diccionarios:
# A partir de Python 3.5, el método dict.items devuelve una vista de los elementos del diccionario, es decir, no devuelve los objetos en sí hasta que no los recorramos o los convirtamos explícitamente en listas. Otros métodos tienen el mismo comportamiento son dict.keys y dict.values, que devuelven vistas de las claves y los valores respectivamente.
for k in d.keys():
    print(k, end= ' ') # apellidos edad nombre
for v in d.values():
    print(v, end= ' ') # Van Rossum 60 Guido

# Si en lugar de recorrerlos, intentamos extraer todos las claves o elementos vemos que no devuelven una lista, sino que son vistas del diccionario:
d = {'nombre': 'Guido', 'apellidos': 'van Rossum', 'edad': 60}

# Vista de las claves
claves = d.keys()
print(claves)  # Output: dict_keys(['nombre', 'apellidos', 'edad'])

# Vista de los valores
valores = d.values()
print(valores)  # Output: dict_values(['Guido', 'van Rossum', 60])

# Vista de los pares clave-valor
items = d.items()
print(items)  # Output: dict_items([('nombre', 'Guido'), ('apellidos', 'van Rossum'), ('edad', 60)])
# Tened en cuenta que no podemos acceder directamente a estas listas, sino que tenemos que, o bien recorrerlas como hemos visto antes, o bien envolverlas en listas para poder indexarlas, trocearlas, etc.

# Bucles for y contadores: (pag. 18)
# Diferencias entre el for de otros lenguajes como C/C++ o Java con los de Python. Los bucles for de Python son más parecidos a los for-each de otros lenguajes de programación. Es decir, están destinados a recorrer los elementos de secuencias o iterables. Primero de todo, veamos cómo es un for al estilo C y al estilo Pythónico. La vía Pythónica es, en casi todos los casos, más legible y más rápida de ejecutar.
letras = list('abcdesfghijklmnopqrstuvwxyz')
for i in range(len(letras)): # Versión C/C++. No lo uséis!
    print(letras[i], end='')
# a b c d e f g h i j k l m n o p q r s t u v w x y z
for c in letras:    #Versión Pythonica. Más legible y rápido
    print(c, end=' ')
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# Podemos ver se puede hacer un for al estilo C/C++. La función range nos devuelve un listado de números consecutivos de la longitud que le pasemos. En este caso, le hemos pasado la longitud de la lista de letras.
# Ejemplos de uso de range
# Hay que envolverlo en lista o recorrerlo en for
list(range(5)) # Devuelve 5 elementos empezando en 0
[0, 1, 2, 3, 4]
list(range(-5, 5)) # Devuelve elementos en el rango -5, 5
[-4, -3, -2, -1, 0, 1, 2, 3, 4]
list(range(-5, 5, 2)) # Elementos -5 a 5 en saltos de 2
[-5, -3, -1, 1, 3]
print("Primer rango:", list(range(5)))
print("Segundo rango:", list(range(-5, 5)))
print("Tercer rango:", list(range(-5, 5, 2)))
# En general, es siempre recomendable utilizar el bucle for al estilo de Python. Cuando empecemos a utilizar bucles nos veréis tentados a utilizar los for de la manera típica de otros lenguajes. Salvo algunas excepciones, siempre es mejor hacerlo de la manera Pythónica. A continuación, exponemos algunos de los casos típicos donde los recién llegados a Python tienen tendencia a programar bucles for no Pythónicos. También damos la alternativa que se debe utilizar.

# El primero de estos ejemplos ya lo hemos visto anteriormente. Se trata de recorrer varias listas simultáneamente.
import random
l1 = letras [:8] #Creamos 3 listas a partir de trozos
l2 = letras [8:16]
l3 = letras [:16]

random.shuffle(l1) # Barajamos cada trozo
random.shuffle(l2)
random.shuffle(l3)

for i in range(len(l1)): # Versión no Pythónica. NO RECOMENDADA
    print(l1[i] + l2[i] + l3[i], end='')
    print(' No Pythónica')
# cpv emq dlt hnr fis gow akz bjx

for a, b, c in zip(l1, l2, l3): # Versión Pythonica
    print(a + b + c, end=' ')
    print('Pythónica')
# cpv emq dlt hnr fis gow akz bjx
# En este ejemplo estamos troceando la lista letras en tres partes, luego barajamos cada una de las partes y recorremos las tres listas simultáneamente para ir mostrando en pantalla una letra de cada lista en cada iteración. La versión Pythónica utiliza la función zip, que ya habíamos visto antes. La única diferencia es que, en este caso, en lugar de unir dos listas estamos haciéndolo con tres. La gran ventaja de zip (además de ser más legible) es que no tenemos que preocuparnos de que todas las listas sean de igual longitud. Cuando una de las listas se termina, zip detiene la ejecución. En la alternativa no Pythónica, tendríamos que consultar las longitudes de cada lista y recorrer el bucle siguiendo los índices de la lista más corta.
    
# Otro ejemplo típico en el que los programadores noveles de Python tienden a hacer uso de for no Pythónicos es cuando estamos haciendo búsquedas de índices de los elementos de una lista. Por ejemplo:
letras = list ('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'

random.shuffle(letras)
print(''.join(letras))
#rqkmjgvzblsaoicfntxewduphy

for i in range(len(letras)): # Manera no Pythónica
    if letras [i] in vocales:
        print('{} en la posición {}'.format(letras[i], i))
        print('Versión no Pythónica')
# a en la posición 11
# o en la posición 12
# i en la posición 13
# e en la posición 19
# u en la posición 22

for i, letra in enumerate(letras): # Manera Pythónica
    if letra in vocales:
        print('{} en la posición {}'.format(letra, i))
        print('Versión Pythónica')

# a en la posición 11
# o en la posición 12
# i en la posición 13
# e en la posición 19
# u en la posición 22

# En este ejemplo buscamos las posiciones de las vocales en un abecedario desordenado. Para ello usamos la función enumerate, que nos pide una secuencia y nos devuelve la misma secuencia asociada a sus índices:
# Ejemplos de enumerate. Hay que envolverlo en list() o recorrerlo en un for
abcde = sorted(letras)[:5]

list(enumerate(abcde)) # Devuelve secuencias con sus índices
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
print("Enumeración desde 0:", list(enumerate(abcde))) 

list(enumerate(abcde, 10)) # Podemos decirle en que índice empieza
[(10, 'a'), (11, 'b'), (12, 'c'), (13, 'd'), (14, 'e')]
print("Enumeración desde 10:", list(enumerate(abcde, 10)))


# Iteradores (pag.23)

