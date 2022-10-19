# Calcular el área de un triángulo

base = None
altura = None
while True: 
    try:
        base = float(input("Ingresa la base del triáunglo: "))
        break
    except:
        print("Debe ingresar un número")
        break
while True: 
    try:
        altura = float(input("Ingresa la altura del triáunglo: "))
        break
    except:
        print("Debe ingresar un número")
        break
area = base * altura / 2

print(f"El área del triángulo es {area}")