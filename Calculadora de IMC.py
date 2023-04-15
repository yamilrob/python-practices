Calculadora de IMC

peso= float(input("Ingrese su peso en kg: "))
altura= float(input("Ingrese su altura en metros: "))

imc= peso / altura
imc_r = round (imc, 2)

print("Indice de Masa Corporal: " + str(imc_r))