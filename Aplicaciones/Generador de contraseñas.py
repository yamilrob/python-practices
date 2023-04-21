#Generador de contraseñas

import random
import string 

condi= string.ascii_letters + string.digits + string.punctuation 

longitud= int(input("Ingrese la longitud de la contaseña: "))

contraseña= ''.join(random.choice(condi) for i in range(longitud))

print(contraseña)