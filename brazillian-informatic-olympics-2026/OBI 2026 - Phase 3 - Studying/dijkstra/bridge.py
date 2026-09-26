import heapq as hp
N, M = map(int, input().split())
caminhos = [[] for _ in range(N+2)]

for _ in range(M):
    S, T, B = map(int, input().split())
    caminhos[S].append((T, B))
    caminhos[T].append((S, B))

buracos = [float('inf')] * (N+2)
buracos[0] = 0

fila = [(0, 0)]
while fila:
    b, p_atual = hp.heappop(fila)
    if b > buracos[p_atual]:
        continue
    for p_vizinha, bp_vizinha in caminhos[p_atual]:
        qtd_buracos_nova = b + bp_vizinha
        if qtd_buracos_nova < buracos[p_vizinha]:
            buracos[p_vizinha] = qtd_buracos_nova
            hp.heappush(fila, (qtd_buracos_nova, p_vizinha))

print(buracos[N+1])