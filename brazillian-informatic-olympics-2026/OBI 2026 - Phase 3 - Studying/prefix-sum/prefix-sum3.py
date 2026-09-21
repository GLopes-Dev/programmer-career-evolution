N = int(input())
conexoes = list(map(int, input().split()))
prefix = []
L = int(input())
R = int(input())

for i in range(N):
    if i == 0:
        prefix.append(conexoes[i])
    else:
        prefix.append(conexoes[i] + prefix[i-1])

if L == 0:
    soma = prefix[R]
else:
    soma = prefix[R] - prefix[L-1]


print(conexoes)
print(prefix)
print(soma)