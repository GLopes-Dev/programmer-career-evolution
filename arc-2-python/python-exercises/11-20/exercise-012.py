#Desafio 012 - Make an algoritm that reads a product price and shows its new price, with 5% discount\
from utilities import discount
print('=' * 10, '[Challenge 012]', '=' * 10)
disc = int(input('Discount: '))
value = float(input('Product price: '))
final = discount(value, disc)
print('-' * 35)
print(f'New price: {final:.2f}')



#Learned importing functions from other files, and how to use them. In this case, the function 'discount' is imported from the 'utilities' file"
# and it calculates the new price after applying the discount.

#Learned it from TikTok