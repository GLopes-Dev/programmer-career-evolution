A = int(input())
S = int(input())
D = int(input())
dias = 0
total = 0
while True:
    dias += 1
    total += S
    if total >= A:
        break
    total -= D

print(dias)
