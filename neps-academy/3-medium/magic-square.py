N = int(input())
square = []
ref = 0
soma = 0
sum_diagp = 0
sum_diagsec = 0
for L in range(N):
    row = list(map(int, input().split()))
    if L == 0:
        ref = sum(row)
    square.append(row)

for linha in square:
    if sum(linha) != ref:
        ref = -1
        break

if ref != -1:
    for c in range(N):
        for l in range(N):
            soma += square[l][c]
        if soma != ref:
            ref = -1
            break
        soma = 0

if ref != -1:
    c = N - 1
    for l in range(N):
        sum_diagp += square[l][l]  
        sum_diagsec += square[l][c]
        c -= 1
    if sum_diagp != ref or sum_diagsec != ref:
        ref = -1
print(ref)
