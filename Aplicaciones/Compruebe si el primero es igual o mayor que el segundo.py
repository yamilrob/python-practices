#Escribir un programa que pida al usuario dos números y compruebe si el primero es igual o mayor que el segundo

dato1= int(input("Ingrese un número: "))
dato2= int(input("Ingrese un número: "))

if dato1 >= dato2:
 print(str(dato1) + " es mayor o igual que : " + str(dato2))
else:
 print("Error")