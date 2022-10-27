


class Alumno():
    def __init__(self, nombre, nota):
        self.nombre = nombre 
        self.nota = nota 

def mostrar (self):
    print("Nombre: ", self.nombre)
    print("Nota: ", self.nota)
    print("El alumno se ha creado con exito")


def calificacion(self):
    if self.nota >= 5:
        print("el alumno esta aprobrado ")
    else:
        print("el alumno esta suspendido")

a = Alumno("marcos", 10)
b = Alumno("fernando", 4)
i = Alumno("paula", 8)

p = calificacion(a)
r = calificacion(i)
print(p,i)


