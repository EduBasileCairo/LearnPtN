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
