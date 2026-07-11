dados_amigos = {}
dados_amigos[1] = 3
dados_amigos[2] = 9
print(dados_amigos)
dados_amigos[2] = dados_amigos[2] + 1
print(dados_amigos)
mensagens = dados_amigos.get(3, 2)
print(mensagens)
print(10 in dados_amigos)