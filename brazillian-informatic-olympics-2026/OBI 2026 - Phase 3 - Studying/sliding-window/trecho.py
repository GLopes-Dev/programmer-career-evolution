import sys

N = int(input())
numeros = list(map(int, sys.stdin.readline().split()))
maior_comprimento = 0
esquerda = 0
sequencia = set()

for direita in range(N):
    while numeros[direita] in sequencia:
        sequencia.remove(numeros[esquerda])
        esquerda += 1
    sequencia.add(numeros[direita])
    tamanho_atual = direita - esquerda + 1
    maior_comprimento = max(maior_comprimento, tamanho_atual)
print(maior_comprimento)


# [1, 2, 3, 2, 4, 5, 3, 6]

#  0, 1, 2, 3, 4, 5, 6, 7
# direita = 7
# esquerda = 3
# tamanho_atual = 5
# maior_comprimento = 5
# sequencia = [2, 4, 5, 3, 6]
# sequencia_lista = []