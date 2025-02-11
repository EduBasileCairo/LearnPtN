def codigo_1( number ):
    a = 0
    for j in range(1, number+1):
        a += a + j
    for k in range(number, 0, -1):
        a -= 1
        a *= 2
    return a

# En este algoritmo tenemos unas instrucciones y varios bucles. Empecemos con contar las instrucciones. Tenemos una asignación de la variable a, así que tenemos 1 instrucción.
# Instrucciones = 1
# El siguiente es un bucle con una instrucción dentro. Dependiendo del valor de la variable $number, se realiza una instrucción n veces. Por ejemplo, si $number tiene el valor de 3 entonces las instrucciones que se realizan son 3 veces. Entonces tenemos:
# Instrucciones = (1)+(n)
# Instrucciones = n+1
# En el segundo bucle sucede lo mismo. Pero esta vez son 2 instrucciones dentro del ciclo de código. El número de instrucciones quedaría:
# Instrucciones = 2n+n+1
# Instrucciones = 3n+1
# Entonces la complejidad algorítmica sería 3n+1 porque es el número de instrucciones que tiene que realizar para solucionar el problema. Lo que interesa es saber cómo puede crecer en unidades de tiempo la resolución de un problema. En este ejemplo es claro que el tiempo crece linealmente con respecto al valor de entrada.

# CODIGO Y COMPLEJIDAD:
# Es posible calcular visualmente la complejidad de algunos algoritmos sencillos. Veamos algunos ejemplos:
def codigo_2():
    a = 0
    a -= 1
    a *= 2
# En el código 2 la complejidad sería:
# F(x)=3

# Veamos otro ejemplo:
def codigo_3( number ):
    a = 0;
    for j in range(1, number+1): # Bucle externo
        for k in range(1, number+1): # Bucle interno
            a += a + ( k*j ) # Opreaciones dentro de los bucles
    return a
# En el código 3 tenemos un bucle anidado. Cada vez que ejecute un ciclo el otro se ejecuta n veces también. Lo cual sería n veces n. La complejidad quedaría:
# F(x) = n2+1 donde n2 es en al cuadrado

# ESCENARIO DE PEOR CASO:
# Algunos algoritmos pueden tener distintos tiempos de ejecución, teniendo el mismo tamaño de los datos y los mismos recursos computacionales. Esto es debido a que, dependiendo de los datos, a veces se llegue a una solución en la primera iteración, o bien tener que recorrer todos los datos. El siguiente código tiene como fin encontrar el primer número par de una lista de números:
def codigo_4(array):
    for k in range(len(array)):
        if( array[k] % 2 == 0 ):
            return k
# return null
# Dependiendo de los valores que se guarden en el vector, así será el tiempo que dure el algoritmo en resolver el problema. Si el array es una secuencia de números enteros, entonces solo hará falta una iteración. Si es una lista de números impares, entonces recorrerá todas las iteraciones. En el mejor de los escenarios el número par será el primero de la lista, lo que concluiría el algoritmo. En el peor caso ni siquiera tenga un número par, porque recorrería todas las instrucciones. Para el mejor caso tendríamos una complejidad algorítmica: Para el mejor caso tendríamos una complejidad algorítmica: F(x)=1 Para el peor de los casos la complejidad algorítmica sería: F(x)=n Para expresar el peor caso usaremos una notación conocida como “O Grande” y se escribe: O(n). Que significa complejidad en el peor caso. Se escribe como “O” pero en realidad es la letra griega Omicron.

# ÓRDEN DE COMPLEJIDAD: Hasta aquí, es posible medir cualquier algoritmo. Pero incluso así es complicado comparar unos algoritmos con otros. Además, se requiere poder categorizar lo complejo que es un algoritmo con respecto a otros. Para esto recurriremos al orden de complejidad. Como vimos antes. Para medir un algoritmo necesitamos recurrir al escenario de peor caso y con un gran volumen de datos.

# Orden de complejidad más conocidas:
# CONSTANTE: Es la más sencilla y siempre presenta un tiempo de ejecución constante. Ejemplo:
def constante():
    x = 50
    ++x
    return x

# LINEAL: El tiempo crece linealmente mientras crece los datos. Ejemplo:   
def lineal(number):
    result = 0
    for x in range(0, number):
        ++result
    return result

# POLINÓMICO: Son los algoritmos más comunes. Cuando c es 2 se le llama cuadrático, cuando es 3 se le llama cúbico, y en general, polinómico. Cuando n es muy grande suelen ser muy complicados. Estos algoritmos suelen tener bucles anidados. Si tienen 2 bucles anidados sería un cuadrático. Ejemplo:
def polinomico(number):
    x = 0

    for i in range(1,number): # Bucle externo (Primer bloque) -> O(n)
        for j in range(1,number): # Bucle interno (Primer bloque) -> O(n) 
            x += i + j # Operación en cada iteración -> O(1)

    for i in range(1,number): # Bucle externo (Segundo bloque) -> O(n)
        for j in range(1,number): # Bucle medio (Segundo bloque) -> O(n)
            for k in range(1,number): # Bucle interno (Segundo bloque) -> O(n)
                x += i * j * k # Operación en cada iteración -> O(1)
        return x # ¡Cuidado! Esto provoca que el segundo bloque termine prematuramente
    
#LOGARÍTMICO: No suelen ser muchos. Estos algoritmos indican que el tiempo es menor que el tamaño de los datos de entrada. No importa indicar la base del logaritmo. Un ejemplo es una búsqueda dicotómica. Este algoritmo busca un elemento en un array ordenado dividiendo el array en 2 mitades, identifica en cuál de las mitades se encuentra, luego divide esa parte en 2 mitades iguales y busca nuevamente hasta encontrar el elemento, es un algoritmo recursivo:
def bin(a,x,low,high):
    ans = -1
    if low==high: ans = -1 # Caso base: no hay más elementos en el rango
    else:
        mid = (low+((high-low)//2)) # Encontrar el punto medio
    if x < a[mid]: ans = bin(a,x,low,mid) # Buscar en la mitad izquierda
    elif x > a[mid]: ans = bin(a,x,mid+1,high) # Buscar en la mitad derecha
    else: ans = mid # Elemento encontrado
    return ans

# ENELOGARÍTMICO: Tan bueno como el anterior, en este orden encontramos el algoritmo QuickSort. El ejemplo podemos verlo en Wikipedia en este enlace https://en.wikipedia.org/wiki/Quicksort. No se incluye el código debido a las distintas versiones, estudios y discusiones de este algoritmo. Pero compartiremos el comportamiento de este orden de complejidad.

# EXPONENCIAL: Es una de las peores complejidades algorítmicas. Sube demasiado a medida que crece los datos de entrada. Puede verse en la Figura como crece una función de este tipo. Un ejemplo de este código es la solución de Fibonacci, el cual genera bucles 2 recursividades en cada ejecución. Ejemplo:

def exponencial(n):
    if n==1 or n==2: # Casos base
        return 1
    return exponencial(n-1)+exponencial(n-2) # Llamadas recursivas

# Aquí tenemos una tabla muy completa con la complejidad de los principales algoritmos para estructuras de datos, ordenación de matrices, operaciones en grafos y operaciones de montón (heap).
# https://www.bigocheatsheet.com/


