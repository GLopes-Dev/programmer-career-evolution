N = int(input())
competidores = {}
for c in range(N):
    competidor, ponto = input().split()
    ponto = int(ponto)
    competidores[competidor] = ponto

ranking = sorted(competidores.items(), key=lambda comp: (-comp[1], comp[0]))
for c, p in ranking:
    print(f"{c}: {p}")

  #  competidor = 'Bob'
  #  ponto = 300
  #  {'Pedro': 150, 'Ana': 300, 'Maria': 150, 'Bob': 300}
  #  [('Pedro', 150), ('Ana', 300), ('Maria', 150), ('Bob', 300)]
  #
  #
  #
  #
  #
  #
  #