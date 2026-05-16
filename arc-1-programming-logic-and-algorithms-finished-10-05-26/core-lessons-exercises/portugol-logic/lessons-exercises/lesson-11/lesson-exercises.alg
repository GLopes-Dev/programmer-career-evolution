algoritmo "Review"
var
    count: inteiro
inicio
    count <- 0
    para count <- 0 ate 10 passo 2 faca
        escreval(count)
        count <- count + 1
    fimpara
fimalgoritmo


//

algoritmo "Count1to10"
var
    count: inteiro
inicio
    para count <- 1 ate 10 passo 1 faca
        escreval(count)
    fimpara
fimalgoritmo

//
algoritmo "Sum"
var
    n, c, s: inteiro
inicio
    s <- 0
    para c <- 1 ate 5 passo 1 faca
        escreval("Type a number: ")
        leia(n)
        s <- s + n
    fimpara
    escreval("The numbers sum is: ", s)
fimalgoritmo

//
algoritmo "s"
var
    c, n: inteiro
inicio
    escreva("Type a number: ")
    leia(n)
    se (n%2=1) entao
       n <- n-1
    fimse
    para c <- n ate 0 passo -2 faca
        escreval(c)
    fimpara
    escreval("Count Finished")
fimalgoritmo

//
algoritmo "Between0and10"
var
    c, v, q, s: inteiro
inicio
    q <- 0
    s <- 0
    Para c <- 1 ate 6 faca
        escreva("Type a number: ")
        leia(v)
        se (v >= 0) e (v <=10) entao
            q <- q + 1
        fimse
        se (v%2=1) entao
            s <- s + v
        fimse
    fimpara
    escreval("The total of numbers between 0 and 10 is: ", q)
    escreval("The sum between the inpair numbers is: ", s)
fimalgoritmo



//

algoritmo "Combinations"
var
    c1, c2: inteiro
inicio
    para c1 := 1 ate 3 faca
        para c2 := 1 ate 3 faca
        escreval(c1, c2)
        fimpara
    fimpara

fimalgoritmo