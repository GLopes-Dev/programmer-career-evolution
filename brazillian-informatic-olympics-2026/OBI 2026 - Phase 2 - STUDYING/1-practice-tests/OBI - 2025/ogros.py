
import sys
N, M = map(int, sys.stdin.readline().split())
divisoes = list(map(int, sys.stdin.readline().split()))
premios = list(map(int, sys.stdin.readline().split()))
ogros = list(map(int, sys.stdin.readline()).split())

def acha_faixa(divisoes, forca):
    ini = 0
    fim = len(divisoes) - 1
    resposta = -1

    while ini <= fim:
        meio = (ini + fim) // 2
        if divisoes[meio] <= forca:
            resposta = meio
            ini = meio + 1
        else:
            fim = meio - 1
        return resposta + 1
    
resultados = []
for o in ogros:
    posicao_premio = acha_faixa(divisoes, o)
    resultados.append(premios[posicao_premio])
print(*(resultados))

