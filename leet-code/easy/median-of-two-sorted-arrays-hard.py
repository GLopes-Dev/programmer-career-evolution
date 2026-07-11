nums = [0, 3, 1, 9]
nums2 = [2, 8, 7, 9]
l = nums + nums2
aSum = 0
for i in range(len(l)):
    aSum = aSum + l[i]
med = aSum / len(l)
print(len(l))
print(f"Arrays average: {med}")