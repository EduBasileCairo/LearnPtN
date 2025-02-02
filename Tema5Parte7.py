# Excepciones en Python: Manejo de errores - Notificación de eventos - Manejo de casos especiales - Manejo de casos especiales

def indexador(objeto, indice):
    return objeto[indice] 
resultado=indexador('Python', 0) # Llamamos a la función
print(resultado) # Mostramos el resultado en consola - Deberá ser p

#Capturando excepciones
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 10) # Llamamos a la función con un índice fuera de rango
except IndexError: # Captura Indexerror
    print('Has puesto un índice muy grande.')
print('Hemos salido del try-catch') # Se ejecuta después del try/except

# el except sólo captura las excepciones indicadas en la sentencia. Si dentro del try se produce una excepción no contemplada en el except, no la capturará. Es posible capturar varios tipos de excepciones a la vez con:
def indexador(objeto, indice):
    return objeto[indice]
try:
    indexador('Python', 'h')
except (IndexError, TypeError):
# Captura varios errores
    print('Error.')
print('Hemos salido del try-catch')
try:
    indexador('Python', 'h')
except: # Captura todos los errores. No recomendado.
    print('Error.')
print('Hemos salido del try-catch')
#Mostramos dos maneras de interceptar excepciones.
#La primera es la recomendada y consiste en un listado (una tupla) de Excepciones que pueden saltar en nuestro bloque try. Cuando salte cualquiera de las Excepciones indicadas en nuestra tupla, entraremos en el bloque "except".
# La segunda opción, es válida sintácticamente, pero es menos recomendada porque captura cualquier excepción. Es peligroso porque podríamos estar silenciando excepciones no previstas por nosotros, por lo que estaríamos ocultando errores que luego serán difíciles de encontrar. Utilizarla con mucho cuidado y conociendo el riesgo asumido.


#Encadenamiento de bloques Except
# Las dos opciones anteriores interceptan las excepciones, pero las tratan indistintamente. Es decir, que independientemente fuera una u otra. Si queremos realizar un tratamiento especial a un tipo de excepciones, lo podemos hacer encadenando bloques except uno detrás de otro, de manera similar a bloques elif en los condicionales:
def indexador(objeto, indice):
    return objeto[indice]

try:
    indexador('Python', 'h')
except IndexError: # Captura IndexError
    print('Error de índice.')
except TypeError: # Captura TypeError
    print('El índice tiene que ser un número.')

print('Hemos salido del try-catch')
# En este caso, hemos llamado a indexador produciendo una excepción de tipo TypeError. Estas excepciones saltan cuando intentamos hacer una operación no admitida por el tipo que estamos utilizando. En este caso hemos intentado acceder al índice de una cadena de texto con otra cadena de texto en lugar de un número, por lo que hemos producido una excepción de tipo.


# Lanzando excepciones manualmente
# Podemos lanzar excepciones directamente en nuestro código utilizando la sentencia raise seguida del tipo de excepción que queremos lanzar. Para tener información que nos oriente cual ha podido ser la causa del error, creamos una instancia de IndexError (o de la excepción que queramos lanzar) y en su constructor añadimos el mensaje a mostrar. Es posible capturar nuestras propias excepciones lanzadas manualmente. Por ej.:
try:
    raise IndexError('Excepción lanzada manualmente')
except:
    print('He capturado mi propia excepción')

# La sentencia ‘assert’
# Además de lanzar excepciones manualmente, es posible hacerlo condicionalmente. Para ello, Python proporciona la sentencia assert que nos permite lanzar una excepción si se cumple una condición determinada. Es muy común utilizar la sentencia assert durante el proceso de depuración, para asegurarnos que se cumplen ciertas condiciones previas. Ejemplo:
a = 10
b = 0
assert(a > b), 'A tiene que ser mayor que B!' # Si se cumple no salta el error
print('Si se muestra esto es que no ha saltado el assert')
# Se cumple la condición, no salta el assert. Veamos un caso en el que sí salta la excepción producida por el assert. Ejemplo:
a = 10
b = 0
c = 5
assert(a == c), 'A y C tienen que ser iguales!'


# Creando nuestras propias excepciones
# Hemos visto como capturar y lanzar excepciones incluidas en la librería estándar de Python. Es de gran utilidad saber crear nuestras propias excepciones. Las excepciones son clases, si queremos crear nuestra propia excepción, sólo tenemos que crear una clase que herede de la clase base de todas las excepciones (Exception) o de cualquier otra excepción:

###class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
###    pass
###raise miPropiaExcepcion ()

#Acabamos de crear la clase MiPropiaExcepcion que hereda de Exception. Cuando una clase hereda de Exception, podemos incluirla dentro de una sentencia raise para lanzarla, así como dentro de un except para interceptarla:
class miPropiaExcepcion(Exception): #Las excepciones heredan de Exception
    pass
try:
    raise miPropiaExcepcion
except miPropiaExcepcion:
    print('He capturado mi propia excepción')
# Nuestra excepción es muy básica. Vamos a mejorarla un poco para que pueda representar su propio mensaje de error:
class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __str__(self):
        return str(self.valor)
raise(miError('Mensaje de error'))


#GPT4
# Definimos una excepción personalizada
class miPropiaExcepcion(Exception):  # Las excepciones heredan de Exception
    pass

# Lanzamos la excepción (instanciándola correctamente)
try:
    raise miPropiaExcepcion()  # Correcto: la excepción debe ser instanciada
except miPropiaExcepcion:
    print('He capturado mi propia excepción')

# Mejoramos la excepción con un mensaje personalizado
class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):  # Método debe estar indentado dentro de la clase
        return str(self.valor)

# Lanzamos la excepción personalizada con un mensaje
raise miError('Mensaje de error')

#GPT4 (2)
print("Inicio del script")  # Verifica que el código se ejecuta

# Definimos una excepción personalizada
class miPropiaExcepcion(Exception):  # Las excepciones heredan de Exception
    pass

# Lanzamos la excepción (instanciándola correctamente)
try:
    raise miPropiaExcepcion()  # Correcto: la excepción debe ser instanciada
except miPropiaExcepcion:
    print('He capturado mi propia excepción')

# Verificación de que el programa continúa
print("Continuando después del manejo de la excepción")

# Mejoramos la excepción con un mensaje personalizado
class miError(Exception):
    def __init__(self, valor):
        self.valor = valor
    
    def __str__(self):  # Método debe estar indentado dentro de la clase
        return str(self.valor)

# Lanzamos la excepción personalizada con un mensaje
raise miError('Mensaje de error')

# Evitar que la terminal se cierre automáticamente
input("Presiona Enter para salir...")
