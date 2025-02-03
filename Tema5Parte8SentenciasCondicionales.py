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
texto = input("Introduce un documento de identidad")
if texto in d: #Comprobamos si esta en el diccionario
    print("La edad de " + texto + " es " + str(d[texto]))
else:
    edad = input("Documento no existe. Introduce edad: ")
    if edad.isnumeric():
        num = int(edad)
        d[texto] = num
        print("Añadido al diccionario")

print(d) # Mostramos por pantalla el diccionario