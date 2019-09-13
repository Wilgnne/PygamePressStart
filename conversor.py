def HorasParaAngulo (hora:int):
    t = hora / 24
    return (360 * t) - 90

def MinutosParaAngulo (minutos:int):
    t = minutos / 60
    return (360 * t) - 90