# Anagrama
# Condiciones:
# palabras con misma cantidad y mismas letras
# que sean palabras distintas
# y que las letras esten en un orden diferente

def anagrama1 (palabra1, palabra2):
    condicion1 = sorted(palabra1) == sorted(palabra2) 
    condicion2 = palabra1 != palabra2 
    condicion3 = True
    for i in range(len(palabra1)):
        for j in range(len(palabra2)):
            condicion3 = condicion3 and not(i==j and palabra1[i]==palabra2[j])
    return condicion1 and condicion2 and condicion3 

def anagrama2 (palabra1, palabra2):
    if palabra1 != palabra2:
        if sorted(palabra1) == sorted(palabra2):
            for i in range(len(palabra1)):
                for j in range(len(palabra2)):
                    if i==j and palabra1[i]==palabra2[j]:
                        return False
            return True
        return False
    return False

  
    
palabra1 = 'medanos'
palabra2 = 'nsdeoma'
print(anagrama1 (palabra1, palabra2))
print(anagrama2 (palabra1, palabra2))  