diaMes= int(input(("Ingrese día del mes: " )))
mes= int(input(("Ingrese el mes: " )))
año_siglo= int(input(("Ingrese los últimos dos dígitos del año: " )))
siglo= int(input(("Ingrese dos primeros dígitos del año: " )))

DiaSemana = diaMes + ((13*mes - 1)/5) + año_siglo + (año_siglo/4) + (siglo/4) - 2*siglo

DiaSemana_1 = int(DiaSemana / 6) 

numeros= [1,2,3,4,5,6,7]
dias= ["DOMINGO","LUNES","MARTES","MIÉRCOLES","JUEVES","VIERNES","SÁBADO"]

nombre_dia= dias[numeros.index(DiaSemana_1)]

print("La fecha ingresada: " + str(diaMes) + " del mes: " + str(mes) + " es día: " + str(nombre_dia))

    




  


             