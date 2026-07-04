P, T = map(int, input().split())
altitude = [0] + list(map(int, input().split()))
caminhos = {}
for p in range(1, P+1):
    caminhos[p] = []
for p in range(T):
    I, J = map(int, input().split())
    caminhos[I].append(J)
    caminhos[J].append(I)
start = int(input())
visitados = set()

def rotas(atual, caminhos, altura, visitados):
    if atual in visitados:
        return 0
    maximo_daqui = 0
    visitados.add(atual)

    for rota in caminhos[atual]:
        if altura[rota] < altura[atual]:
            maximo_da_proxima = 1 + rotas(rota, caminhos, altura, visitados)
            if maximo_da_proxima > maximo_daqui:
                maximo_daqui = maximo_da_proxima

    visitados.remove(atual)
    return maximo_daqui

    

print(rotas(start, caminhos, altitude, visitados))
