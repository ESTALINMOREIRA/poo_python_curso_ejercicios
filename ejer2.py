class Persona:
    #constructor
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    #metodo imprimir datos
    def imprimirDatos(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'


#aplicamos herencia -> Estudiante hereda de Persona los atributos
class Estudiante(Persona):
    #constructor
    def __init__(self, nombre, edad,grado):
        #llamamos al constructor de la clase padre, y heredamos atributo nombre y edad
        super().__init__(nombre,edad)
        self.grado=grado

        #metodos
    def imprimirGrado(self):
        return f'{self.imprimirDatos()}\nGrado cursando: {self.grado }'
    
print('\n___________CREANDO UNA PERSONA:__________\n')
nombre=input('Dar nombre: ')
edad=int(input('Dar edad: '))    
persona1=Persona(nombre,edad)
grado=input('Dar un grado: ')
persona1=Persona(nombre,edad)
print(persona1.imprimirDatos())
print('\n___________CREANDO UN ESTUDIANTE:__________\n')
estudiante1=Estudiante(nombre,edad,grado)
print(estudiante1.imprimirGrado())
