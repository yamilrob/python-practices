Contador de vocales

entrada=input("Ingrese una frase: ")
entrada_str= str(entrada)
vocales= ["a , e , i , o , u "]
contador = 0 
for i in (entrada): 
    if i.lower in vocales:
        contador =+1 
        print(contador)

texto = input("Introduce una cadena de texto: ")
contador = 0

for letra in texto:
    if letra.lower() in "aeiou":
        contador += 1

print("La cadena de texto introducida contiene", contador, "vocales.")
