A, B = map(float, input().split())
avg = (A + B) / 2

if avg >= 7:
    print('Aprovado')
elif 4 <= avg < 7:
    print('Recuperacao')
else:
    print('Reprovado')