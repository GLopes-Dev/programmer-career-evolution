# caminhos = {
#     'Mercado': ['Padaria'],
#     'Escola': ['Tribunal', 'Prefeitura'],
#     'Prefeitura': ['Confeitaria'],
#     'Academia': ['Prefeitura', 'Confeitaria'],
#     'Padaria': ['Escola'],
#     'Tribunal': ['Padaria', 'Mercado'],
#     'Confeitaria': ['Tribunal', 'Academia']
# }


# def dfs(atual, destino, caminhos, visitados):
#     if atual == destino:
#         return True
#     if atual in visitados:
#         return False
    
#     visitados.add(atual)

#     for vizinho in caminhos[atual]:
#         if dfs(vizinho, destino, caminhos, visitados) == True:
#             return True
#     return False

# resultado = dfs('Mercado', 'Academia', caminhos, set())
# print(resultado)




caminhos = {
    'Mercado': ['Padaria'],
    'Escola': ['Tribunal', 'Prefeitura'],
    'Prefeitura': ['Confeitaria'],
    'Academia': ['Prefeitura', 'Confeitaria'],
    'Padaria': ['Escola'],
    'Tribunal': ['Padaria', 'Mercado'],
    'Confeitaria': ['Tribunal', 'Academia']
}


def dfs(atual, caminhos, visitados):
    if atual in visitados:
        return
    visitados.add(atual)
    for vizinho in caminhos[atual]:
        dfs(vizinho, caminhos, visitados)

visitados_set = set()
dfs('Mercado', caminhos, visitados_set)
print(len(visitados_set))
