N = int(input())
casas = []
for n in range(N):
    casa = int(input())
    casas.append(casa)
K = int(input())

def search(casas, K):
    left = 0
    right = len(casas) - 1
    soma = 0
    while soma != K:
        soma = casas[left] + casas[right]
        if soma == K:
            return (casas[left], casas[right])
        elif soma > K:
            right -= 1
        else:
            left += 1

resposta = search(casas, K)
print(*(resposta))
