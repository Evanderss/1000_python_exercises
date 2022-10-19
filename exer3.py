# Obtener la fecha y hora actuales en el sistema
# Importamos la libería que viene por default en python
import datetime
# Podemos usar este formato que no es tán practico, primero creamos una variable despúes le pasamos 
# y sobre datetime usamos el objeto datetime y sobre este la función now
ahora = datetime.datetime.now()
print(ahora)
# También podemos usar este formato que es mucho más práctico desde mi perspectiva
# Primero invocamos el método strftime y pasamos la cadena de formateo con los datos que queremos
print()
print(ahora.strftime("%d/%m/%Y %H:%M:%S"))