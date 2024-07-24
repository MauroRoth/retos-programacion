def potencia(c):
    if len(c)==0:
        return[[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

def imprime_ordenado(c):
    for e in sorted(c, key=lambda s: (len(s), s)):
        print(e)

def sumaSubconjuntos(c):
    for t in potencia(c):
        print(t,sum(t))

def combinaciones(c,n):
    return [s for s in potencia(c) if len(s) == n]

c = [1,2,3]
sumaSubconjuntos(c)

helados = ['cereza','chocolate','fresa','nuez','vainilla']
imprime_ordenado(combinaciones(helados,3))
