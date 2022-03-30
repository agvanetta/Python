# Son parecidos a un objeto / array
# Las tuplas se representan escribiendo los elementos entre parentesis y separados por coma.

#Ejemplo de una Tupla ; no se puede modificar

operaciones = [(37580489, "20/9/2021", "V", True, "TSLA",
                5.0, 8883, "20/9/2021", 5, 8901.5, 44507.5)]

# Slicing (La sintaxis) permite cortar un fragmento de una secuencia
# "lista[desde:hasta:paso]"

lista = list(range(10))
lista

lista2 = lista[2:6:1] #Desde el 2 hasta el 6, de 1 en 1. [2, 3, 4, 5]
print(lista2)

# Modulos
#Fechas y tiempos
print (int("2021-11-15".split("-")[2]))

import datetime as dt

hora = dt.datetime.now()
print(hora)

from datetime import datetime as dt2

# Manejo de excepciones

diccionario = {}
try:
    diccionario["clave"]
except:
    print("Hubo un problema")#pass