import sys
input = sys.stdin.readline()

def busca_binaria(lista, alvo):
    ini = 0
    fim = len(lista) - 1
    
    while ini <= fim:
        meio = (ini + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            ini = meio + 1
        else:
            fim = meio - 1
    return -1

numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("Posição do 23:", busca_binaria(numeros, 23))
print("Posicao do 50: ", busca_binaria(numeros, 50))

      