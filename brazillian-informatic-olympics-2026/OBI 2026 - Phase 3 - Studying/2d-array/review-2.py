N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
soma = 0

for l in range(N):
    for c in range(M):
        if c == 0 or c == M - 1 or l == 0 or l == N - 1:
            soma += matriz[l][c]

print(soma)