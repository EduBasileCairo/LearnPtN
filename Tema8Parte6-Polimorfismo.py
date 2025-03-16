# POLIMORFISMO

# El polimorfismo es una propiedad de la herencia por la que objetos de distintas subclases pueden responder a una misma acción. El polimorfismo está implícito en Python, ya que todas las clases son subclases de una superclase común llamada OBJECT. Ejemplo, la siguiente función aplica una rebaja al precio de un producto:

def rebajar_producto(producto, rebaja):
    producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

# Gracias al polimorfismo no tenemos que comprobar si un objeto tiene o no el atributo pvp, simplemente intentamos acceder y si existe, se ejecuta.
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def rebajar(self, descuento):
        self.precio -= descuento

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}€"

def rebajar_producto(producto, descuento):
    producto.rebajar(descuento)

alimento = Producto("Manzanas", 1.50)
print(alimento, "\n")
rebajar_producto(alimento, 0.20)
print(alimento)

otro_producto = Producto("Leche", 0.80)
print(otro_producto, "\n")
rebajar_producto(otro_producto, 0.10)
print(otro_producto)

print(alimento, "\n")
rebajar_producto(alimento, 10)
print(alimento)

# Este ejemplo se centra en la definición de una clase y una función para evitar el error, el concepto de polimorfismo podría extenderse si tuvieras diferentes tipos de "alimentos" o "productos" (por ejemplo, Fruta, Lacteo, etc.) que heredarían de una clase base Producto y podrían tener implementaciones diferentes del método rebajar() o formas distintas de representarse con __str__(). En el código actual, la función rebajar_producto es polimórfica en el sentido de que puede aceptar cualquier objeto que tenga un método rebajar() (o al menos, el código intentará llamarlo). Sin embargo, para demostrar el polimorfismo de herencia de manera más explícita, necesitarías definir más clases con una jerarquía.

# Ejemplo 2:
class Poligono:
    def __init__(self, num_lados, color=None):
        self.num_lados = num_lados
        self.color = color

    def show(self):
        print(f'Polígono de {self.num_lados} lados')
        if self.color:
            print(f'Color: {self.color}')
class Cuadrado(Poligono):
    def __init__(self, lado, color=None):
        Poligono.__init__(self,4,color)
        self.lado = lado

    def show(self):
        super().show()
        print('lado:', self.lado)

class Triangulo(Poligono):
    def __init__(self, lado1, lado2, lado3, color=None):
        Poligono.__init__(self, 3, color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def show(self):
        super().show()
        print(f'lado1: {self.lado1}')
        print(f'lado2: {self.lado2}')
        print(f'lado3: {self.lado3}')

t1 = Triangulo(3, 4, 5, 'rojo') # Declaramos un triángulo
t2 = Triangulo(5, 5, 5) # Declaramos otro triángulo sin color
c1 = Cuadrado(2, 'verde') #Declaramos un cuadrado

poligonos = t1, t2, c1 #Tupla con dos Trinagulo y un Cuadrado

for poligono in poligonos:
    poligono.show() # Corregido: el método para mostrar la información es 'show'
    print()

#En este ejemplo estamos, primero definiendo la clase Cuadrado, que hereda de Poligono. Creamos una tupla con dos Triangulo y un Cuadrado y recorriéndola con un bucle for. Como vemos, llamamos al método show de cada elemento de la tupla. Como es lógico, cada llamada produce el resultado específico para el tipo de polígono al que pertenece. Notad que esto en Python es trivial ya que siempre tratamos directamente con referencias a objetos, así que la llamada a show es siempre la correspondiente a la del objeto referenciado.

# El polimorfismo se observa claramente en el bucle for. La tupla poligonos contiene objetos de diferentes clases (Triangulo y Cuadrado), que comparten una clase padre (Poligono). Cuando se llama al método show() en cada objeto de la tupla, Python automáticamente invoca la implementación del método show() que es específica para la clase de ese objeto en particular. Cuando poligono es un objeto Triangulo, se ejecuta el método show() de la clase Triangulo. Cuando poligono es un objeto Cuadrado, se ejecuta el método show() de la clase Cuadrado. Esto demuestra el polimorfismo: un único nombre de método (show()) puede tener diferentes comportamientos dependiendo del tipo de objeto al que se aplica. Python logra esto de forma natural debido a su tipado dinámico y al manejo de referencias a objetos.

# Ejemplo 3:

class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Nombre: {self.nombre}, Sueldo: {self.sueldo}]'

    def mostrar_detalles(self):
        return self.__str__()

class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento:{self.departamento}] {super().__str__()}'
    
    # def mostrar_detalles(self):
    # return self.__str__()

def imprimir_detalles(objeto): # print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

empleado = Empleado('Juan', 5000)
imprimir_detalles(empleado)

gerente = Gerente('Karla', 6000, 'Sistemas')
imprimir_detalles(gerente)