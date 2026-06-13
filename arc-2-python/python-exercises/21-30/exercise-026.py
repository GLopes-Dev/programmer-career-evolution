#Challenge 025 - Make a program that reads a phrase and displays:
# How many times the letter "A" appears
# What position it appears for the first time
# What position it appears for the last time

print("=" * 10, "[Chalenge 026]", "=" * 10)
text = str(input("Type anything: ").strip())
print(f"The letter A appears {text.upper().count('A')} times.")
print(f"The letter A appears for the first time in position {text.upper().find('A')+1}")
print(f"The letter A appears for last time in position {text.upper().rfind('A')+1}")
