# Calcular el valor futuro para una cantidad, interés y número de años.
def valor_futuro(vp, i, n):
    return vp * (1 + i) ** n

if __name__ == "__main__":
    valor_presente = 5000
    interes = 3.7
    periodos = 7
    print(valor_futuro(valor_presente, interes/100, periodos))