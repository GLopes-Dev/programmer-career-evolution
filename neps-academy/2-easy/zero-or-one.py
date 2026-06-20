A, B, C = map(int, input().split())
if A != B == C:
    print('A')
elif B != A == C:
    print('B')
elif C != A == B:
    print('C')
else:
    print('*')