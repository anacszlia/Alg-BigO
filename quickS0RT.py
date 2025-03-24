
#A notação Big O para quicksort ,que é um dos algoritmos mais velozes de ordenação é O(n log n)
def quicksort(array):
    if len(array)<2:
        return array #caso-base :se tem um termo,não precisa ordernar
    else:
        pivo=array[0]
        menores=[i for i in array[1:] if i<=pivo]
        maiores=[i for i in array[1:] if i>pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)
print(quicksort([10,32,8,21,7,3,4]))
