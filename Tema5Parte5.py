'''def nombre_de_la_función(arg1, arg2, ...a
rgN):
sentencias
return #El return es opciona'''

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

x=suma(2, 3) # Llamada a la función. Hay que pasarle dos parámetros.
print(x)# Resultado: 5 y lo guardamos en x


def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio
en_pantalla('Me gusta', 'Python')
# Resultado: Me gusta Python


#Funciones y polimorfismo

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.
y=suma (2, 3) # Función con ints
print (y)
# Resultado = 5
y=suma(2.7, 4.0) # Función con floats
print(y)
# Resultado = 6.7
y=suma('Me gusta mucho ', 'Python!!!') # Función con strings
print(y)


#Funciones anidadas
def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    f2(b)
f1('Python - funciones anidadas') # Llamamos a f1


#Recursividad
def factorial(x):
    if x>1: #Caso recursivo
        return x*factorial(x-1)
    else:
        return 1 #Caso base
        
print('Recursividad: resultado de factorial de 5 es',factorial(5)) #Muestra el resultado en consola que para 5 es 120

#Devolviendo múltiples valores simultáneamente
def maxmin(lista):
    return max(lista), min(lista) #Devuelve una tupla de 2 elementos
l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin(l) #Desempaqueta la tupla en 2 variables
print('El mínimo y el máximo de la Tupla son respectivamente: ',minimo, maximo, sep= ' ')


#Ejercicio de experimentación con factores primos

def factores_primos(n): # Recibe un número entero n como parámetro.
    factores = [] # Objetivo: Devolver una lista con los factores primos de n
    #En la línea anterior creamos una lista vacia "factores" guardaremos allí los factores primos que vayamos encontrando

    # Dividir por 2 hasta que ya no sea divisible
    while n % 2 == 0: # Significa que es divisible por 2 hasta no dejar residuo
        factores.append(2) # Agrega 2 a la lista con el append
        n //= 2  # Reducimos el número dividiendo entre 2, significa que es una división entera, por lo que elimina todos los factores 2 en n

    # Probar con los impares desde 3 hasta la raíz cuadrada de n
    i = 3
    while i * i <= n: #Ejecutamos el algoritmo hata que el cuadrado de i sea mayor que n ya que todo número compuesto tiene al menos un factor primo menor o igual a su raíz cuadrada
        while n % i == 0:  # Si es divisible, lo agregamos y reducimos n
            factores.append(i) # Agrega i a la lista de factores
            n //= i
        i += 2  # Solo probamos con impares, saltamos al siguiente número impar

    # Si queda un número mayor a 2, también es un factor primo
    if n > 2:
        factores.append(n) # Agregamos el númeroa la lista de factores

    return factores

# Prueba con un número
num = 2025 #En este renglón colocar el número que se quiere facorizar
print(f"Factores primos de {num}: {factores_primos(num)}") #Muestra la lista factores


# Parámetros y argumentos - Objetos Mutables e Inmutables
# Ejemplo de inmutables
def suma(a, b): # Modificamos a y b en el scope de suma()
    a = 3
    b = 4
    return a+b

a, b = 5, 10
print('Objetos inmutables:')
print(suma(a, b))
print(a, b) # a y b no han cambiado fuera de la función

# Ejemplo de Mutables

def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]

print('Objetos mutables:')
print('Lista original',l)
print('Mínimo de la lista luego de cambiar el elemento 0:',minimo(l)) # Modifica la lista aquí
print('Lista luego de reemplazar el elemento 0:',l)


# Formas de paso de argumentos
# 1 Por Posición
def f(a, b, c): # llama a la función con sus argumentos en orden
    print('Paso de argumentos por posicion:', a, b, c)

f(1, 2, 3)

# 2 Por Keywords
def f(a, b, c): # utiliza la sintaxis nombre=valor
    print('Paso de argumentos por keywords', a, b, c)

f(c=12, a=10, b=100)

# 3 Especificando valores por defecto en la definición de la llamada
def f(a, b=10, c=30):
    print('Especificando valores en la definición de la llamada:', a, b, c)

f(1)
f(1, 12)
f(1, 12, 19)

# 4 Especificando en la función que se le pasará una colección de argumentos 
def f(*args): # Acepta número arbitrario de argumentos
    print('Colección de argumentos', args)

f() # Si no hay argumentos, args es una tupla vacía
f(1)
f(1, 2)
f(1, 2, 3, 4, 5, 6)

# 5 Si usamos la sintaxis de doble asterisco:
def f(**Kargs): # Acepta número de argumentos por nombre
    print('Colección de argumentos por nombre',Kargs)

f() # Si no hay argumentos, Kargs es un diccionario vacío
f(a=1)
f(a=1, b=2)
f(a=1, c=3, b=2)

# 6 Desempaquetando una colección de argumentos posicionales o por keyword

# 7 Desempaquetar un diccionario utilizando la sintaxis de doble asterisco
def f(a, b, c, d):
    print('Colección de diccionario por **', a, b, c, d)

argumentos = {'b':20, 'a':1, 'c':300,'d':4000}
f(**argumentos) # Desempaquetando diccionario argumentos con **

argumentos = {'b':200, 'c':300, 'd':400}
f(10, **argumentos) # Podemos combinar argumentos posicionales con dict

# 8 Utilizando argumentos que sólo pueden ser pasados por clave (keyword-only)
def f(a, *b, c): # Hay que pasar 'c' por clave obligatoriamente
    print('Colección de argumentos pasados por keyword-only',a, b, c)

f(1, c=2)
f(1, 2, c=3)
f(1, 2, 3, 4, 5, c=10)


# 9 Los argumentos tras el ‘*’ se convierten en keywordonly: hay muchas funciones escritas en Python que aprovechan estas funcionalidades como, por ej., las funciones builtin zip y print.
la = [1, 2, 3, 4, 5]
lb = list('abcde')
lc = list('ABCDE')

zlist = list(zip(la, lb, lc)) # zip soporta cualquier número de argumentos posicionales
zlist
a, b, c = zip(*zlist) # El * en zip desempaqueta lista de tuplas
print('Colección de argumentos Keywordonly ', la, lb, lc, sep = '\n')
print('Colección de argumentos ', la, lb) # Separador por defecto es espacio

# Por el ejercicio de la página 17 ver el archivo EjercicioTema5Parte5.py

# Definición de variables
x = 15
y = "Ana"
print('valor de la variable x:', x)
print('valor de la variable y:', y)

# Guardamos en la variable suma el resultado de 1 + 2
suma = 1 + 2
# Accedemos al resultado de 1 + 2 a través de la variable suma
print('Resultado de la suma: ', suma)


# Asignar un valor a una variable en Python
# Asigna a la variable <a> el valor 1
a = 1
print('Valor de la variable a:', a)
# Asigna a la variable <a> el resultado de la expresión 3 * 4
a = 3 * 4
print('Valor de la variable a:', a)
# Asigna a la variable <a> la cadena de caracteres 'Pythonista'
a = 'Pythonista'
print('Valor de la variable a:', a)