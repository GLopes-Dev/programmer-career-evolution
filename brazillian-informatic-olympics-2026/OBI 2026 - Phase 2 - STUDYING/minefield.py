N = int(input())
matriz = []
matrizR = []
for i in range(N):
    A = list(map(int, input().split()))
    matriz.append(A)

print(matriz)

for l in range(N):
    for c in range(N):
        