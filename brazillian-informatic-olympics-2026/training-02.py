#Little Challenge - 02
#Vitoria = 3 pontos | Empate = 1 ponto | Derrota = 0 pontos
#

Cv, Ce, Cs, Fv, Fe, Fs = map(int, input().split())
Cp = (Cv * 3) + Ce 
Fp = (Fv * 3) + Fe

if Cp > Fp:
    print('C')
elif Fp > Cp:
    print('F')
else:
    if Cs > Fs:
        print('C')
    elif Fs > Cs:
        print('F')
    else:
        print('=')