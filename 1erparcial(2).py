from cola import Cola 
from pila import Pila

cola_app = Cola ()
pila_ig = Pila ()

class gestor_notif (object):
    app,hora,mensaje = '','',''


def __init__(self,app, hora, mensaje):
    self.app= app
    self.hora= hora
    self.mensaje= mensaje


def __str__(self):
    return self.app+ '-. Hora: '+ self.hora+ '-. Mensaje:'+self.mensaje

dato = gestor_notif = ('Facebook','19:32','Sol. de Amistad')
cola_app.arribo(dato)
dato = gestor_notif = ('Instagram','20:00','Mencion en Historia')
cola_app.arribo(dato)
dato = gestor_notif = ('Twitter','17:40','Retweet')
cola_app.arribo(dato)
dato = gestor_notif = ('Instagram','19:32','Nuevo Seguidor')
cola_app.arribo(dato)
dato = gestor_notif = ('Twitter','22:55','Python')
cola_app.arribo(dato)
dato = gestor_notif = ('WhatsApp','23:12','Mama: Volve temprano croto')
cola_app.arribo(dato)
dato = gestor_notif = ('Facebook','10:33','MarketPlace')
cola_app.arribo(dato)

n_element = 0

while (n_element < cola_app.tamanio() ):
    dato = cola_app.mover_final()

print (dato) 
n_element += 1


# Punto C

n_element_C = 0
while (n_element_C < cola_app.tamanio()):
    dato = cola_app.atencion()
    if (dato.app != 'Facebook'):
        cola_app.arribo (dato)

        n_element_C += 1


#Punto D

n_element_D = 0
while (n_element_D < cola_app.tamanio()):
    dato = cola_app.mover_final()


    if ((dato.app == 'Twitter') and ('Python' in dato.mensaje)):
        print (dato)

        
        n_element_D += 1


#Punto E

n_element_E = 0

while (n_element_E < cola_app.tamanio()):
    dato = cola_app.mover_final()

    if (dato.nombre == 'Instagram' ):
        pila_ig.apilar (dato)

        n_element_E += 1

print ('Notificaciones de Instagram Registradas: ')
while (not pila_ig.pila_vacia()):
    print (pila_ig.desapilar)



