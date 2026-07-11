import sys

def tem_ciclo(atual, conexoes, visitados):
    if atual in visitados:
        return True
    visitados.add(atual)
    
conexoes = {}
visitados = set()

N, M = map(int, sys.stdin.readline().split())
for l in range(M):
    X, Y = sys.stdin.readline().split()
    conexoes[X] = Y
servidor_inicial = sys.stdin.readline()
