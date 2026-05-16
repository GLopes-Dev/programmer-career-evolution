#Desafio 012 - Make an algoritm that reads a product price and shows its new price, with 5% discount\
from utilities import discount
print('=' * 10, '[Challenge 012]', '=' * 10)
disc = int(input('Discount: '))
value = float(input('Product price: '))
final = discount(value, disc)
print('-' * 35)
print(f'New price: {final:.2f}')
