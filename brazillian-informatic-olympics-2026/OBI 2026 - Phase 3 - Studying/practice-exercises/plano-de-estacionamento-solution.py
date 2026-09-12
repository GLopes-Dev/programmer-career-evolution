import sys
sys.setrecursionlimit(200000)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
plano = []
maior_qtd = 0
parent = [_ for _ in range(N + 1)]

def buscar(x):
    if parent[x] == x:
        return x

    parent[x] = buscar(parent[x])
    return parent[x]

        
            
for _ in range(M):
    numero = int(sys.stdin.readline())
    plano.append(numero)

for intervalo in plano:
    maior_vaga_disponivel = buscar(intervalo)
    if maior_vaga_disponivel == 0:
        break
    else:
        maior_qtd += 1
        parent[maior_vaga_disponivel] = buscar(maior_vaga_disponivel - 1)

print(maior_qtd)


# left = 1
# right = 1
# middle = 1
# answer = 1

# vagas = 3
# numero = 3

# maior_vaga_livre = 0
# maior_qtd = 1

# plano = [3, 3, 3]
# intervalo = 3
# preenchidas = {3, 2}
