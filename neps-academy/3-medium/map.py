

# import sys
sys.setrecursionlimit(20000)
L, C = map(int, input().split())
mapa = [list(input().lower()) for _ in range(L)]
copia = [[False] * C for _ in range(L)]
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ordem = []
def achar_herminone(l, c):
    ordem.append((l, c))
    copia[l][c] = True
    celula = mapa[l][c]
    for dl, dc in direcoes:
        nl = l + dl
        nc = c + dc
        if (0 <= nl < L and 0 <= nc < C
            and copia[nl][nc] == False and mapa[nl][nc] == "h"):
            achar_herminone(nl, nc)

for l in range(L):
    for c in range(C):
        if mapa[l][c] == "o":
            achar_herminone(l, c)

print(ordem[-1][0] + 1, ordem[-1][1] + 1)







#Iterable DFS
import sys
sys.setrecursionlimit(20000)
L, C = map(int, input().split())
mapa = [list(input().lower()) for _ in range(L)]
copia = [[False] * C for _ in range(L)]
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ordem = []
def achar_herminone(l_inicial, c_inicial):
    pilha = [(l_inicial, c_inicial)]
    while pilha:
        l, c = pilha.pop()
        if copia[l][c]:
            continue
        ordem.append((l, c))
        copia[l][c] = True
        for dl, dc in direcoes:
            nl = l + dl
            nc = c + dc
            if (0 <= nl < L and 0 <= nc < C
                and copia[nl][nc] == False and mapa[nl][nc] == "h"):
                pilha.append((nl, nc))

for l in range(L):
    for c in range(C):
        if mapa[l][c] == "o":
            achar_herminone(l, c)

print(ordem[-1][0] + 1, ordem[-1][1] + 1)