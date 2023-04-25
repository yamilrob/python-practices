"""System module."""

MENSAJE = """Bienvenidos a la Calculadora =)
Operaciones permitidad son: suma, resta, multiplicación, división.
Para salir escriba Salir."""
print(MENSAJE)

ACUMULADOR = float(input("Ingrese número: "))
operacion = input("Ingrese la opración que quiere realizar: ")

while operacion != "Salir":
    if operacion == "suma":
        dato = float(input("Ingrese otro número: "))
        ACUMULADOR = ACUMULADOR + dato
        print(round(ACUMULADOR))
        operacion = input("Ingrese la opración que quiere realizar: ")
    elif operacion == "resta":
        dato = float(input("Ingrese otro número: "))
        ACUMULADOR = ACUMULADOR - dato
        print(round(ACUMULADOR))
        operacion = input("Ingrese la opración que quiere realizar: ")
    elif operacion == "multi":
        dato = float(input("Ingrese otro número: "))
        ACUMULADOR = ACUMULADOR * dato
        print(round(ACUMULADOR))
        operacion = input("Ingrese la opración que quiere realizar: ")
    elif operacion == "div":
        dato = float(input("Ingrese otro número: "))
        ACUMULADOR = ACUMULADOR / dato
        print(round(ACUMULADOR, 1))
        operacion = input("Ingrese la opración que quiere realizar: ")
