V = int(input())
moedas = [25, 10, 5, 1]
qtd_moedas = 0
for moeda in moedas:
    qtd_moeda_atual = V // moeda
    V -= qtd_moeda_atual * moeda
    qtd_moedas += qtd_moeda_atual

print(qtd_moedas)