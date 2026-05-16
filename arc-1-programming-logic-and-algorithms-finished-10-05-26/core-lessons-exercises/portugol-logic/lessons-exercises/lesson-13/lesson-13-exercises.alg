algoritmo "Function"
var
    v1, v2, sum: real
funcao Soma(a, b: real) : real
var
    sum: real
inicio
    sum <- a + b
    retorne sum
fimfuncao
inicio
    escreval("Type a number: ")
    leia(v1)
    escreval("Type another number: ")
    leia(v2)
    sum <- Soma(v1, v2)
    escreval("The sum between the numbers is ", sum)
fimalgoritmo

algoritmo "EvenOrOdd"
var
    num: inteiro
funcao EvenOrOdd(n: inteiro) : caractere
inicio
    se (n%2=0) entao
        retorne "Even"
    senao
        retorne "Odd"
    fimse
fimfuncao
inicio
    escreval("Type a number: ")
    leia(num)
    escreval(EvenOrOdd(num))
fimalgoritmo

algoritmo "Factorial"
var
    N, F: inteiro

funcao Factorial(V: inteiro):inteiro
var
    C, R: inteiro
inicio
    R <- 1
    para C <- 1 ate V faca
        R <- R * C 
    fimpara
    retorne R
fimfuncao
inicio
    escreval("Type a number: ")
    leia(N)
    F <- Factorial(N)
    escreval(N, "! is ", F)
fimalgoritmo




algoritmo "Fibonacci"
var
    C, T1, T2, T3: inteiro

funcao Fibonacci(var n1, n2, n3: inteiro) : inteiro
inicio
    n3 <- n1 + n2
    retorne n3
    n1 <- n2
    n2 <- n3
fimfuncao
inicio
    T1 <- 0
    escreva(T1)
    T2 <- 1
    escreva(T2)
    para C <- 3 ate 10 faca
        escreva(Fibonacci(T1, T2, T3))
    fimpara
fimalgoritmo


algoritmo "Names Analyzer"
var
    N: caractere
    C: inteiro
inicio
    escreval("Type your name: ")
    leia(N)
    escreval("Your name total letters: ", Compr(N))
    escreval("Your name in Capital is: ", Maiusc(N))
    escreval("Your name in LowerCase is: ", Minusc(N))
    escreval("The first letter of your name is: ", Copia(N, 1, 1))
    escreval("The last letter of your name is: ", Copia(Maiusc(N), Compr(N), 1))
    escreval("The position of letter R in your name is:", Pos("R," Maiusc(N)))
    escreval("The letter R code is: ", Asc("R"))
    escreval("The letter that represents code 82 is: ", Carac(82))
    para C <- Compr(N) ate 1 passo -1 faca
         escreva(Copia(Maiusc(N), C, 1))
    fimpara
fimalgoritmo






algoritmo "Login"
var
    lUser, user: caractere
    pass, lPass, year: real
inicio
    escreval(" S I G N U P ")
    escreval("=============")
    escreva("Username: ")
    leia(user)
    escreva("Password: ")
    leia(pass)
    repita
        escreval("Birth Year: ")
        leia(year)
        se (year <2008) entao
            escreva("You must be at least 18 years old to create an account. ")
        fimse
    ate (year >= 2008)
    escreval(" L O G I N")
    escreval("==========")
    escreva("Username: ")
    leia(lUser)
    escreva("Password: ")
    leia(lPass)
    se (lUser = user) e (lPass = pass) entao
        escreval("Welcome, ", Maiusc(lUser))
    senao
        escreval("Acess Denied. ")
    fimse
fimalgoritmo


algoritmo "Sum"
var
    num1, num2, res: real

funcao Somador(n1, n2: real) : real
inicio
    res <- n1 + n2
    retorne res
fimfuncao
inicio
    escreval("Type a number: ")
    leia(num1)
    escreval("Type another number: ")
    leia(num2)
    res <- Somador(num1, num2)
    escreval("The result is: ", res)
fimalgoritmo

algoritmo "Media"
var
    n1, n2, med: real

funcao Media(nu, nu2: real) : real
inicio
    med <- (nu + nu2) / 2
    retorne med
fimfuncao
inicio
    escreva("Type your first grade: ")
    leia(n1)
    escreva("Type your second grade: ")
    leia(n2)
    med <- Media(n1, n2)
    escreval("Your average was: ", med)
fimalgoritmo




