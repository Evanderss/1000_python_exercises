# Calcular la diferencia en dias de dos fechas dadas
from datetime import date, datetime

hoy = date(2022, 7, 13)
otra_fecha = date(2022, 7, 21)

diferencia = otra_fecha - hoy
print(diferencia.days)