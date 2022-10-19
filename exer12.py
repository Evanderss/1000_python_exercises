# Imprimer el calendario de un año y mes específico 
import calendar

año = int(input(("Ingresa el año: ")))
mes = int(input("Ingresa el número del mes: "))

print(calendar.month(año, mes))
