#código do problema dois
#ir e vir - deve testar se o grafo é fortemente conexo, ou seja se existe um caminho de cada vértice para todos os outros vértices
import sys 
from collections import deque

    #parte de teste de componentes fortemente conexos + operações - códigos do professor Lucas Alegre
def init_visitados(g):
        """Dicionário mapeando todo nodo para False (não-visitado)."""
        return {n : False for n in g.keys()}

def toposort(g):
        """Ordenamento Topológico via DFS."""
        visitados = init_visitados(g)
        order = []

        def dfs_rec(g, s, visitados, order):
            visitados[s] = True
            for v in g[s]:
                if not visitados[v]:
                    dfs_rec(g, v, visitados, order)
            order.append(s)
        
        for i in g.keys():
            if not visitados[i]:
                dfs_rec(g, i, visitados, order)
        
        return order[::-1]  # reverte a lista

def reverse_graph(g):
        """Dado um dígrafo, retorna um dígrafo com a direção de todas as arestas invertidas."""
        rev_g = {i : [] for i in g.keys()}
        for n, vizinhos in g.items():
            for v in vizinhos:
                rev_g[v].append(n)
        return rev_g

def kosaraju_shamir(g):

        """Algoritmo de Kosaraju-Shamir para encontrar Componentes Fortemente Conexos em um Dígrafo."""
        rev_g = reverse_graph(g)
        order = toposort(rev_g) 
        resultado = 0

        visited = init_visitados(g)
        components = {}
        c = 0

        def dfs(g, s, visitados, components, c):
            visitados[s] = True
            components[s] = c
            for v in g[s]:
                if not visited[v]:
                    dfs(g, v, visited, components, c)

        for i in order:
            if not visited[i]:
                dfs(g, i, visited, components, c)
                c += 1

        if (c == 1):
            resultado = 1
            

        return resultado

#parte de processamento dos grafos em dicionários
while True:
    n, m = (int(x) for x in input().split())
    
    if n == 0 and m == 0:
        break
    #inicializa os grafos normal e invertido

    graph = {i: [] for i in range(1, n + 1)}
    graph_rev = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        v, w, p = (int(x) for x in input().split())
        
        graph[v].append(w)
        graph_rev[w].append(v)
        
        # só adicionamos o caminho da volta se a rua for de mão dupla (p == 2)
        if p == 2:
            graph[w].append(v)
            graph_rev[v].append(w)

  

    resultado = kosaraju_shamir(graph)
    print(resultado) 
