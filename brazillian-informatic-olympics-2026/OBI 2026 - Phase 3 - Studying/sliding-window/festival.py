import sys
from collections import defaultdict
N, K = map(int, input().split())
games = list(map(int, sys.stdin.readline().split()))
greatest_size = 0
left = 0
frequency = defaultdict(int)
for right in range(N):
    frequency[games[right]] += 1
    while len(frequency) > K:
        frequency[games[left]] -= 1
        if frequency[games[left]] == 0:
            del frequency[games[left]]
        left += 1
    current_size = right - left + 1
    greatest_size = max(greatest_size, current_size)

print(greatest_size)



# K = 2
# [1, 2, 1, 3, 4, 3, 3, 2]
#  0  1  2  3  4  5  6  7
# right = 7
# left = 5
#{2: 4, 4: 3}
# len = 3
# current_size = 3
# greatest_size = 4
# [2, 2, 4, 4, 4, 2, 2]

