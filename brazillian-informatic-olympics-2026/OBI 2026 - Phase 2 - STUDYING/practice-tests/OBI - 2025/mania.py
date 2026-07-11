pos = [
    (-1, 0), (1, 0),
    (0, 1), (0, -1)
]
N, M = map(int, input().split())
bandeja = [list(map(int, input().split())) for l in range(N)]
custo_A = 0
custo_B = 0
for l in range(N):
    for c in range(M):
        valor = bandeja[l][c]
        if (l + c) % 2 == 0:
            if valor % 2 == 0: custo_A += 1
            if valor % 2 != 0: custo_B += 1
        else:
            if valor % 2 != 0: custo_A += 1
            if valor % 2 == 0: custo_B += 1

print(min(custo_A, custo_B))
config = 'A' if custo_A < custo_B else 'B'

for l in range(N):
    for c in range(M):
        if (l + c) % 2 == 0: #Posicao Par
            if config == 'A' and bandeja[l][c] % 2 == 0:
                bandeja[l][c] += 1
            elif config == 'B' and bandeja[l][c] % 2 != 0:
                bandeja[l][c] += 1
        else: #Posicao Impar
            if config == 'A' and bandeja[l][c] % 2 != 0:
                bandeja[l][c] += 1
            elif config == 'B' and bandeja[l][c] % 2 == 0:
                bandeja[l][c] += 1
print(*bandeja)