# grafo = {
#     'Ana': ['Pedro'],
#     'Pedro': ['Ana', 'Maria'],
#     'Maria': ['Pedro', 'Joao'],
#     'Joao': ['Maria']
# }

# visitados = set()

# def dfs(atual):
#     visitados.add(atual)
#     print(f'Estou visitando: {atual}')

#     for vizinho in grafo[atual]:
#         if vizinho not in visitados:
#             dfs(vizinho)

# dfs('Pedro')

cities = {
    'Saquarema': ['Rio de Janeiro', 'Niteroi'],
    'Rio de Janeiro': ['Saquarema', 'Cabo Frio'],
    'Niteroi': ['Saquarema'],
    'Cabo Frio': ['Rio de Janeiro']
}

print(f'Saquarema neighbours: {', '.join(cities["Saquarema"])}')