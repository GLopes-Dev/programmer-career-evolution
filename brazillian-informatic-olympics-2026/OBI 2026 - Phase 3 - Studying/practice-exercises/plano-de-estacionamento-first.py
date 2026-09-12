import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
plano = []
preenchidas = set()
maior_qtd = 0

def buscar(vagas):
    left = 1
    right = vagas
    answer = -1
    while left <= right:
        middle = (left + right) // 2
        if middle not in preenchidas:
            answer = middle
            left = middle + 1
        else:
            left = middle + 1
    return answer

        
            
for _ in range(M):
    numero = int(sys.stdin.readline())
    plano.append(numero)

for intervalo in plano:
    maior_vaga_disponivel = buscar(intervalo)
    if maior_vaga_disponivel == -1:
        break
    else:
        maior_qtd += 1
        preenchidas.add(maior_vaga_disponivel)

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
