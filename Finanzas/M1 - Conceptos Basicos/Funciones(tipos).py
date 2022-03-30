#def nombre_funcion (param1, param2):
    #sentencia1
    #sentencia2
    #sentencia3
    #return

#Funciones sin retorno
def valor_take_profit(precio, porcentaje):
    print(f"es valor de venta, el tp es {precio * (1 + porcentaje)}")

def funcion_v2 (nombre):
    print (f"Hola {nombre}")
    print ("Hola")

valor_take_profit(1000,0.05)

funcion_v2("Pupino")

# Funciones con parametros por nombre

def esElPrimeroMayor(num1, num2, num3):
    return num1>num2 and num1>num3

print(esElPrimeroMayor(3,2,1))

#Funcion sin parametros

def mostrat_terminos_y_condiciones():
    return "Esto es un string de condiciones"

#Funciones con parametros opcionales

def conviene_vender (mediarapida, precio, medialenta= 102.05):
    return mediarapida <= medialenta and precio <= mediarapida