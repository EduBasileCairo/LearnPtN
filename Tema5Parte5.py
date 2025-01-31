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

def factores_primos(n):
    factores = []
    
    # Dividir por 2 hasta que ya no sea divisible
    while n % 2 == 0:
        factores.append(2)
        n //= 2  # Reducimos el número dividiendo entre 2

    # Probar con los impares desde 3 hasta la raíz cuadrada de n
    i = 3
    while i * i <= n:
        while n % i == 0:  # Si es divisible, lo agregamos y reducimos n
            factores.append(i)
            n //= i
        i += 2  # Solo probamos con impares

    # Si queda un número mayor a 2, también es un factor primo
    if n > 2:
        factores.append(n)

    return factores

# Prueba con un número
num = 105
print(f"Factores primos de {num}: {factores_primos(num)}")
