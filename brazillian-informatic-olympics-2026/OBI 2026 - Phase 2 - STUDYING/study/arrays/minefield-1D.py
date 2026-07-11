

#Simplified (Answer)
N = int(input())
NI = list(map(int, input().split()))
res = []
for m in range(N):
    soma_casa = NI[m]
    if m - 1 >= 0:
        soma_casa += NI[m - 1]
    
    if m + 1 < N:
        soma_casa += NI[m + 1]
    
    res.append(soma_casa)
print(*res)

#My Code
N = int(input())
NI = list(map(int, input().split()))
res = []
sm = 0
for m in range(N):
    if N == 1:
        res.append(NI[m])
    else:
        if m == 0:
            sm = NI[m] + NI[m+1]
            res.append(sm)
        elif m == (N-1):
            sm = NI[m] + NI[m-1]
            res.append(sm)
        else:
            sm = NI[m] + NI[m-1] + NI[m+1]
            res.append(sm)
print(*res)