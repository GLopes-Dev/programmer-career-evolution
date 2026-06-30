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

# cities = {
#     'Saquarema': ['Rio de Janeiro', 'Niteroi'],
#     'Rio de Janeiro': ['Saquarema', 'Cabo Frio'],
#     'Niteroi': ['Saquarema'],
#     'Cabo Frio': ['Rio de Janeiro']
# }

# print(f'Saquarema neighbours: {', '.join(cities["Saquarema"])}')


# connections = {
#     'Biel': ['MEXT_Monbukagakusho', 'Cla_Roblox'],
#     'Cla_Roblox': ['Biel'],
#     'MEXT_Monbukagakusho': []
# }

connections = {
    'Biel': ['MEXT_Monbukagakusho', 'Cla_Roblox'],
    'Cla_Roblox': ['Biel'],
    'MEXT_Monbukagakusho': [],
    'Guanabara': ['Biel']
}

visitados = set()

def dfs(no_atual, grafo):
    if no_atual in visitados:
        return
    
    print(f"Visitando: {no_atual}")
    visitados.add(no_atual)

    for vizinhos in grafo[no_atual]:
        dfs(vizinhos, grafo)

print("--- Starting DFS ---")
dfs('Guanabara', connections)