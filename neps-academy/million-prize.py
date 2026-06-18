N = int(input())
sum = 0
days = 0
for i in range(N):
    acess = int(input())
    sum += acess
    days += 1
    if sum >= 1000000:
        StopIteration
print(days)
