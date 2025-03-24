#grafos ponderados

grafo={}
grafo["inicio"]={}
grafo["inicio"]["a"]=6
grafo["inicio"]["b"]=2

grafo["a"]={}
grafo["a"]["fim"]=1

grafo["b"]={}
grafo["b"]["a"]=3
grafo["b"]["fim"]=5

grafo["fim"]={}
print(grafo["inicio"].keys())
#tempo que nao se sabe para chegar até o final
infinito=float("inf")
custos={
    "a":6,
    "b":2,
    "fim":infinito

}
pais={
    "a":"inicio",
    "b":"inicio",
    "fim":None
}
# garantir que os vertices nao sejam pprocessados mais de uma vez
processados = []

def ache_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    node_custo_baixo = None
    for node in custos:
        if custos[node] < custo_mais_baixo and node not in processados:
            custo_mais_baixo = custos[node]
            node_custo_baixo = node
    return node_custo_baixo

node = ache_custo_mais_baixo(custos)
while node is not None:
    custo = custos[node]
    vizinhos = grafo[node]
    for i in vizinhos.keys():
        novo_custo = custo + vizinhos[i]
        if custos[i] > novo_custo:
            custos[i] = novo_custo
            pais[i] = node
    processados.append(node)
    node = ache_custo_mais_baixo(custos)

print(custos)


