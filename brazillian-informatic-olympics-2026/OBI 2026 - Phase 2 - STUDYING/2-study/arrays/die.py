dados = [3, 4, 1, 4, 3, 6, 5, 4, 3, 1]
maior_frequencia = 0
numero_vencedor = 0
for n in range(1, 7):
    qtd = dados.count(n)
    if qtd >= maior_frequencia:
        maior_frequencia = qtd
        numero_vencedor = n
print(numero_vencedor)