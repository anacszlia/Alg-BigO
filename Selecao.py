# ordenação por seleção tem sua notação como O(n²) que é mais lento do que o algoritmo de ordenação simples O(n)
def buscaMenor(arr):
    menor=arr[0]
    menor_indice=0
    for i in range(1,len(arr)):
        if arr[i]< menor:
            menor=arr[i]
            menor_indice=i
    return menor_indice

def ordenacaoporSelecao(arr):
    novoArr=[]
    # o loop calcula o tamanho do array inicialmente e nao se atualiza a cada remoção do arr
    for i in range(len(arr)):
        menor=buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

print(ordenacaoporSelecao([4,5,9,3,8,1]))