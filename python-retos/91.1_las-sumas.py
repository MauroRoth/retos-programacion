def findSubset(nums):
    n = len(nums)
    sets=[]
    for i in range(1<<n):
        subsets=[]
        for j in range(n):
            if i&(1<<j)!=0:
                subsets.append(nums[j])
        sets.append(subsets)
    return sets

def sumaVsObjetivo(listas, objetivo):
    lista1=[]
    for lista in findSubset(listas):
        suma = 0
        for element in lista:
            suma += element
        if suma == objetivo:
            lista1.append(lista)
    return lista1

arr = [1,5,3,2,1]
objetivo = 6
print(sumaVsObjetivo(arr,objetivo))
