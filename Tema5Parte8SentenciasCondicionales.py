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
