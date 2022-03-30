#Sentencia if
# else :
    #pass

precio = 140

if (precio < 130):
    print ("El precio es menor a 130")
elif (precio >= 130 and precio <200):
    print ("El precio esta en el rango de 130 a 200")
else:
    print ("El precio es mayor o igual a 200")

# Sentencia for

print ("Inicio")
for elemento in [0,1,2,3]: # o range(3)
    print (f"Iteracion con el elemento {elemento}")
print ("Fin")

# While

i = 0
while i < 5:
    #ejecuta codigo
    print(i)
    i+=1

while True:
    i = i + 1
    if ( i == 20):
        break
