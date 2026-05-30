#Challenge 033 - Create a program that reads 3 numbers and shows which one is the largest and which one is the smallest.


#Nested IFs version

print("=" * 10, "[Challenge 033]", "=" * 10)
n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
print("=" * 30)

if (n1 == n2) and (n1 == n3):
    print("The numbers are equals.")
elif n1 > n2 and n1 > n3:
    largest_number = n1
    print(f"Largest number: {n1}")
elif n2 > n1 and n2 > n3:
    largest_number = n2
    print(f"Largest number: {n2}")
elif n3 > n1 and n3 > n2:
    largest_number = n3
    print(f"Largest number: {n3}")

if n1 < n2 and n1 < n3:
    smallest_number = n1
    print(f"Smallest number: {n1}")
elif n2 < n1 and n2 < n3:
    smallest_number = n2
    print(f"Smallest number: {n2}")
elif n3 < n1 and n3 < n2:
    smallest_number = n3
    print(f"Smallest number: {n3}")
print("=" * 30)


#Fast Version (Trick)

print("=" * 10, "[Challenge 033]", "=" * 10)
numbers = []
largest_num = 0
smallest_num = 999999999999999999
for i in range (3):
    num = int(input(f"{i+1}° Number: "))
    numbers.append(num)
    if num > largest_num:
        largest_num = num
    if num < smallest_num:
        smallest_num = num
print("=" * 30)
print(numbers)
print(f"Largest number: {largest_num}\nSmallest number: {smallest_num}\n", "=" * 30)



#Fast Version v2
print("=" * 10, "[Challenge 033]", "=" * 10)
numbers = []
for i in range (3):
    num = int(input(f"{i+1}° Number: "))
    numbers.append(num)
largest_num = max(numbers)
smallest_num = min(numbers)
print("=" * 30)
print(numbers)
print(f"Largest number: {largest_num}\nSmallest number: {smallest_num}\n", "=" * 30)