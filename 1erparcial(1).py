personajes = ['Darth Vader','Obi-Wan','Yoda','Anakin','Chewbacca','Han solo', 'C3PO']
pos = 0
def barrido_r(personajes, pos):
    if(pos < len(personajes)):
       print (personajes[pos])
       barrido_r(personajes,pos+1)

barrido_r (personajes,0)

def buscar(personajes,pos):
    if(pos< len(personajes)):
        if(personajes[pos] == 'Yoda'): 
            return pos
        else:
            return buscar(personajes, pos+1)
    else:
        print ('No se ha encontrado a Yoda')
        return -1

buscar (personajes,0)

print ('Yoda esta en la posicion: ',(buscar(personajes, 0)))