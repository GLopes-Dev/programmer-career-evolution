import sys
from bisect import bisect_left

def main():
    N = int(sys.stdin.buffer.readline())
    M = int(sys.stdin.buffer.readline())
    turnos = []

    for _ in range(M):
        t_atual = int(sys.stdin.buffer.readline())
        turnos.append(t_atual)
        removidos = N // t_atual
        N -= removidos

    posicoes = [n for n in range(1, min(N, 10000) + 1)]
    total_posicoes = len(posicoes)
    for turno in reversed(turnos):
            inicio = bisect_left(posicoes, turno)
            if inicio == total_posicoes:
                continue
            d = turno - 1
            for i in range(inicio, total_posicoes):
                p = posicoes[i]
                posicoes[i] = p + (p - 1) // d

    sys.stdout.write("\n".join(map(str, posicoes)))

if __name__ == "__main__":
     main()    
        



#Tenebrous






    ## Pq total dividido por turno da exatamente a qtd de removidos?
