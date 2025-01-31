# Conceptos básicos y sintaxis de Python
# Entrada y salida de datos en Python

# Cómo recibir información del usuario

# Ejemplo 1: Pedir al usuario que introduzca su nombre.
# Entrada input del usuario
nombre = input('Introduce tu nombre: ')
# Salida
print("Hola, " + nombre)
print(type(nombre))

# Nota: Python toma todo aquello que el usuario introduzca por medio de un input() como un string. Para convertirlo a cualquier otro tipo de datos, tenemos que convertir la entrada explícitamente. Por ejemplo, para convertir la entrada a int o float tenemos que usar el método int() y float() respectivamente.

# Ejemplo 2: Solicitar un número y sumarle una unidad.
# Entrada por parte del usuario como número entero
num = int(input('Introduce un número: '))
add = num+1
# Salida
print('El número introducido + 1 es =', add)


# Pedir varios valores de una sola vez
# Podemos tomar múltiples entradas a la vez, usando el método map()
a, b, c = map(int, input("Introduzca los números (separados por un espacio): ").split())
print("Los números son: ", end = " ")
print(a, b, c)


# Entrada de datos en listas, conjuntos, tuplas, etc.
# Solicitando elementos de List/Set uno por uno
# Usaremos el método append() para las Listas, y el método add() para los conjuntos.
Lista = list()
Conjunto = set()
l = int(input("Introduzca el tamaño de la lista: "))
s = int(input("Introduzca el tamaño del conjunto: "))
print("Introduzca los elementos de la lista (presiona enter luego de ingresar cada número):")
for i in range(0, 3):
    Lista.append(int(input()))
print("Introduzca los elementos del Conjunto (presiona enter luego de ingresar cada número): ")
for i in range(0, 5):
    Conjunto.add(int(input()))
print(list)
print(set)

#List = list(map(int, input("Introduzca los elementos de la lista:").split()))
#Set = set(map(int, input("Introduzca los elementos del Set: ").split()))
#print(List)

# Entrada de datos en una tupla
# las tuplas son inmutables. Para agregar un elemento a una tupla, debemos convertir la tupla en lista, luego agregamos el elemento a la lista y  nuevamente convertimos la lista en una tupla.
T = (2, 3, 4, 5, 6)
print("Tupla inicial")
print(T)
L = list(T) # Se convierte la tupla en lista
L.append(int(input("Introduzca el nuevo elemento: "))) # Agregas un elemento a L
T = tuple(L) # Se convierte la lista en tupla
print("Tupla final")
print(T)


# Salida de datos en Python
#Demostración de la función print()
print("GFG")
# Demostración de la función print() con espacios
print('G', 'F', 'G')
# Print con parámetro personalizado de separación y finalización
print("GFG", end = "@")
print('G', 'F', 'G', sep = "#")

#Salida de datos con formato
# Podemos usar literales de cadena con formato, comenzando una cadena con f o F antes de abrir comillas o comillas triples. En esta cadena, podemos escribir expresiones de Python entre { } que pueden referirse a una variable o cualquier valor literal.
# Declaramos una variable
name = "Antonio"
# Salida
print(f'¡Hola {name}!. ¿Qué tal?')

#Usando format: para que nuestra salida se vea presentable. Las llaves { } funcionan como marcadores de posición. Podemos especificar el orden en que aparecen las variables en la salida.
#Declaramos de variables
a = 20
b = 10
# Suma
sum = a+b
# Resta
sub = a-b
#Producto
producto = a*b
#Cociente
cociente = a/b
#Potencia
potencia = a**b
# Salida
print('El valor de a es {} y b es {}'.format(a,b))
print('{2} es la suma de {0} y {1}'.format(a, b, sum))
print('{sub_value} es la resta de {value_a} y {value_b}'.format(value_a=a,value_b=b,sub_value=sub))
print('{2} es el producto de {0} y {1}'.format(a, b, producto))
print('{2} es el cociente de {0} y {1}'.format(a, b, cociente))
print('{2} es la potencia de {0} elevado a la {1}'.format(a, b, potencia))


# Uso del operador %
# Los valores de % se reemplazan con cero o más valores de elementos. El formateo usando % es similar al de 'printf' en el lenguaje de programación C.
# %d – entero
# %f – flotante
# %s - cadena
# %x - hexadecimal
# %o – octal

num = int(input("Introduzca un número:"))
add = num+5
# Salida
print("La suma es %d" %add)
