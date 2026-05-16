algoritmo "SuperSum"
var
    N, Cont, S: inteiro
inicio
    S <- 0
    Cont <- 1
    enquanto (Cont <= 5) faca
        escreva("Type the ", Cont, " number: ")
        Leia(N)
        S <- S + N
        Cont <- Cont + 1
    fimenquanto
    escreval("The sum of all the values entered is ", S)
fimalgoritmo

//


algoritmo "Leilao"
var
    n, s: inteiro
    answer: caractere
inicio
        s <- 0
        Repita
            escreva("Type a number: ")
            leia(n)
            s <- s + n
            escreva("Do you want to continue? [S/N]")
            leia(answer)
        ate (resp = "N")
         escreval("The sum of all the numbers is: ", s)
fimalgoritmo



//

algoritmo "Count"
var
    count, n, r: inteiro
inicio
    count <- 1
    Escreva("What number multiplication table do you want to see? ")
    leia(n)
    repita
        r <- N * count
        escreval(n, " x ", count, " = ", r)
        count <- count + 1
    ate (count > 10)
    escreval("Count Finished")
fimalgoritmo


//

algoritmo "Negative Counter" 
var
    n, c, totN: inteiro
inicio
    c <- 1
    totN <- 0
    repita
        escreva("Type a number: ")
        leia(n)
        se (n < 0) entao
            totN <- totN + 1
        fimse
        c <- c + 1
    ate (c > 5)
    escreva("Negative numbers amount: ", totN)
fimalgoritmo

//

algoritmo "Factorial"
var
    c, n, f: inteiro
    r: caractere
inicio
Repita
    escreva("What number factorial do you want to know? ")
    leia(n)
    c <- n
    f <- 1
    repita
        f <- f * c
        c <- c - 1
    ate (c < 1)
    escreval("The factorial value of ", n, " is ", f)
    escreva("Continue? [S/N] ")
    leia(r)
    LimpaTela
Ate (r = "N")
fimalgoritmo


//

algoritmo "Primes"
var
    c, n, contDiv: inteiro
inicio
    c <- 1
    contDiv <- 0
    escreva("Type a number: ")
    leia(n)
    repita
        se (n % c = 0) entao
           contDiv <- contDiv + 1
        fimse
        c <- c + 1
    ate (c > n)|
    se (contDiv > 2) entao
       escreval(n, " is not a Prime number")
    senao
       escreval(n, " is a Prime number")
    fimse
fimalgoritmo

