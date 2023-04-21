#Comprueba si es mayor que 10
#Escribir un programa que pida al usuario un número y compruebe si es mayor que 10.

dato= int(input("Ingrese un número: "))

try:
    dato= int(input("Ingrese un número: "))
    if dato < 10: 
        print ("Es menor que 10")
    else:
        print("Es mayor que 10")
except ValueError: 
    print("La dato es diferente a un número, ingrese un número")