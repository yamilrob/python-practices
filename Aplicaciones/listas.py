#Numero par 
acum = 0

for i in range(5): 
    numero = int(input("Ingrese un número("+ str(i) +"): "))
    if numero % 2 == 0:
        print("Es un número par")
        acum = acum + numero
    else: 
        print("Es un número impar")

print("La sumatoria de los numeros pares introducidos es: "  + str(acum))
