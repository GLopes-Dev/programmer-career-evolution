#Challenge 044 - Make a program that calculates the price to be paid for a product, considering its regular price and payment methods:
# - In full money/check: 10% discount
# - Card in full: 5% discount
# - Up to 2x on card: regular price
# - 3x or higher on card: 20% fees.

print('=' * 10, '[Challenge 044]', '=' * 10)
print('=' * 10, ' Biel Dev Store ', '=' * 10)
price = float(input('Purchase Price: R$'))
print('''PAYMENT METHODS 
[ 1 ] In full MONEY/CHECK
[ 2 ] In full on card
[ 3 ] 2x on card
[ 4 ] 3x or more on card''')
option = int(input('Your option: '))
match option:
    case 1:
        discount = price - (price * 0.10)
        print(f'Your purchase of R${price:.2f} will cost R${discount:.2f} in the end.')
    case 2:
        discount = price - (price * 0.05)
        print(f'Your purchase of R${price:.2f} will cost R${discount:.2f} in the end.')
    case 3:
        installments = price / 2
        print(f'Your purchase will be split into 2 installments of R${installments}.')
        print(f'Your purchase of R${price:.2f} will cost R${price:.2f} in the end.')
    case 4:
        installments_qty = int(input('How many installments? '))
        price_fees = price + (price * 0.20)
        installments = price_fees / installments_qty
        print(f'Your purchase will be split into {installments_qty} installments of R${installments:.2f} with INTEREST.')
        print(f'Your purchase of R${price:.2f} will cost R${price_fees:.2f} in the end. ')