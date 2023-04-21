#Adivina el número

import random 

entrada= int(input("Ingrese un número del 0 al 20: "))

nun_aleatorio= random.randint (0 , 20)

if entrada < nun_aleatorio:
    print("Es muy bajo")
if entrada > nun_aleatorio: 
    print ("es muy alto")
if entrada == nun_aleatorio: 
    print("Eres el ganador")