N, M = map(int, input().split())
conexoes = {}
visitados = set()
caminho = set()
tem_ciclo = False
for c in range(M):
    A, B = map(int, input().split())
    conexoes.setdefault(A, []).append(B)
    conexoes.setdefault(B, []).append(A)
def dfs(atual, conexoes, visitados, caminho, origem):
    visitados.add(atual)
    caminho.add(atual)
    for v in conexoes.get(atual, []):
            if v == origem:
                continue
            if v in caminho:
                return True
            if v not in visitados:
                if dfs(v, conexoes, visitados, caminho, atual):
                    return True
    caminho.remove(atual)
    return False
for a in range(1, N + 1):
    if a not in visitados:
        if dfs(a, conexoes, visitados, caminho, a):
            tem_ciclo = True
            break

if tem_ciclo:
    print("S")
else:
    print("N")