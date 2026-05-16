#Desafio 010 - Make a program that reads how much money in R$ reais a person has in their wallet and shows how many U$ dolars do they have. U$1,00 = R$4,98

print('=' * 10, '[Challenge 010]', '=' * 10)
rs = float(input('How much R$ you have in your wallet? '))
print('-' * 30)
print(f'You can exchange {rs:.2f}R$ Reais for {rs / 4.98:.2f}U$ Dolars.\n', '=' * 30)
