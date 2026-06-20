#Challenge 034 - Create a program that asks for an employee's salary and calculates their increase
#For salaries higher than R$1.250,00, calculate a 10% increase.
#For values less than or equal to, calculate a 15% increase.

print("=" * 10,"[Challenge 034]", "=" * 10 )
salary = float(input("Your salary: R$"))
if salary > 1250:
    increase = 0.10 * salary
    new_salary = salary + increase
else:
    increase = 0.15 * salary
    new_salary = salary + increase
print("=" * 10, f"\nYour new salary is R${new_salary:.2f}")
print("=" * 30)