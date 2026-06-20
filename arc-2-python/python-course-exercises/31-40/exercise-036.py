#Challenge 036 - Create a program to approve a bank loans for the purchase of a house. Ask for the house value, the buyer's salary 
#and the number of years they will take to repay the loan. The monthly payment cannot exceed 30% of the salary, otherwise the loan will be denied.

print('=' * 10, '[Challenge 036]', '=' * 10)
#Input
house_value = float(input("House's Value: "))
buyers_salary = float(input("Buyer's Salary: "))
years = int(input('How many years of financing? '))

#Operations
monthly_payment = house_value / (years * 12)
salary_30 = buyers_salary * 0.30

print(f'To pay for a house costing R${house_value:.2f} in {years} {"year" if years == 1 else "years"}', end='')
print(f' the monthly payment will be R${monthly_payment:.2f}')
if monthly_payment > salary_30:
    print('Loan DENIED.')
else:
    print('The loan can be GRANTED!')