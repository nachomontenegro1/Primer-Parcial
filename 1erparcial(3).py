from lista import Lista
lista_avengers=Lista()


lista1 = [
        {'nombre': 'Captain America','Año de aparicion': 1941, 'Heroe': True},
        {'nombre': 'Iron-Man','Año de aparicion': 1963, 'Heroe': True},
        {'nombre': 'Hawkeye','Año de aparicion': 1963, 'Heroe': True},
        {'nombre': 'Spider-Man','Año de aparicion': 1962, 'Heroe': True},
        {'nombre': 'Black Panther','Año de aparicion': 1966, 'Heroe': True},
        {'nombre': 'Thor','Año de aparicion': 1962, 'Heroe': True},
        {'nombre': 'Thanos','Año de aparicion': 1973, 'Heroe': False},
        {'nombre': 'Scalet Witch','Año de aparicion': 1964, 'Heroe': True},
     ]
for personaje in lista1:
    lista_avengers.insertar(personaje,'name')


lista_aux = [
        {'nombre': 'Black Widow','Año de aparicion': 1964, 'Heroe': True},
        {'nombre': 'Hulk','Año de aparicion': 1962, 'Heroe': True},
        {'nombre': 'Rocket Racoonn','Año de aparicion': 1976, 'Heroe': True},
        {'nombre': 'Loki','Año de aparicion': 1949, 'Heroe': False},
     ]

for personaje in lista_aux:
    lista_avengers.insertar(personaje,'nombre')

lista_avengers.barrido()
print()

#Punto A
pos = lista_avengers.busqueda ('Thor', 'nombre')
if (pos != -1):
    print (f'Thor esta en la pos {pos}')

#Punto B
pos2 = lista_avengers.busqueda ('Scalet Witch','nombre')
if (pos2 != -1):
        lista_avengers.obtener_elemento(pos2)['nombre'] = 'Scarlet Witch'
        print ()
    
