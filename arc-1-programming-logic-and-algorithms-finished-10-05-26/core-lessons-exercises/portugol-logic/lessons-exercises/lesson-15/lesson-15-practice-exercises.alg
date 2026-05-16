algoritmo "Matriz3x2"
var
    mat: vetor [1..3, 1..2] de inteiro
    l, c: inteiro
inicio
    para l <- 1 ate 3 faca
        para c <- 1 ate 2 faca
            leia(mat[l, c])
        fimpara
    fimpara

    para l <- 1 ate 3 faca
        para c <- 1 ate 2 faca
            escreva(mat[l, c])
        fimpara
        escreva("")
    fimpara
fimalgoritmo










algoritmo "Matriz3x3Even"
var
    mat: vetor[1..3, 1..3] de inteiro
    even: vetor[1..9] de inteiro
    l, c, totEven, i: inteiro
inicio
    para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
            escreva("Type the position [", l, ", ", c, "] value: ")
            leia(mat[l, c])
            se (mat[l, c]%2=0) entao
                totEven <- totEven + 1
                even[totEven] <- mat[l, c]
            fimse
        fimpara
    fimpara

    para l <- 1 ate 3 faca
        para c <- 1 ate 3 faca
            escreva("[", mat[l, c], "]")
        fimpara
        escreval()
    fimpara
    escreval("-----------------")
    escreval("Even Numbers: ")
    para i <- 1 ate totEven faca
        escreva("[", even[i], "]")
    fimpara
    escreval()
    escreval("Total EVEN numbers: ", totEven)
fimalgoritmo








algoritmo "MatrizID"
var
    mID: vetor[1..4, 1..4] de inteiro
    l, c: inteiro
inicio
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            se (l = c) entao
                mID[l, c] <- 1
            senao
                mID[l, c] <- 0
            fimse
        fimpara
    fimpara

    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            escreva("[", mID[l, c], "]")
        fimpara
        escreval()
    fimpara
fimalgoritmo
















algoritmo "preencherMatriz4ordem"
var
    m: vetor[1..4, 1..4] de inteiro
    l, c, sDP, produto, maior3C: inteiro
    SM, med: real
inicio
    produto <- 1
    sDP <- 0
    maior3C <- 0
    med <- 0
    SM <- 0
    //Preencher
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            escreva("Digite o valor da posição [", l, ", ", c, "]: ")
            leia(m[l, c])
            se (l = c) entao
               sDP <- sDP + m[l, c]
            fimse
        fimpara
    fimpara
    //Produto
    para c <- 1 ate 4 faca
        produto <- produto * m[2, c]
    fimpara
    //Maior 3 Linha
    para l <- 1 ate 4 faca
        se (m[l, 3] > maior3C) entao
            maior3C <- m[l, 3]
        fimse
    fimpara
    escreval("MATRIZ")
    escreval("-----------------")
    para l <- 1 ate 4 faca
        para c <- 1 ate 4 faca
            escreva(m[l, c]:5)
            SM <- SM + m[l, c]
        fimpara
        escreval()
    fimpara
    med <- SM / 16
    escreval("A soma dos valores da DIAGONAL PRINCIPAL é: ", sDP)
    escreval("O produto entre os valores da SEGUNDA LINHA é: ", produto)
    escreval("O maior valor da TERCEIRA LINHA é: ", maior3C)
    escreval("A média entre TODOS os valores da MATRIZ é: ", med)
fimalgoritmo



















algoritmo ""
var

inicio

fimalgoritmo