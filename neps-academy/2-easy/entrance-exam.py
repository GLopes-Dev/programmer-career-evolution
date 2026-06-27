N = int(input())
T = input()
R = input()
hits = 0
for gab, ans in zip(T, R):
    if gab == ans:
        hits += 1
print(hits)
