# Definimos la clase Persona con un constructor que recibe nombre y edad
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo para almacenar el nombre
        self.edad = edad      # Atributo para almacenar la edad

    # Método para mostrar la información de la persona
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Pedimos al usuario que ingrese el nombre y la edad de la persona
nombre_ingresado = input("Ingrese el nombre de la persona: ")
edad_ingresada = int(input("Ingrese la edad de la persona: "))

# Creamos un objeto Persona con los datos ingresados
persona1 = Persona(nombre_ingresado, edad_ingresada)

# Mostramos la información inicial de la persona
print("\nAntes de modificar la edad:")
persona1.mostrar_info()

# Pedimos al usuario que ingrese una nueva edad
nueva_edad = int(input("\nIngrese la nueva edad: "))

# Modificamos el atributo edad del objeto persona1
persona1.edad = nueva_edad

# Mostramos la información después de modificar la edad
print("\nDespués de modificar la edad:")
persona1.mostrar_info()
