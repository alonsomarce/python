"""
print("Hola Mundo")

nombre = "Carlitos"
edad = 30


a = 2 + 3 + 5
print(a)

#Calcular superficie pidiendo lado
"""

"""Esta funcion calcula
la superficie pidiendo el lado"""


"""
lado = int( input("Ingresar el lado: "))
superficie=lado*lado
print(superficie)
"""

"""
nombre = input("Decime tu nombre: ") #Emiliano

if(nombre[0]=='E'):
    print("Empieza con la letra E")
    print("Sigo adentro porque empieza con e")

print("Sigue el programa")
"""

"""
def suma_numeros(numeros): #Bloque 1
        suma = 0 #Bloque 2
        for n in numeros: #Bloque 2
            suma += n #Bloque 3
            print(suma) #Bloque 3
        return suma #Bloque 2
"""

"""
primer_nombre="Maria"

print(len(primer_nombre))
print(primer_nombre.upper())
"""

"""
var1 = "Hola"
var2 = "python"
var3 = var1 + " " + var2
print(var3)


nombre="Juan"
edad=30
print(nombre, "tiene", edad, "anios")


print("%s tiene %d anios"%(nombre,edad))

# %s es un string, %d es un decimal

print("{} tiene {} anios".format(nombre,edad))


#estas 3 lineas traen el mismo resultado
print(nombre, "tiene", edad, "anios")
print("%s tiene %d anios"%(nombre,edad))
print("{} tiene {} anios".format(nombre,edad))
"""


"""
lista = [1,3,5,7,8,12,87]
#si siete esta en la lista

print(7 in lista)  #TRUE si esta, o FALSE si no esta


eliminado=lista.pop(1)    #elimina el elemento de posicion 1 >> recordar que empieza de posicion 0

print(lista)
print(eliminado)


resultado = 2**3    #esto calcula la potencia
print(resultado)
"""

"""
x=1
x = x+2     # x += 2  es lo mismo que x=x+2
print(x)
"""

"""
#LISTAS

lista1=[10, 5, 3]   #lista de enteros

lista2=[1.78, 2.66, 1.55, 89,4] #lista de valores float
lista3=["lunes", "martes", "miercoles"]     #lista de string
lista4=["juan", 45, 1.92, ["maria", "juan"]]
"""

"""
list1=[1, "" , 2]
print(list1[2])
"""


#DICCIONARIOS (clave - valor)
#No pueden haber 2 claves iguales, pero si 2 valores iguales

productos = {'manzana':200, 'cynar':600, 'cafe'=350}
print(productos)

# el append no funciona porque es una lista


nombre=input("Che, mete el nuevo producto:")
precio=int( input('mete el precio: '))
productos[nombre]=precioprint(productos)