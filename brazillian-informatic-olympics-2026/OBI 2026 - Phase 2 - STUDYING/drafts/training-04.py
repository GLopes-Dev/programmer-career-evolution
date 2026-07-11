C = int(input())
A = int(input())
vagas_reais = C - 1
viagens_cheias = A // vagas_reais
if A % vagas_reais > 0:
    viagens_cheias += 1
print(viagens_cheias)