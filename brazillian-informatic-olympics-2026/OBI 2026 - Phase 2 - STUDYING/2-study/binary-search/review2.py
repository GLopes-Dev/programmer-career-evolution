import sys
D, M = map(int, sys.stdin.readline().split())

def search(D, M):
    potencia_min = 1
    potencia_max = M * (1 + D)
    while potencia_min <= potencia_max:
        potencia_atual = (potencia_min + potencia_max) // 2
        if potencia_atual >= M * (1 + D):
            potencia_certa = potencia_atual
            potencia_max = potencia_atual - 1
        else:
            potencia_min = potencia_atual + 1

    return potencia_certa     

print(search(D, M))
