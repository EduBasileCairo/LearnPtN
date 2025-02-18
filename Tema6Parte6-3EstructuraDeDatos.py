# La eficiencia de un algoritmo depende de la cantidad de tiempo, almacenamiento y otros recursos necesarios para ejecutar el algoritmo. La eficiencia se mide con la ayuda de notaciones asintóticas. Un algoritmo puede no tener el mismo rendimiento para diferentes tipos de entradas. Con el aumento en el tamaño de entrada, el rendimiento cambiará. El estudio del cambio en el rendimiento del algoritmo con el cambio en el orden del tamaño de entrada se define como análisis asintótico.
# Hemos visto cómo guardar un dato en una variable para poder trabajar posteriormente con él. Ahora vamos a ver las estructuras que posee Python para poder trabajar con colecciones de datos. Las estructuras de datos en Python se pueden entender como un tipo de dato compuesto, debido a que en una misma variable podemos almacenar no sólo un dato, sino infinidad de ellos. Dichas estructuras, pueden tener diferentes características y funcionalidades. Hay cuatro tipos de estructuras de recopilación de datos en el lenguaje de programación Python: 1) La lista (list); es una colección ordenada y modificable. Permite miembros duplicados. 2) Tupla (tuple); es una colección ordenada e inmutable. Permite miembros duplicados. 3) Conjuntos (Set); es una colección que no está ordenada ni indexada. No hay miembros duplicados. 4) Diccionario (Dictionary); es una colección desordenada, modificable e indexada. No hay miembros duplicados. Al elegir un tipo de colección, es útil comprender las propiedades de ese tipo. Elegir el tipo correcto para un conjunto de datos en particular podría significar un aumento en la eficiencia y seguridad.

# LISTAS: Son una secuencia de valores de cualquier tipo, ordenados y de tamaño variable. Las listas en Python se representan con el tipo list y la sintaxis que se utiliza para definirlas consiste en indicar una lista de objetos separados entre comas y encerrados entre corchetes: [obj1, obj2, ..., objn]. Las listas son estructuras de datos que nos permiten almacenar gran cantidad de valores (equivalentes a los arrays en otros lenguajes de programación). Se pueden expandir dinámicamente añadiendo nuevos elementos, es decir, la cantidad de valores que contendrán podrá variar a lo largo de la ejecución del programa. Las listas pueden contener cualquier tipo de dato: números, cadenas, booleanos… y también otras listas e incluso funciones, objetos, etc. Se pueden mezclar diferentes tipos de datos. Las listas son mutables.Una de las características importantes de las listas es que se corresponden con una colección ordenada de objetos. El orden en el que se especifican los elementos cuando se define una lista es relevante y se mantiene durante toda su vida. Sintaxis de las listas: Crear una lista es tan sencillo como indicar entre corchetes y separados por comas, los valores que queremos incluir en la lista:
# nombreLista=[elem1, elem2, elem3…]
# Se pueden mezclar elementos de distinto tipo.
miLista=["Angel", 43, 667767250]
miLista2 = [22, True, "una lista", [1, 2]]
type(miLista)
print(miLista)

# También se pueden crear desde strings:
# Crear una lista con las letras de "Python"
lista_letras = list("Python")

# Imprimir la lista resultante
print(lista_letras)

# Podemos acceder a cada uno de los elementos de la lista escribiendo el nombre de la lista e indicando el índice del elemento entre corchetes.
print(miLista[0]) # Imprimiría: Angel

# Si queremos acceder a un elemento de una lista incluida dentro de otra lista tendremos que utilizar dos veces este operador, primero para indicar a qué posición de la lista exterior queremos acceder, y el segundo para seleccionar el elemento de la lista interior:
miLista3 = ['una lista', [1, 2, 3, 4, 5]]
mi_var = miLista3 [1][0] # mi_var vale 1
print(mi_var)

# Podemos utilizar este operador para modificar un elemento de la lista si lo colocamos en la parte izquierda de una asignación:
miLista4 = [22, True]
print(miLista4)
miLista4 [0] = 99 # Con esto miLista valdrá [99, True]
print(miLista4[:])

# Se puede declarar una li sta vacía, sin elementos. Como en Java, el primer elemento de la lista está en el índice o posición cero.
# Nota: Si pongo índices negativos lo que hace Python es contar desde el final hasta el principio empezando por -1, es decir, en mi caso el elemento “Angel” podría ser la posición [0] o la [-3]. Como en los strings. Si pongo:
Lista2 = miLista[-2:] # Me crea una sublista con los elementos [43, 667767250]
print(Lista2) # Elimina "Ángel" y deja [43, 667767250]

# Podemos comparar listas:
miLista6 = ['t1', 't2', 't3']
miLista3 == miLista6

# MÉTODOS DE LAS LISTAS: Method & Description
# append() Añade un elemento al final de la lista
# clear() Borra los elementos de la lista.
# copy() Devuelve una copia de la lista.
# count() Devuelve el número de veces que se
# encuentra un elemento en la lista
# extend() Añade los elementos de una lista a otra.
# index() Devuelve el índice del primer
# elemento cuyo valor es el especificado.
# insert() Añade un elemento en la posición especificada.
# pop() Borra el elemento en la posición especificada y devuelve el elemento eliminado.
# remove() Elimina el elemento con el valor especificado
# reverse() Invierte el orden de la lista.
# sort() Ordena la lista

# Los métodos más usados son: len(), append(), pop(), insert() y remove().
# Como las listas son colecciones mutables, muchos de los métodos de éstas la modifican in-place en lugar de crear una lista nueva, como por ejemplo sort() o reverse().
miLista1 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
miLista2 = ["Maria", 2, 5.56, True] # Se puede mezclar diferentes elementos
print (miLista[1]) # Para un elemento en concreto, se empieza a contar desde la posición cero.
print (miLista[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, “Angel y María”.

# Si escribimos tres números (inicio:fin:salto) en lugar de dos, el tercero se utiliza para determinar cada cuantas posiciones añadir un elemento a la lista, Ejemplo:
miLista1 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
miLista2 = ["Maria", 2, 5.56, True] # Se puede mezclar diferentes elementos
print (miLista[1]) # Para un elemento en concreto, se empieza a contar desde la posición cero.
print (miLista[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, “Angel y María”.

# Listas anidadas: Una lista puede contener cualquier tipo de objeto. Esto incluye otra lista. Una lista puede contener sublistas, que a su vez pueden contener sublistas, y así hasta una profundidad arbitraria. Estas operaciones sirven para matrices pequeñas y operaciones sencillas. Sin embargo, si queremos operar con matrices grandes o en problemas complejos, Python dispone de librerías para este tipo de usos. El principal ejemplo es Numpy, un proyecto de código abierto con gran respaldo de la comunidad científica y de numerosas organizaciones privadas. El proyecto Numpy es uno de los principales responsables del tremendo éxito de Python en el campo de Data Science.

# TUPLAS: son un objeto idéntico a una lista excepto por las siguientes propiedades: 1) Al igual que las listas, definen una colección ordenada de objetos, sin embargo, utilizan la sintaxis (obj1, obj2, ..., objn) en lugar de [obj1, obj2, ..., objn]. 2) Las tuplas son inmutables, es decir, no se pueden modificar después de su creación. 3) No permiten añadir, eliminar, mover elementos (no append, extend, remove). 4) Sí permiten extraer porciones, pero el resultado de la extracción es una tupla nueva. 5) No permiten búsquedas (no index). 6) Permiten comprobar si un elemento se encentra en la tupla. 7) Se representan dentro de Python con el tipo de dato tuple.
# Las tuplas respecto a las listas, son más rápidas, menos espacio (mayor optimización), formatean string, pueden utilizarse como claves en un diccionario (las listas no).
# Hay determinados casos de uso en los que puede ser recomendable utilizar una tupla en lugar de una lista: 1) La ejecución del programa es más rápida cuando se manipula una tupla que cuando se trata de una lista equivalente. (Esto probablemente no se note cuando la lista o tupla es pequeña). 2) Si los valores de la colección van a permanecer constantes durante la vida del programa, el uso de una tupla en lugar de una lista protege contra la modificación accidental. 3) Hay otro tipo de datos de Python que presentaremos próximamente llamado diccionario, que requiere como uno de sus componentes un valor inmutable. Una tupla puede ser utilizada para este propósito, mientras que una lista no puede serlo.
# Acceso a elementos de tupla:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Indexación Negativa: La indexación negativa significa comenzar desde el final, -1 refiere al último elemento, -2 refiere al segundo último elemento, etc.
print(thistuple[-1])

# Rango de índices: Puede especificar un rango de índices especificando dónde comenzar y dónde terminar el rango. Al especificar un rango, el valor de retorno será una nueva tupla con los elementos especificados.
thistuple = ("apple", "banana", "cherry", "orange" , "kiwi", "melon", "mango")
print('Rango elementos', thistuple[2:5])

# Rango de índices negativos: índice -1 excluido.
print('Rango elementos índice negativo', thistuple[-4:-1])

# Cambiar valores de tupla: Una vez que se crea una tupla, no puede cambiar sus valores. Las tuplas son inmutables. Pero hay una solución alternativa. Podemos convertir la tupla en una lista, cambiar la lista y volver a convertir la lista en una tupla.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" #cambia el elemento 1 "banana" por "kiwi"
x = tuple(y)
print(x)

# Recorrer una tupla: Puedes recorrer los elementos de la tupla utilizando un bucle for.
thistuple = ("apple", "banana", "cherry")
for x in thistuple: print('recorriendo la tupla con bucle for ',x)

# Comprobar si el artículo existe: su usa la palabra clave in.
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: print("Yes, 'apple' is in the fruits tuple")

# Longitud de la tupla: se usa el método len().
thistuple = ("apple", "banana", "cherry")
print('La longitud de la tupla es: ', len(thistuple))

# Agregar artículos: 
# thistuple = ("apple", "banana", "cherry")
# thistuple[3] = "orange" # This will raise an error
# print(thistuple)

# Crear tupla con un artículo:Para crear una tupla con un solo elemento, debes agregar una coma después del elemento, a menos que Python no reconozca la variable como una tupla.
thistuple = ("apple",)
print(type(thistuple)) #NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Eliminar elementos: Las tuplas no se pueden cambiar, por lo que no puedes eliminar elementos de él, pero puedes eliminarlas por completo: La palabra clave es "del".
# thistuple = ("apple", "banana", "cherry") 
# del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists

# Une dos tuplas: Para unir dos o más tuplas, puedes usar el operador + .
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# El constructor tuple (): es posible usar el constructor tuple () para hacer una tupla.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print('Tupla creada con el constructor "tuple"', thistuple)

# Métodos de las tuplas:
# Método Descripción
# count() Devuelve el número de veces que un valor especificado aparece en una tupla.
# index() Busca en la tupla un valor específico y devuelve la posición donde se encontró.
miTupla9=("Angel", 4, 5.345, True, 4)
tuplaUnitaria=("Sara",) #Tupla unitaria. Hay que poner al final ","
print(miTupla9[2]) #Igual que en las listas
miLista=list(miTupla9) #Con list convierto una tupla en una lista
miTupla2=tuple(miLista) #Con tuple convierto una lista en una tupla.
print('En mi tupla esta Ángel: ',"Angel" in miTupla9) #Está "Angel" en miTupla?, devuelve True o False
print('¿Cuántas veces está el número 4 en mi tupla? ', miTupla9.count(4)) #Cuantas veces se encuentra el elemento 4 en miTupla?
print('¿Qué longitud tiene mi tupla? ',len(miTupla9)) #Longitud de mi Tupla

# Podemos definir la tupla sin poner los paréntesis, es lo que se conoce como “empaquetado de tupla”. En principio no se recomienda:
miTupla="Angel", 4, 5.345, True, 4 
#Desempaquetado de tupla. Permite asignar todos los elementos de una tupla a diferentes variables:
miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla
# Solo con esto ya nos ha asignado los valores de miTupla a las variables que hemos definido, podemos hacer la prueba imprimiéndolas:
print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)

# DICCIONARIOS: también llamados matrices asociativas, deben su nombre a que son colecciones que relacionan una clave y un valor. Un diccionario es una colección desordenada, modificable e indexada. En Python, los diccionarios se escriben entre llaves y tienen claves y valores. Son estructuras de datos que nos permiten almacenar valores de diferente tipo (números, strings, etc) e incluso listas y otros diccionarios. La principal característica de los diccionarios es que los datos se almacenan asociados a una clave de tal forma que se crea una asociación de tipo clave-valor para cada elemento. Los elementos almacenados no están ordenados. Ejemplo: Crear e imprimir un diccionario:
dic = {
"Nombre":"Santiago",
"Apellido":"Hernandez",
"Pais":"España",
"Ciudad":"Madrid"
}
print('Diccionario 1: ',dic)
# Otra forma de definir diccionarios con la funcion dict()
dic2 = dict(
Nombre="Santiago",
Apellido="Hernandez",
Pais="España",
Ciudad="Madrid"
)
print('Diccionario 2:',dic2)

# En Python un diccionario sería similar a lo que en Java un hashtable o en PHP un array asociativo. El primer valor se trata de la clave y el segundo del valor asociado a la clave. Como clave podemos utilizar cualquier valor inmutable: podríamos usar números, cadenas, booleanos, tuplas… pero no listas o diccionarios, dado que son mutables. Esto es así porque los diccionarios se implementan como tablas hash, y a la hora de introducir un nuevo par clavevalor en el diccionario se calcula el hash de la clave para después poder encontrar la entrada correspondiente rápidamente. Si se modificara el objeto clave después de haber sido introducido en el diccionario, evidentemente, su hash también cambiaría y no podría ser encontrado.
# Métodos de los diccionarios:
# clear() Borra todos los elementos de un diccionario
# copy() Devuelve una copia de un diccionario
# fromkeys() Devuelve un diccionario con las claves y valores especificados
# get() Devuelve el valor de una clave
# items() Devuelve una lista que contiene una tupla por cada par clave-valor
# keys() Devuelve una lista que contiene las claves del diccionario
# pop() Borra el elemento con la clave especificada
# popitem() Borra el último par clave-valor insertado
# setdefault() Devuelve el valor de la clave especificada. Si no existe, inserta la clave con el valor especificado.
# update() Actualiza el diccionario con el par clave-valor que se especifique
# values() Devuelve una lista con los valores del diccionario

# BYTES y BYTEARRAY: Un byte es una ubicación de memoria con un tamaño de 8 bits. Un objeto bytes es una secuencia inmutable de bytes, conceptualmente similar a un string. El objeto bytes es importante porque cualquier tipo de dato que se escribe en disco se escribe como una secuencia de bytes, los enteros o las cadenas de texto son secuencias de bytes. Lo que convierte la cadena de bytes en una cadena de texto o un número entero, es la forma en la que se interpreta.

# SETS, CONJUNTOS: Los sets son un tipo de datos en Python que permite almacenar múltiples elementos en una misma variable. A diferencia de las listas, la colección de elementos que forman un set: 1) No se puede indexar. 2) No respeta un orden. 3) No puede contener valores duplicados Los sets se representan dentro de python con el tipo de dato set. La sintaxis que se utiliza para definir un set en Python es la siguiente:
# {val1, val2, ..., valn}
# También llamados sets. Los sets (conjuntos) son un tipo de datos básico de Python diferente a las secuencias y los diccionarios, pero aun así de gran utilidad. Los sets son conjuntos de objetos mutables no ordenados, (únicos y no ordenados), que se basan en la noción matemática de conjuntos. De hecho, implementan una serie de métodos que permiten trabajar con conjuntos de objetos de la misma manera que lo hacemos en conjuntos matemáticos. Podemos hacer intersecciones, uniones, diferencias, etc. No obstante, un conjunto no puede incluir objetos mutables como listas, diccionarios, e incluso otros conjuntos. Son útiles cuando queremos trabajar con datos masivos y queremos extraer información relevante de ellos.
# Establecer métodos:
# add() Añade un elemento al set
# clear() Borra todos los elementos del set
# copy() Devuelve una copia del set
# difference() Devuelve un set que contiene las diferencias entre dos o más sets
# difference_update() Borra los elementos del set que están incluidos en otro
# discard() Borra el elemento especificado
# intersection() Devuelve un set que es la intersección resultante de otros dos
# intersection_update() Borra los elementos del set que no están presentes en otro
# isdisjoint() Informa si dos sets tienen una intersección o no
# issubset() Informa si otro set contiene a este set o no
# issuperset() Informa si este set contiene a otro set o no
# pop() Borra un elemento del set, no podremos elegir cuál.
# remove() Borra un elemento específico
# symmetric_difference() Devuelve un set con las diferencias simétricas de dos sets
# symmetric_difference_update() Inserta las diferencias simétricas de este set y otro
# union() Devuelve un set con la unión de dos sets
# update() Actualiza el set con la unión de este set y otros
