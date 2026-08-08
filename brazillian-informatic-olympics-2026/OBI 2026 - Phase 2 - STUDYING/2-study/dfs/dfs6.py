N, M = map(int, input().split())
conexoes = {}
visitados = set()
contador_grupos = 0
for c in range(M):
    A, B = map(int, input().split())
    conexoes.setdefault(A, []).append(B)
    conexoes.setdefault(B, []).append(A)
def dfs(inicial, conexoes, visitados):
    pilha = [inicial]
    while pilha:
        atual = pilha.pop()
        if atual not in visitados:
            visitados.add(atual)
            for v in conexoes.get(atual, []):
                if v not in visitados:
                    pilha.append(v)

for a in range(1, N + 1):
    if a not in visitados:
        dfs(a, conexoes, visitados)
        contador_grupos += 1

print(contador_grupos)

# 1: [2, 3]
# 2: [1, 3]
# 3: [2, 1]
# 4: [5]
# 5: [4]
# 6: []
# 6 4
# 1 2
# 2 3
# 4 5
# 1 3

# (1, 2, 3, 4, 5, 6)