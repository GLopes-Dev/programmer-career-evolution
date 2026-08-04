import sys
pesos = list(map(int, sys.stdin.readline().split()))
D = int(sys.stdin.readline())

def simulate(pesos, middle):
    soma = 0
    d = 0
    for p in pesos:
        if p + soma > middle:
            d += 1
            soma = 0
        soma += p
    if soma > 0:
        d += 1

    return d

def achar_capacidade(pesos, D):
    left = max(pesos)
    right = sum(pesos)
    while left <= right:
        middle = (left + right) // 2
        dias = simulate(pesos, middle)
        if dias <= D:
            ans = middle
            right = middle - 1
        else:
            left = middle + 1

    return ans

C = achar_capacidade(pesos, D)
print(C)