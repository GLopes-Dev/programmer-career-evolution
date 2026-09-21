N, M = map(int, input().split())
conexoes = [n for n in range(N+1)]

def union(a, b):
    raiz_a = find(a)
    raiz_b = find(b)
    if raiz_a != raiz_b:
        conexoes[raiz_a] = raiz_b

def find(x):
    if conexoes[x] == x:
        return x
    conexoes[x] = find(conexoes[x])
    return conexoes[x]

for _ in range(M):
    a, b = map(int, input().split())
    union(a, b)

for i in range(1, N+1):
    find(i)
conexoes = set(conexoes)
print(len(conexoes) - 1)
