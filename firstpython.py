def calcular(factor, *valores, redondear=False, **kwargs):
    resultado = [v * factor for v in valores]

    if redondear:
        resultado = [round(x, 2) for x in resultado]

    return resultado

calcular(2, 1.212,2,3, redondear=True)