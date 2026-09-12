N, M = map(int, input().split())
parent = [_ for _ in range(N + 1)]
respostas = []

def union(a, b):
    raiz_a = find(a)
    raiz_b = find(b)
    if raiz_a != raiz_b:
        parent[raiz_a] = raiz_b

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

for _ in range(M):
    O, A, B = map(int, input().split())
    if O == 1:
        union(A, B)
    if O == 2:
        resposta1, resposta2 = find(A), find(B)
        respostas.append("SIM" if resposta1 == resposta2 else "NAO")

print('\n'.join(respostas))

# [0, 2, 3, 3, 5, 5, 6]
#  0  1  2  3  4  5  6
# grupos: {1, 2, 3}, {4, 5}, {6}