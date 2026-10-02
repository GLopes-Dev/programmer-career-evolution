N, Q = map(int, input().split())
sensores_posicoes = []
sensores_veiculos = []
prefix = [0]
validos = []

def achar(A, B):
    left = 0
    right = len(sensores_posicoes) - 1
    answer = -1
    while left <= right:
        middle = (left + right) // 2
        if sensores_posicoes[middle] >= A:
            answer = middle
            right = middle - 1
        else:
            left = middle + 1
    left = 0
    right = len(sensores_posicoes) - 1
    answer2 = -1
    while left <= right:
        middle = (left + right) // 2
        if sensores_posicoes[middle] <= B:
            answer = middle
            left = middle + 1
        else:
            right = middle - 1

    return (answer, answer2)

for _ in range(N):
    P, V = map(int, input().split())
    sensores_posicoes.append(P)
    sensores_veiculos.append(V)

for v in sensores_veiculos:
    prefix.append(prefix[-1] + v)

for _ in range(Q):
    A, B = map(int, input().split())
    L, R = achar(A, B)
    if L == -1 or R == -1 or L > R:
        validos.append[0]
        continue
    else:
        soma = prefix[R + 1] - prefix[L]
    validos.append(soma)

for _ in validos:
    print(_)
