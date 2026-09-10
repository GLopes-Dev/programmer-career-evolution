N = int(input())
prices = list(map(int, input().split()))
K = int(input())
left = 0
sum = 0
max_items = 0

for right in range(N):
     sum += prices[right]
     while sum > K:
           sum -= prices[left]
           left += 1
     actual_items_amount = right - left + 1
     max_items = max(actual_items_amount, max_items)

print(max_items)