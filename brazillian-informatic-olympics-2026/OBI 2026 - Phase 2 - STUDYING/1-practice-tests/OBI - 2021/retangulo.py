import sys
N = int(sys.stdin.readline())
circulo = list(map(int, sys.stdin.readline().split()))
soma = 0
for c in range(2, N):
    soma_ref = circulo[0] + circulo[1]
    soma += circulo[c]
    if soma == soma_ref:
        is_retangle = True
        soma = 0
    else:
        is_retangle = False
if is_retangle:
    print("S")
else:
    print("N")