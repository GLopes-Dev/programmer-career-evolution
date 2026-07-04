C, T = map(int, input().split())
alturas = [0] + list(map(int, input().split()))
caminhos = {}
for n in range(1, C+1):
    caminhos[n] = []

for n in range(T):
    I, J = map(int, input().split())
    caminhos[I].append(J)
    caminhos[J].append(I)

P = int(input())
visitados = set()
total = 0
def route(atual, caminhos, alturas, visitados):
    if atual in visitados:
        return 0
    visitados.add(atual)
    maior_caminho_daqui = 0

    for caminho in caminhos[atual]:
        if alturas[caminho] < alturas[atual]:
            caminho_desse_vizinho = 1 + route(caminho, caminhos, alturas, visitados)
            if caminho_desse_vizinho > maior_caminho_daqui:
                maior_caminho_daqui = caminho_desse_vizinho

    visitados.remove(atual)
    return maior_caminho_daqui

total = route(P, caminhos, alturas, visitados)
print(total)