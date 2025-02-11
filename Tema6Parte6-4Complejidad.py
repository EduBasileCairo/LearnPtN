# Genero una lista de 100 millones de números aleatorios
# import numpy as np 
# x = list(np.random.randint(low=1,high=500000,size=9999999))

# COMPLEJIDAD CONSTANTE O(k) CONSTANT TIME
import time

def constante(x: list) -> list:
    return x

x = [1, 2, 3, 4, 5]  # Lista de prueba

start_time = time.time()  # Iniciar temporizador
print('Complejidad Constante O(k) Constant Time',constante(x))  # Llamamos a la función e imprimimos su salida
end_time = time.time()  # Finalizar temporizador

print(f"Tiempo de ejecución: {end_time - start_time:.6f} segundos")


# COMPLEJIDAD O(n) LINEAR TIME
def iterador_normal(x:list) -> list:
    contador = len(x)
    while(contador > 0):
        contador -= 1
    return x # iterador_normal(x)
# Llamamos a la función con una lista y mostramos su resultado
print('Complejidad O(n) Linear Time', iterador_normal([1, 2, 3, 4, 5]))




# COMPLEJIDAD O(n2) QUADRATIC TIME
def iterador_anidado(x:list) -> list:
    contador_externo = len(x)//1000
    contador_interno = len(x)//1000
    while(contador_externo > 0):
        contador_externo -= 1
    for i in range(contador_interno):
        pass # No hace nada dentro del bucle interno
    return x

# Lista de prueba
x = [1, 2, 3, 4, 5]

# Imprimir el resultado de la función
print('Complejidad O(n2) Quadratic Time',iterador_anidado(x))

# COMPLEJIDAD O(log(n)) LOGARITHMIC TIME:
def iterador_multiplicado(x: list) -> list:
    iterador = len(x)
    incremento = 1
    
    while (iterador > 0):
        iterador -= incremento
        incremento *= (incremento + 1)  # Se multiplica el incremento por su sucesor
    
    return x  # El return debe estar correctamente indentado

# Lista de prueba
x = [1, 2, 3, 4, 5]

# Imprimir el resultado de la función
print('Complejidad O(log(n)) Logarithmic Time',iterador_multiplicado(x))


# COMPLEJIDAD O(log(n)) LOGARITHMIC TIME:
import time # Importa el módulo time, que proporciona funciones para trabajar con tiempos.
def iterador_dividido(x: list) -> None:
    """Imprime cada elemento de la lista x usando un iterador y un bucle while."""

    iterador = 0
    longitud_x = len(x)

    while iterador < longitud_x:
        print('COMPLEJIDAD O(log(n)) LOGARITHMIC TIME',x[iterador])
        iterador += 1

# Ejemplo de uso:
mi_lista = [1, 2, 3, 4, 5]
iterador_dividido(mi_lista)
# Registra el tiempo de inicio
inicio = time.time()

iterador_dividido(mi_lista)

# Registra el tiempo de fin
fin = time.time()

# Calcula el tiempo transcurrido en segundos
tiempo_transcurrido = fin - inicio

# Convierte el tiempo a nanosegundos
tiempo_transcurrido_ns = tiempo_transcurrido * 10**9

#  Imprime el tiempo transcurrido en nanosegundos, formateado para mostrar 0 decimales
print(f"Wall time: {tiempo_transcurrido_ns:.0f} ns")

# COMPLEJIDAD O(log(log(n))) LOGARITHMIC from LOGARITHMIC TIME
import math
import time

def iterador_incremento_exponencial(x: list) -> list:
    """
    Esta función itera sobre una lista y reduce el iterador 
    exponencialmente en cada paso, utilizando el cuadrado del incremento.
    """
    iterador = len(x)
    incremento = 1
    while iterador > 0:
        iterador -= pow(incremento, 2)
        incremento += 1
    return x

# Ejemplo de uso
x = list(range(10))  # Creamos una lista de ejemplo

# Medir el tiempo de ejecución
inicio = time.time()

resultado = iterador_incremento_exponencial(x)

fin = time.time()

# Calcular y mostrar el tiempo transcurrido
tiempo_transcurrido = fin - inicio
tiempo_transcurrido_ms = tiempo_transcurrido * 1000  # Convertir a milisegundos

print(f"Resultado: {resultado}")
print(f"Wall time: {tiempo_transcurrido_ms:.6f} ms")

# CÁLCULO DE LA COMPLEJIDAD ALGORÍTMICA DEL EJEMPLO:
import numpy as np
import time

y = list(np.random.randint(low=1, high=500000, size=999))

def calculo_bit_o_ejemplo(y: list) -> str:
    iterador = -len(y)
    incremento = 1
    q_list = y  # Esta línea no se utiliza, se puede eliminar
    while iterador < 0:
        iterador /= incremento
        incremento += 1
    for p in y:
        for q in y:
            for r in y:
                r  # Esta línea no hace nada, se puede eliminar
    return "La Complejidad es n*n*n, n cubo"

# Medir el tiempo de ejecución
inicio = time.time()

resultado = calculo_bit_o_ejemplo(y)

fin = time.time()

# Calcular y mostrar el tiempo transcurrido
tiempo_transcurrido = fin - inicio
tiempo_transcurrido_ms = tiempo_transcurrido * 1000  # Convertir a milisegundos

print(resultado)
print(f"Wall time: {tiempo_transcurrido_ms:.6f} ms")