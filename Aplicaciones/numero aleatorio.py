import random

num_aleatorio= random.randint(1,100)
# print(num_aleatorio)

dato = int(input("Adivine un número: "))



if dato == int(num_aleatorio):
    print("¡CORRECTO!")
else:
    if dato < num_aleatorio: 
        print("Demasiado bajo")
    else:
        print("Demasiado alto")