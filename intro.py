class Hotel:
    pass
#######################################################################################################
# Mientras que las clases proveen la estructura, las instancias son los objetos reales que creamos
# en nuestro programa: un hotel llamado PlatziHotel o Hilton. Otra forma de pensarlo es que las clases 
# son como un formulario y una vez que se llena cada copia del formulario tenemos las instancias que 
# pertenecen a dicha clase. Cada copia puede tener datos distintos, al igual que cada instancia es
# distinta de las demas (aunque todas pertenecen a una misma clase).
#######################################################################################################
# Una vez que tenemos una clase llamada Hotel podemos generar una instancia llamando al 
# constructor de la clase.
hotel = Hotel()
################################ Atributos de la instancia ############################################
# Todas las clases crean objetos y todos los objetos tienen atributos. 
# Utilizamos el método especial __init__ para definir el estado inicial de nuestra instancia. 
# Recibe como primer parámetro obligatorio self (que es simplemente una referencia a la instancia).
#######################################################################################################
class Hotel:
    
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0
##
hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)
print(hotel.lugares_de_estacionamiento) # 20
