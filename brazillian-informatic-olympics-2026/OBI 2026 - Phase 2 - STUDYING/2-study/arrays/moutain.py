N = int(input())
alturas = list(map(int, input().split()))
picos = 0
for a in range(N):
    if 0 < a < N:
        if alturas[a - 1] < alturas[a] > alturas[a + 1]:
            picos += 1
print(picos)

#Alterando indice do loop

N = int(input())
alturas = list(map(int, input().split()))
picos = 0
for a in range(1, N-1):
    if alturas[a-1] < alturas[a] > alturas[a + 1]:
        picos += 1
print(picos)