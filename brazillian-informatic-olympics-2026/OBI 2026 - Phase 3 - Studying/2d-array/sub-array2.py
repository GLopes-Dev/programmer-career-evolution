N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
maior_soma = float("-inf")

for l in range(N - 1):
    for c in range(M - 1):
        soma = matriz[l][c] + matriz[l][c+1] + matriz[l+1][c] + matriz[l+1][c+1]
        maior_soma = max(maior_soma, soma)

print(maior_soma)