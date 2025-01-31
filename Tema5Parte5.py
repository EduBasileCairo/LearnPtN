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