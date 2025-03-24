# Desempenho médio O(1) para pesquisar ,inserir e remover
# Exemplo de função hash eficiente = função SHA
# As tabelas hashs estão em todas as linguagens por padrão,em python uma tabela hash é a mesma 
# que um dicionário,no qual há seus itens e seus valores.Muito útil na procura de um intem que corresponda a um determinado valor,
# na verificação de itens repetidos com a função .get() ,como tradução de sites para endereços ip e 
# na utilização como cache(memorização dos dados)

cache={}

def pega_pag(url):
    if cache.get(url):
        return cache[url]
    else:
        dados=pega_dados_servidor(url)
        cache[url]=dados
        return dados
    
def pega_dados_servidor(url):
    # Simulando uma resposta do servidor
    return f"Dados da {url}"

print(pega_pag("http://exemplo.com"))
print(pega_pag("http://exemplo.com"))  # Deve retornar do cache