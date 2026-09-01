import sys
N, K = map(int, input().split())
treinos = list(map(int, sys.stdin.readline().split()))
maior_sequencia = 0
soma = 0
esquerda = 0
for direita in range(N):
    soma += treinos[direita]
    while soma > K:
        soma -= treinos[esquerda]
        esquerda += 1
    tamanho_atual = direita - esquerda + 1
    maior_sequencia = max(maior_sequencia, tamanho_atual)
print(maior_sequencia)