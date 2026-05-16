algoritmo "var"
var
    vet: vetor[0..9] de inteiro
    i, c: inteiro
inicio
    c <- 5
    para i <- 0 ate 9 faca
        vet[i] <- c
        c <- c + 5
    fimpara

    para i <- 0 ate 9 faca
        escreva("[", vet[i], "] ")
    fimpara
fimalgoritmo



algoritmo "var"
var
    vet: vetor[1..10] de inteiro
    i: inteiro
inicio
    para i <- 1 ate 10 faca
        escreva("Type the ", i, " number: ")
        leia(vet[i])
    fimpara


    escreval("EVEN LIST")
    escreval("=============")
    escreval("POS      NUM ")
    para i <- 1 ate 10 faca
        se (vet[i]%2=0) entao
            escreval(i, vet[i]:10)
        fimse
    fimpara
    escreval("=============")
fimalgoritmo


algoritmo "Ordenação"
var
    vet: vetor[1..20] de inteiro
    i, j, aux: inteiro
inicio
    para i <- 1 ate 20 faca
        vet[i] <- RandI(100)
    fimpara

    escreval("TYPED NUMBERS")
    escreval("=============")
    para i <- 1 ate 20 faca
        escreval("[", vet[i], "] ")
    fimpara
    escreval("=============")

    para i <- 1 ate 19 faca
        para j <- i+1 ate 20 faca
            se (vet[i] > vet[j]) entao
                aux <- vet[i]
                vet[i] <- vet[j]
                vet[j] <- aux
            fimse
        fimpara
    fimpara

    escreval("ORDERED NUMBERS")
    escreval("===============")
    para i <- 1 ate 20 faca
        escreval("[", vet[i], "] ")
    fimpara
fimalgoritmo