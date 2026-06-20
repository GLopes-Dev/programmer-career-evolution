#Challenge 022 - Create a program that reads a persons full name and shows:
# - The name with all uppercase letters
# - The name with all lowercase letters
# - How many letters it has (without whitespace)
# - How many letters the first name has

print("=" * 10, "[Challenge 022]", "=" * 10)
name = input("What's your name? ")
print(f"Nice to meet you, {name.split()[0].capitalize()}!")
print("=" * 10, "INFO", "=" * 10)
print(f"Your name in Uppercase letters: {name.upper()}")
print(f"Your name in Lowercase letters: {name.lower()}")
print(f"Your name has {len(name.replace(' ', ''))} letters.")
print(f"Your first name is {name.capitalize().split()[0]} and it has {len(name.split()[0])} letters.")

#Extras
print(f"Your Username: {name.lower().split()[0]}.{name.lower().split()[-1]}")
sName = name.split()
print(f"Just your first and last name for privacy reasons: {sName[0].capitalize()} *** {sName[-1].capitalize()}")
print("=" * 30)