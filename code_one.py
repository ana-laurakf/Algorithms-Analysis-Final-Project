import heapq # para usar heap em Python

# Dica: Você precisa modificar o algoritmo de dijkstra abaixo para resolver o problema!

def dijkstra(graph, source, fim):
    """
    Dijkstra O((|E| + |V|) log |V|) com heap binário.

    Parâmetros:
      graph: dicionário (lista de adjacência) representando grafo valorado com arestas não-negativas.
      source: nó de origem.

    Retorna:
      dist: dicionário com a menor distância da origem para cada nó.
            Para nós inalcançáveis, distância = float('inf').
      parent: dicionário com o predecessor imediato no caminho mínimo
              (None para a origem e para nós inalcançáveis).
    """

    # Inicialização
    processado = {v : False for v in graph.keys()}  # para marcar nós processados
    dist = {v : float('inf') for v in graph.keys()}
    parent = {v : None for v in graph.keys()}

    dist[source] = 0  # Origem começa com distância zero

    fila = [(0, source)]


    while fila:  # enquanto fila não for vazia
        du, u = heapq.heappop(fila)  # extrai nodo com menor distância na fila
    
        if processado[u]:
            continue
        processado[u] = True

        if u == fim:
            return dist[fim]
        
        if u in graph:
            for v, wv in graph[u]:    # para cada vizinho v de u
                novo_dv = du + wv     # distância até u mais peso da aresta u-v
                if novo_dv < dist[v]: # se distância menor que a atual
                    dist[v] = novo_dv
                    parent[v] = u
                    heapq.heappush(fila, (novo_dv, v))  # coloca v na fila com sua distância atual da origem

    return float('inf') ##Caso não exista um caminho

# Leitura da entrada:
n, m = (int(x) for x in input().split())
graph = {}
for _ in range(m):
    a, b = input().split()
    
    # Escreva aqui o código preenchendo o grafo
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    #preenche o grafo coloca dist como 1
    graph[a].append((b, 1))  
    graph[b].append((a, 1))


dist1 = dijkstra(graph, 'Entrada', '*')
dist2 = dijkstra(graph, 'Saida', '*')

distTotal = dist1 + dist2 #somando as distancias encontradas
# Escreva aqui o código para imprimir a resposta
print(distTotal)
