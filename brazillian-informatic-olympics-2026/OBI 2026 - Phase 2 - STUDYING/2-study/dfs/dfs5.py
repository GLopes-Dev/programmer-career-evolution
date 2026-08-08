L, C = map(int, input().split())
mapa = []
visitados = [[False] * C for _ in range(L)]
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
maior_ilha = 0
total_terras = 0
def dfs(l, c):
    global total_terras
    total_terras += 1
    visitados[l][c] = True
    for dl, dc in direcoes:
        nova_l = l + dl
        nova_c = c + dc
        if (0 <= nova_l < L and 0 <= nova_c < C
            and mapa[nova_l][nova_c] == 1 and not visitados[nova_l][nova_c]):
            dfs(nova_l, nova_c)

for l in range(L):
    linha = list(map(int, input().split()))
    mapa.append(linha)

for l in range(L):
    for c in range(C):
        celula = mapa[l][c]
        if celula == 1 and not visitados[l][c]:
            dfs(l, c)
            if total_terras > maior_ilha:
                maior_ilha = total_terras
            total_terras = 0

print(maior_ilha)