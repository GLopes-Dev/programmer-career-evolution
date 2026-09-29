from collections import deque
import sys

sys.setrecursionlimit(200000)
N = int(input())
tabela = [list(map(int, input().strip())) for _ in range(N)]
conexao = [n for n in range(N+1)]
E = int(input())
entrevistas = []
for i in range(E):
    lista = deque(list(map(int, input().split())))
    lista.popleft()
    entrevistas.append(lista)

def union(a, b):
    raiz_a = find(a)
    raiz_b = find(b)
    if raiz_a != raiz_b:
        conexao[raiz_a] = raiz_b

def find(x):
    if conexao[x] == x:
        return x

    conexao[x] = find(conexao[x])
    return conexao[x]

for l in range(N):
    for c in range(N):
        if tabela[l][c] == 1:
            union(l+1, c+1)

for i in range(1, N+1):
    find(i)

for l in range(E):
    ordem = set()
    for valor in entrevistas[l]:
        ordem.add(find(valor))
    if len(entrevistas[l]) > len(ordem):
        print("S")
    else:
        print("N")