class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota 

    def __str__(self):
        return "El alumno se llama {}, y tiene {} de nota".format(self.nombre, self.nota)

def calificacion(nota):
    if nota >= 5:
        print("el alumno esta aprobrado ")
    else:
        print("el alumno esta suspendido")

a = Alumno("marcos", 10)
b = Alumno("fernando", 4)
i = Alumno("paula", 8)
