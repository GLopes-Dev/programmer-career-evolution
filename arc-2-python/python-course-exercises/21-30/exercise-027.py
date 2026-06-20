#Challenge 027 - Make a program that reads a person full name, displaying the first and last name right away, separated.
#Ex: Gabriel de Sousa Ferreira Lopes
#First name = Gabriel
#Last Name = Lopes

print("=" * 10, "[Challenge 027]", "=" * 10)
name = str(input("Type your full name: "))
name = name.split()
print(f"Nice to meet you, {name[0].capitalize()}!").strip()
print(f"First name: {name[0].capitalize()}\nLast name: {name[-1].capitalize()}")
print("=" * 30)
