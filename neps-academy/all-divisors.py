x = int(input())
divisors = []

limite = int(x ** 0.5)
for i in range(1, limite + 1):
    if x % i == 0:
        divisors.append(i)
        partner = x // i
        if partner != i:
            divisors.append(partner)

print(divisors)

divisors.sort()

print(*divisors)