#Challenge 030 - Create a program that reads a integer number and displays on the screen if it is EVEN or ODD.
#

print("=" * 10, "[Challenge 030]", "=" * 10)
num = int(input('Type any number: '))
if num % 2 == 0:
    print(f"The number {num} is EVEN")
else:
    print(f"The number {num} is ODD")