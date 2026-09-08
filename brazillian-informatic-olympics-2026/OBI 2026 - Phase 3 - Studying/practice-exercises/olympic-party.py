N = int(input())
M = int(input())
turnos = []
suditos_final = []

for _ in range(M):
    t_atual = int(input())
    turnos.append(t_atual)
    removidos = N // t_atual
    N = N - removidos

for p in range(1, min(N, 10000) + 1):
    for turno in reversed(turnos):
        p = p + (p - 1) // (turno - 1)
    suditos_final.append(p)

for sudito in suditos_final:
    print(sudito)













    ## Pq total dividido por turno da exatamente a qtd de removidos?
