#Escribir un programa que pida al usuario una letra y compruebe si es una vocal.

letra= input("Ingrese una letra: ")

if letra in "aeiouAEIOU":
    print ("La letra es una vocal")
else: 
    print("No es un vocal")