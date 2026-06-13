#Challenge 025 - Create a program that reads a person name and says if it has "SILVA" in their name

print("=" * 10, "[Challenge 025]", "=" * 10)
name = input("Type your full name: ")
if 'SILVA' in name.upper().split():
    print("Has Silva? Yes")
else:
    print("Has Silva? No")