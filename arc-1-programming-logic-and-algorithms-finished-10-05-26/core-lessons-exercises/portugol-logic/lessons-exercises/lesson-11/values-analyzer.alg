algoritmo "Values Analyzer"
var
    count, n, sum, div5, null, pSum: inteiro
    med: real
inicio
    sum <- 0
    para count <- 1 ate 5 faca
        escreva("Type the ", count, "th number: ")
        leia(n)
        sum <- sum + n
        se (n%5 = 0) entao
            div5 <- div5 + 1
        fimse
        se (n = 0) entao
            null <- null + 1
        fimse
        se (n%2 = 0) entao
            pSum <- pSum + n
        fimse
    fimpara
    med <- sum / 5
    escreval("The sum between the values is: ", sum)
    escreval("The medium between the values is: ", med)
    escreval("Values that divisible by 5: ", div5)
    escreval("Null numbers: ", null)
    escreval("The sum between the pair numbers is: ", pSum)
fimalgoritmo