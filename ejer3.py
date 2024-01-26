class Animal:
    def __init__(self, nombre, edad, especie, colorDominante):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.colorDominante = colorDominante

class Mamifero(Animal):
    def __init__(self, nombre, edad, especie, colorDominante):
        super().__init__(nombre, edad, especie, colorDominante)

    def decir_info(self):
        return f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años."

    def amamantar(self):
        return '\nEstoy amamantando a mi cría\n'

class Ave(Animal):
    def __init__(self, nombre, edad, especie, colorDominante):
        super().__init__(nombre, edad, especie, colorDominante)

    def decir_info(self):
        return f"Soy un ave llamada {self.nombre}, tengo {self.edad} años."

    def volar(self):
        return '\nVolando alto con mis alas\n'

class Murcielago(Mamifero, Ave):
    def __init__(self, nombre, edad, especie, colorDominante):
        super().__init__(nombre, edad, especie, colorDominante)

    def decir_info(self):
        return f"Soy un murciélago llamado {self.nombre}, tengo {self.edad} años."

# Crear una instancia de la clase Murcielago con entrada de usuario
nombre_murcielago = input("Ingrese el nombre del murciélago: ")
edad_murcielago = int(input("Ingrese la edad del murciélago: "))
especie_murcielago = input("Ingrese la especie del murciélago: ")
color_murcielago = input("Ingrese el color dominante del murciélago: ")

murcielago = Murcielago(nombre_murcielago, edad_murcielago, especie_murcielago, color_murcielago)

# Imprimir métodos específicos de Murcielago
print("Métodos específicos de Murcielago:")
print(murcielago.decir_info())
print(murcielago.amamantar())
print(murcielago.volar())
