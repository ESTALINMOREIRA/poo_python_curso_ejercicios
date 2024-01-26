class Estudiante :
    #atributos nombre, edad, grados
    
    #constructor
    def __init__(self, nombre, edad, grado):
        self.nombre=nombre
        self.edad=edad
        self.grado=grado
    #metodo estudiar
    def estudiar(self):
        return f'\nEl estudiante {self.nombre} está estudiando\n' #retornar un estring haciendo referencia a self usando asi mi atributo nombre


nombre=input("nombre: ")
edad=int(input("edad del estudiante: "))
grado=input("grado al que pertenece estuadiante ")

estudiante1=Estudiante(nombre,edad,grado)
print(estudiante1.estudiar())

    
        