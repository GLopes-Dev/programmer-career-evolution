import sys

N, K = map(int, input().split())
arquivos = list(map(int, sys.stdin.readline().split()))
maior_numero = 0
soma = 0
esquerda = 0

for direita in range(N):
    soma += arquivos[direita]
    while soma > K:
        soma -= arquivos[esquerda]
        esquerda += 1
    tamanho_atual = direita - esquerda + 1
    maior_numero = max(maior_numero, tamanho_atual)
print(maior_numero)


            
# [6, 4, 5, 2, 3, 7, 1, 2, 2, 1]
#  0  1  2  3  4  5, 6, 7, 8, 9
# soma = 18
# direita = 7
# esquerda = 2
# tamanho = 5
# maior_nmero = 5
# K = 20
#[5, 2, 3, 7, 1]
