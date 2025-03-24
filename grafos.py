# Grafos ou pesquisa em largura são conjuntos de conexões formados por vértices e arestas
#  é usado para calcular o menor numero de etapas para alcançar determinado objetivo
# aplicaçoes de Ia ,corretores ortográficos
#  cada vértice tem um ou varios vizinhos

grafo = {}
grafo["eu"] = ["chiquinho", "claudia", "clodoaldo"]
grafo["claudia"] = ["raposinha", "branquinho"]
grafo["branquinho"] = ["negrinho"]
grafo["clodoaldo"] = ["tita", "tiburcio", "tubianin", "tuca"]
grafo["chiquinho"] = []  # Adicionando para evitar KeyError
grafo["raposinha"] = []
grafo["negrinho"] = []
grafo["tita"] = []
grafo["tubianin"] = []
grafo["tuca"] = []
grafo["tiburcio"] = []

from collections import deque

def pessoa_e_vendedora(nome):
    return nome[-1] == 'a'

def pesquisa(nome):
    fila_da_pesquisa = deque()
    fila_da_pesquisa.extend(grafo[nome])
    visitados = set()

    while fila_da_pesquisa:
        pessoa = fila_da_pesquisa.popleft()
        visitados.add(pessoa)
        if pessoa_e_vendedora(pessoa):
            print(pessoa + " é vendedor de manga ")
            return True
        else:
            print(pessoa + " nao é vendedor de manga ")
            fila_da_pesquisa.extend(grafo[pessoa])

    return False

pesquisa("eu")
