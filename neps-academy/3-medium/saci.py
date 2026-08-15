import sys
sys.setrecursionlimit(30000)
L, C = map(int, sys.stdin.readline().split())
toca = [list(map(int, sys.stdin.readline().split())) for _ in range(L)]
copia = [[False] * C for _ in range(L)]
salas = 0
direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def count(l, c):
    global salas
    salas += 1
    copia[l][c] = True
    if toca[l][c] == 2:
        return
    for dl, dc in direcoes:
        nl = l + dl
        nc = c + dc
        if 0 <= nl < L and 0 <= nc < C:
            if (copia[nl][nc] == False and toca[nl][nc] == 1) or toca[nl][nc] == 2:
                count(nl, nc)

for l in range(L):
    for c in range(C):
        if toca[l][c] == 3:
            count(l, c)

print(salas)
# salas = 5