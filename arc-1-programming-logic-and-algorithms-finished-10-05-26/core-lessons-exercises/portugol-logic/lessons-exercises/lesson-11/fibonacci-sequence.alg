algoritmo"fibonacci"
var
    count, a, b, c,: inteiro
inicio
    a <- 0
    b <- 1
    escreva(a)
    escreva(b)
    para count := 3 ate 15 faca
        c <- a + b
        escreva(c)
        a <- b
        b <- c
    fimpara

fimalgoritmo