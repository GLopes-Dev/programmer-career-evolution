N, Q = map(int, input().split())
barracas = list(map(int, input().split()))
prefix = [0]
arrecadacao = []
for i in range(N):
    prefix.append(barracas[i] + prefix[i])
for _ in range(Q):
    a, b = map(int, input().split())
    arrecadacao.append(prefix[b] - prefix[a-1])
    # [0, 12, 19, 24, 44, 47, 58, 66, 72]
for _ in arrecadacao:
    print(_)
