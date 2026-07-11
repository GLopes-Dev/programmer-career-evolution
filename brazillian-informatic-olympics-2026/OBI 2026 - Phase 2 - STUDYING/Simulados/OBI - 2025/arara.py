N, M = map(int, input().split())
gaiolas_minimas = 1 + (N - 1) * 5
if M >= gaiolas_minimas:
    print('S')
else:
    print('N')
    