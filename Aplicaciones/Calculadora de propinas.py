#Calculadora de propinas

porce1= 0.2 
porce2= 0.15 

monto= float(input("Monto total del servicio: "))

total1= porce1 * monto
total2=porce2 * monto

print("Propina 20% es: " + str(total1) + "\n"+ "Propina 15% es: " + str(total2))