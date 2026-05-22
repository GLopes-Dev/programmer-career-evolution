#Challenge 023 - Make a program that reads a number between 0 and 9999 and display in the screen each one of the digits separated
#Ex:
# Type a nuber: 1834
# Unit: 4
# Ten: 3
# Hundred: 8
# Thousands: 1

print("=" * 10, "[Challenge 023]", "=" * 10)
num = input('Type a number between 0 and 9999: ')
print("=" * 10, "[INFO]", "=" * 10)
print(f"Unit: {num[-1]}\nTen: {num[2]}\nHundred: {num[1]}\nThousands: {num[0]}\n", "=" * 30)


#Math Version

print("=" * 10, "[Challenge 023]", "=" * 10)
num = input('Type a number between 0 and 9999: ')
print("=" * 10, "[INFO]", "=" * 10)
num = int(num)
print(f"Unit: {num % 10}\nTen: {(num // 10) % 10}\nHundred: {(num // 100) % 10}\nThousands: {(num // 1000) % 10}\n", "=" * 30)