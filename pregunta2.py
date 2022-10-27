

def multiplos(lista):
    lista2 = []
    for i in lista:
        if i % 10 == 0 and i < 200:
            lista2.append(i)
            return lista2
        
def no_masde_300(lista):
    for i in lista:
        if i > 300:
            break 
        else:
            return(lista)


lista = [18, 50, 210, 80, 145, 333, 70, 30]

m = multiplos(lista)
print(m)