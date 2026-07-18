N, M = map(int, input().split())
corte = list(map(int, input().split()))
faixas = list(map(int, input().split()))
ogros = list(map(int, input().split()))
resultados = []
def acha_faixa(corte, forca):
    ini = 0
    fim = len(corte) - 1
    resultado = -1
    while ini <= fim:
        meio = (ini + fim) // 2
        if corte[meio] <= forca:
           resultado = meio
           ini = meio + 1
        else:
           fim = meio - 1
        return resultado + 1
        
for o in ogros:
    faixa = acha_faixa(corte, o)
    resultados.append(faixas[faixa])
print(*(resultados))


