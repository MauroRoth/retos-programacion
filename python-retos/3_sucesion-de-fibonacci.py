def fibonacciIterativo (numero):
    serie = list()
    for i in range(numero):
        if i<2:
            serie.append(i)
        else:
            serie.append(serie[i-1]+serie[i-2])
    return serie

def fibonacciRecursivo(numero):
    serie = list()
    if numero == 1:
        serie.append(0)
    else:
        serie.append(1)
    return serie
    #else:
        # return fibonacci2(numero-1)+fibonacci2(numero-2)

numero = 3
print(fibonacciIterativo(numero))
print(fibonacciRecursivo(numero))

