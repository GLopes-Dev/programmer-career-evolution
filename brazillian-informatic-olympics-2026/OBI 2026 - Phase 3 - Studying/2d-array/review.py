N, M = map(int, input().split())
matriz = [list(map(int, input().split())) for _ in range(N)]
maior_valor = matriz[0][0]
index = (0, 0)

for l in range(N):
    for c in range(M):
        element = matriz[l][c]
        if element > maior_valor:
            index = (l, c)
            maior_valor = element

print(maior_valor)
print(*index)

