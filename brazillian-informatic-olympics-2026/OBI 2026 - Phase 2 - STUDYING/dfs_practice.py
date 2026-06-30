rotas = {
    'Castelo_Saquarema': ['Vila_Oeste', 'Fortaleza_Norte'],
    'Vila_Oeste': ['Santuario_Oculto'],
    'Fortaleza_Norte': ['Castelo_Imperial'],
    'Santuario_Oculto': ['Castelo_Imperial'],
    'Castelo_Imperial': [] # Beco sem saída
}

visitados = set()

def tem_rota_secreta(local_atual, destino, mapas):
    if local_atual == destino:
        return True
    if local_atual in visitados:
        return False
    
    visitados.add(local_atual)

    for vizinho in mapas[local_atual]:
        if tem_rota_secreta(vizinho, destino, mapas) == True:
            return True
    return False

resultado = tem_rota_secreta('Castelo_Saquarema', 'Castelo_Imperial', rotas)
print(f"O espião consegue chegar? {resultado}")
