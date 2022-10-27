class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "el alumno{} tiene {} de nota".format(self.nombre, self.nota)


def calificacion(self):
    if self.nota >= 5:
        print("el alumno ha aprobado ")
    else:
        print("el alumno ha suspendido")

m = Alumno("marcos", 6)
d = Alumno("elena", 4)
o = Alumno("guille", 10)

lista = [m, d, o]
calificacion(lista)



