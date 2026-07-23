

V = int(input())
moedas = [100, 50, 25, 10, 1]
total_moedas = 0
for moeda in moedas:
    total_moedas += V // moeda
    V = V % moeda
print(total_moedas)


2
