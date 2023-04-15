#Lista entrelazad

Amigos = ["Ana", "Juan", "Pedro"]
for amigo in Amigos:
    print ("Hola " + amigo)


lista1= [1,3,5,7,9]
lista2=[2,4,6,8,10]

lista_entrelazada= []

for elemento1 , elemento2 in zip(lista1 , lista2): 
    lista_entrelazada.append(elemento1) 
    lista_entrelazada.append(elemento2) 

print(lista_entrelazada)    