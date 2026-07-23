import sys
N = int(sys.stdin.readline())
filmes = []
ultimo = -1
qtd = 0
for l in range(N):
    I, F = map(int, sys.stdin.readline().split())
    filmes.append((I, F))
filmes.sort(key=lambda x: x[1])
for i, j in filmes:
    if i >= ultimo:
        ultimo = j
        qtd += 1
print(qtd)