import sys

N = int(sys.stdin.readline())
quadrado = [list(map(int, sys.stdin.readline().split())) for linha in range(N)]
ref = sum(quadrado[0])
diagp = 0
diagS = 0
for linha in quadrado:
    if sum(linha) != ref:
        ref = 0
        break

if ref != 0:
    for c in range(N):
        soma = 0
        for l in range(N):
            soma += quadrado[l][c]
        if soma != ref:
            ref = 0
            break
if ref != 0:
    soma = 0
    for l in range(N):
        N = N - 1
        diagp += quadrado[l][l]
        diagS += quadrado[l][c]
    if diagp != ref or diagS != ref:
        ref = 0
print(ref)
