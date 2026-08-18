N, C, S = map(int, input().split())
comandos = list(map(int, input().split()))
estacoes = [e for e in range(1, N+1)]
qtd = 0
estacao_atual = estacoes.index(1)
if estacoes[estacao_atual] == S:
    qtd += 1
for c in comandos:
    estacao_atual = estacao_atual + c
    if estacao_atual == N:
        estacao_atual = 0
    elif estacao_atual < 0:
        estacao_atual = N - 1
    if estacoes[estacao_atual] == S:
        qtd += 1
print(qtd)

# [1, 2, 3]
#  0  1  2
# atual = -1
# qtd = 2
# S
# N == 3
# C == 4
# S = 3
#[-1, -1, -1, -1]