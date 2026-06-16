P1, C1, P2, C2 = map(int, input().split())
left_side = P1 * C1
right_side = P2 * C2

if left_side == right_side:
    print(0)
elif left_side > right_side:
    print(-1)
else:
    print(1)