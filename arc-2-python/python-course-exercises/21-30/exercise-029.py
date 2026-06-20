#Challenge 029 - Create a program that reads a car velocity. If it exceeds 80Km/h, display a message saying that he was fined.
# The fine costs R$7,00 for each Km above the limit

print("=" * 10, "[Challenge 029]", "=" * 10)
vel = float(input("Car Velocity: "))
if vel > 80:
    abvl = vel - 80
    fine = abvl * 7
    print(f"You got fined.\nPrice: {fine:.2f}")
else:
    print("Safe.")
print("=" * 30)