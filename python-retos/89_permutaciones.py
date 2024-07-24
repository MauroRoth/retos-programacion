def permutaLetras(palabra):
    letras=[]
    for letra in palabra:
        letras.append(letra)
    print(letras)
    palabra_nueva = ""
    for letra in reversed(letras):
        palabra_nueva += letra
    print(palabra_nueva)
    #return lista_palabras

permutaLetras("sol")
