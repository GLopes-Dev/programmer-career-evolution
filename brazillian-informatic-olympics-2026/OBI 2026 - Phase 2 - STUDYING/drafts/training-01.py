'''a, b, c = map(int, input().split())
print(a, b, c)
print(a)
print(b)
print(c)'''


#Little Challenge - 01
# 1 - Abertas
# 0 - Fechadas



P, R = map(int, input().split())

if P == 0:
    print('C')
elif P == 1:
    if R == 0:
        print('B')
    else:
        print('A')
