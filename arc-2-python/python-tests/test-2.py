nums = []
totE = 0
totO = 0
result = 0

for i in range(10):
    n = int(input(f'Type the {i+1} number: '))
    nums.append(n)

for i in range(9):
    for j in range(i+1, 10):
        if nums[i] > nums[j]:
            aux = nums[i]
            nums[i] = nums[j]
            nums[j] = aux

for i in range(10):
    if nums[i] % 2 == 0:
        totE = totE + 1
    else:
        totO = totO + 1
    
    result = result + nums[i]

print(f"The numbers order is\n {nums}")
print(f"Total Even numbers {totE}\n", f"Total Odd numbers {totO}")
print