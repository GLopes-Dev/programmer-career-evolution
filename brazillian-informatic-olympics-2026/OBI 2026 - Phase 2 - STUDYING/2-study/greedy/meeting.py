N = int(input())
reunioes = []
qtd = 0
for a in range(N):
    a, b = map(int, input().split())
    reunioes.append((a, b))
reunioes = sorted(reunioes, key=lambda tuple: tuple[-1])
ultimo_assistido = 0
for i, f in reunioes:
    if i >= ultimo_assistido:
        qtd += 1
        ultimo_assistido = f

print(qtd)

