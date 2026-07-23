N, M = map(int, input().split())
divisao = list(map(int, input().split()))
faixas = list(map(int, input().split()))
ogros = list(map(int, input().split()))
ranking = []

def achar_faixa(divisoes, forca):
    ini = 0
    fim = len(divisao) - 1
    resultado = 0
    while ini <= fim:
        meio = (ini + fim) // 2
        if divisoes[meio] <= forca:
            resultado = meio + 1
            ini = meio + 1
        else:
            fim = meio - 1

    return faixas[resultado]

for o in ogros:
    faixa = achar_faixa(divisao, o)
    ranking.append(faixa)
print(*(ranking))


#Bisect
# import bisect
# N, M = map(int, input().split())
# divisoes = list(map(int, input().split()))
# faixas = list(map(int, input().split()))
# ogros = list(map(int, input().split()))
# ranking = []
# for o in ogros:
#     idx = bisect.bisect_right(divisoes, o)
#     ranking.append(faixas[idx])
# print(ranking)