class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.fuerza}, Velocidad: {self.velocidad})'

    def __add__(self, otro_pj):
        nuevo_nombre = self.nombre + "-" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza) / 2) ** 2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad) / 2) ** 2
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)

    def aumentar_velocidad(self, aumento):
        self.velocidad += aumento
        return f"{self.nombre} ha aumentado su velocidad en {aumento} unidades."

    def aumentar_fuerza(self, aumento):
        self.fuerza += aumento
        return f"{self.nombre} ha aumentado su fuerza en {aumento} unidades."

goku = Personaje("Goku", 1012, 175)
vegeta = Personaje("Vegeta", 55, 101)
jiren = Personaje("Jiren", 100, 100)

gogeta = goku + vegeta

print("Fuerza de Gogeta:", gogeta.fuerza)
print("Velocidad de Gogeta:", gogeta.velocidad)

# Aumentar fuerza de un personaje
print(gogeta.aumentar_fuerza(50))
