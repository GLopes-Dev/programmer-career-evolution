import sys
N = int(input())
nums = list(map(int, sys.stdin.read().split()))
nums1 = []
for n in nums:
    if n == 0:
        nums1.pop()
        continue
    nums1.append(n)

print(sum(nums1))
