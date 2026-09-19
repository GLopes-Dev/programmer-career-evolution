N = int(input())
vetor = []
prefix = []
for i in range(N):
    valor = int(input())
    vetor.append(valor)
    if 0 <= i-1:
        prefix.append(valor + prefix[i-1])
    else:
        prefix.append(valor)

print(prefix)