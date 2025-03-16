# ENCAPSULACION

# Consiste en poder ocultar los atributos o métodos de una clase para que no se puedan cambiar salvo mediante otros métodos que dispongamos nosotros. Es decir, la encapsulación consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior.

class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera."

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera.")
    def atributo_publico(self):
        return self.__atributo_privado
    def metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
print(e.atributo_publico())
e.metodo_publico()

# Pero esta simulación de getter y setters es simplemente eso, una simulación. Veamos otro ejemplo:

class Coche:
    # Método constructor
    def __init__(self):
        self.__largo = 250
        self.__ancho = 120
        self.__ruedas = 4
        self.__peso = 900
        self.__color = "rojo"
        self.__is_enMarcha = False

# Declaración de métodos
    def arrancar(self): # self hace referencia a la instancia de clase.
        self.is_enMarcha = True # Es como si pusiésemos miCoche.is_enMarcha = True

def estado(self):
    if (self.is_enMarcha == True):
        return "El coche está arrancado"
    else:
        return "El coche está parado"

# Declaración de una instancia de clase, objeto de clase o ejemplar de clase.

miCoche = Coche()

miCoche.__ruedas = 9
print("Mi coche tiene", miCoche.__ruedas,
"ruedas.")

# En este ejemplo hemos creado una clase Coche con una serie de atributos privados: largo, ancho, ruedas, peso, color, is_enMarcha. En otro lenguaje de programación con encapsulación real no podríamos cambiar los valores de dichos atributos. En Python sí podríamos, pero como los hemos declarado como privados, vamos a entender que el programador no quiere que el valor de dichos métodos se cambie manualmente y para ello nos ha ofrecido un método, arrancar(), que cambia el valor del atributo is_enMarcha. Se supone que, si quisiésemos cambiar el valor de ese atributo, lo ideal es usar el método implementado para tal efecto y no hacerlo de forma manual.