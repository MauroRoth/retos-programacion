def sumaVsObjetivo(nums, objetivo):
    n = len(nums)
    list1 = []
    for i in range(1<<n): 
        suma = 0
        list2 = []
        for j in range(n):
            if(i&(1<<j)!=0):
                list2.append(nums[j])
                suma += nums[j]
        if suma == objetivo:
            list1.append(list2)
    return list1

arr = [1,5,3,2]
objetivo = 6
print(sumaVsObjetivo(arr,objetivo))
