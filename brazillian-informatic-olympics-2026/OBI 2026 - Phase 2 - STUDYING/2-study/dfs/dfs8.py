L, C = map(int, input().split())
tela = [list(map(int, input().split())) for _ in range(L)]
visitados = [[False] * C for _ in range(L)]
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
regioes = 0

def dfs(l, c):
    visitados[l][c] = True
    cor = tela[l][c]
    for dl, dc in direcoes:
        nova_l = l + dl
        nova_c = c + dc
        if (0 <= nova_l < L and 0 <= nova_c < C
            and tela[nova_l][nova_c] == cor and
            not visitados[nova_l][nova_c]):
            dfs(nova_l, nova_c)

for l in range(L):
    for c in range(C):
        if not visitados[l][c]:
            dfs(l, c)
            regioes += 1

print(regioes)