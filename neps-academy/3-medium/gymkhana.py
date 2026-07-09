
import math
N, M = map(int, input().split())
X = M
gdc = math.gcd(N, X)
while gdc != 1:
    X -= 1
    gdc = math.gcd(N, X)
print(X)