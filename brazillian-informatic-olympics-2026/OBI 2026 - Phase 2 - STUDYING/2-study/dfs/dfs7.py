N, M = map(int, input().split())
conexoes = {}
visitados = set()
no_caminho = set()
ordem = []
tem_ciclo = False
ciclo_encontrado = 0
for d in range(M):
    A, B = map(int, input().split())
    conexoes.setdefault(A, []).append(B)
def dfs(atual, conexoes, visitados, no_caminho):
    global ciclo_encontrado
    visitados.add(atual)
    no_caminho.add(atual)
    ordem.append(atual)
    for v in conexoes.get(atual, []):
        if v in no_caminho:
            indice_inicio = ordem.index(v)
            ciclo_encontrado = ordem[indice_inicio:]
            return True
        if v not in visitados:
            if dfs(v, conexoes, visitados, no_caminho):
                return True
    ordem.pop()
    no_caminho.remove(atual)
    return False
for a in range(1, N+1):
    if a not in visitados:
        if dfs(a, conexoes, visitados, no_caminho):
            tem_ciclo = True
            break
if tem_ciclo:
    print("INVÁLIDO")
    for d in ciclo_encontrado:
        print(d)
else:
    print("VÁLIDO")