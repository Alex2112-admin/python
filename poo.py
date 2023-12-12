# clases
class perro:
    def __init__(self, nombre, raza):
        print(f"Creando un Perro {nombre},{raza}")
        self.nombre = nombre
        self.raza = raza


mi_perro = perro("chucufluto", "cholo")
mi_perro = (type(mi_perro))

print(mi_perro.nombre)
print(mi_perro.raza)


class Gato:
    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando Gato {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza


mi_gato = Gato("Pepito", "Cholo")
mi_gato = (type(mi_gato))

