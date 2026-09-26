buracos = [float('inf')] * (N+2)
# buracos[0] = 0

# fila = [(0, 0)]
# while fila:
#     b, p_atual = hp.heappop(fila)
#     if b > buracos[p_atual]:
#         continue
#     for p_vizinha, bp_vizinha in caminhos[p_atual]:
#         qtd_buracos_nova = b + bp_vizinha
#         if qtd_buracos_nova < buracos[p_vizinha]:
#             buracos[p_vizinha] = qtd_buracos_nova
#             hp.heappush(fila, (bp_vizinha, p_vizinha))

# print(buracos[N+1])