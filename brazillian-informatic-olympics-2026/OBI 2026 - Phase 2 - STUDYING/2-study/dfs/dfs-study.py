import sys
sys.setrecursionlimit(300000)


#DFS
def dfs(l, c):
    visitados[l][c] = True

    for dl, dc in direcoes:
        nova_l = l + dl
        nova_c = c + dc
        if 0 <= nova_l < L and 0 <= nova_c < C and visitados[nova_l][nova_c] == False and mapa[nova_l][nova_c] == 1:
            dfs(nova_l, nova_c)
#Variaveis
L, C = map(int, input().split())
mapa = []
visitados = [[False] * C for _ in range(L)]
contador_ilhas = 0
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#Matriz Input
for l in range (L):
    linha = list(map(int, input().split()))
    mapa.append(linha)

#Matriz Percorrer
for l in range(L):
    for c in range(C):
        celula = mapa[l][c]
        if visitados[l][c] == False and celula == 1:
            dfs(l, c)
            contador_ilhas += 1

print(contador_ilhas)
