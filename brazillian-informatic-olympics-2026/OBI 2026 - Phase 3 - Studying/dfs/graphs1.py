from collections import defaultdict
N = int(input())
conexoes = defaultdict(list)
visitados = set()
vertices_alcancaveis = []

def dfs(conexoes, visitados, x):
    visitados.add(x)
    for v in conexoes[x]:
        if v not in visitados:
            print(v)
            dfs(conexoes, visitados, v)

# def dfs(conexoes, visitados, x):
#     pilha = [x]
#     visitados.add(x)
#     while pilha:
#         vertice = pilha.pop()
#         print(vertice)
#         for v in conexoes[vertice]:
#             if v not in visitados:
#                 visitados.add(v)
#                 pilha.append(v)

for _ in range(N):
    a, b = map(int, input().split())
    conexoes[a].append(b)
    conexoes[b].append(a)

dfs(conexoes, visitados, 1)

