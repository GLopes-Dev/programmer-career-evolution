N, Q = map(int, input().split())
quantidade_problemas = list(map(int, input().split()))
prefix = []
soma_dias = []
for i in range(N):
    if i == 0:
        prefix.append(quantidade_problemas[i])
    else:
        prefix.append(quantidade_problemas[i] + prefix[i-1])

for _ in range(Q):
    s, e = map(int, input().split())
    s, e = s-1, e-1
    if s == 0:
        soma_dias.append(prefix[e])
    else:
        soma_dias.append(prefix[e] - prefix[s-1])

for _ in soma_dias:
    print(_)


[]