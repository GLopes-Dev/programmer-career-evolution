N = int(input())
sum = 0
days = 0
for i in range(N):
    acess = int(input())
    if sum < 1000000:
        sum += acess
        days += 1

print(days)