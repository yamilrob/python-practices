#Escribir un programa que lea una lista de números enteros y calcule la suma de todos los números pares en la lista.

dato = int(input("Ingrese un número: "))
acumulador= 0
while dato != -1: 
    acumulador= acumulador + int (dato)
    dato = int(input("Ingrese un número: "))
print (str(acumulador))