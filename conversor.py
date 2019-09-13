def HorasParaAngulo (hora:int):
    t = hora / 24
    return (360 * t) - 90

def MinutosParaAngulo (minutos:int):
    t = minutos / 60
    return (360 * t) - 90

def distancia (ponto1, ponto2):
    x1, y1 = ponto1
    x2, y2 = ponto2

    resultado = (x2 - x1) ** 2 + (y2 - y1) ** 2
    resultado = resultado ** 0.5
    return resultado