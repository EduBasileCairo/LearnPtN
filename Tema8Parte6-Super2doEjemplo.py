# SUPER 2DO EJEMPLO

# S I N   U S A R   S U P E R (sobre escribiendo los atributos del padre)

# Jerarquía de clases sin usar super(), sobrescribiendo los atributos del padre:

class Padre(): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
        #Definimos los Atributos en el constructor de la clase
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #Definimos los atributos en el constructor
        self.ojos = ojos #Sobreescribimos cada atributo
        self.cejas = cejas
        self.cara = cara #Especificamos el nuevo atributo para Hijo

Tomas = Hijo('Marrones', 'Negras', 'Larga') #Instanciamos
print ('No usando Super ', Tomas.ojos, Tomas.cejas, Tomas.cara) #Imprimimos los atributos del objeto

# U S A N D O   S U P E R

# Es casi el mismo código, pero no necesitamos especificar la clase padre, por lo que podremos cambiarle el nombre en cualquier momento y nuestro código seguirá funcional.

class Padre(object): #Creamos la clase Padre
    def __init__(self, ojos, cejas):
        #Definimos los Atributos
        self.ojos = ojos
        self.cejas = cejas

class Hijo(Padre): #Creamos clase hija que hereda de Padre
    def __init__(self, ojos, cejas, cara): #creamos el constructor de la clase especificando atributos
        super().__init__(ojos, cejas)
        # Solicitamos a super llamar de la clase padre esos atributos
        self.cara = cara #Especificamos el nuevo atributo para Hijo
Tomas = Hijo('Marrones', 'Negras', 'Larga')
print ('Usando Super    ', Tomas.ojos, Tomas.cejas, Tomas.cara)

# El uso de super() como forma de programar más correcta. Nota: En el caso de la Herencia Múltiple super() no nos sirve. Debemos llamar a los constructores de ambas clases especificándolas por su nombre y si cambiamos el nombre u orden de la clase deberemos especificarlo