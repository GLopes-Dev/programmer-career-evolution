#Challenge 015 - Make a program that asks the km driven by a rental car and the number of days it was rented. Calculate the price to pay, knowing that the car costs R$60 per day
# and R$0.15 per km driven.
from utilities import rent_price

print('=' * 10, '[Challenge 015]', '=' * 10)
km = float(input('Km driven: '))
days = int(input('Days rented: '))
price = rent_price(km, days)
print('-' * 20)
print(f"You will need to pay R${price:.2f}.\n", '=' * 35)


#Learned importing functions from other files, and how to use them. Learned it from tiktok