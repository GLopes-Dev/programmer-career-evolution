algoritmo "The Odd Sum"
var
    count, n, neg, sum: inteiro
inicio
    escreva("How many numbers do you want to type? ")
    leia(count)
    para count <- 1 ate count faca
        escreva("Type the ", count, "th number: ")
        leia(n)
        se (n%2 = 1) entao
            sum <- sum + n
        fimse
        se (n < 0) entao
            neg <- neg + 1
        fimse
    fimpara
        escreval("The sum between the numbers is: ", sum)
        escreval("The negative numbers amount was: ", neg)
fimalgoritmo


algoritmo "The price is right"
var
    c: inteiro
    price, min, max: real
inicio
    para c <- 1 ate 5 faca
        escreva("Type the ", c, "th product price: ")
        leia(price)
        se (c = 1) entao
           max <- price
           min <- price
        senao
           se (price > max) entao
              max <- price
           fimse
           se (price < min) entao
              min <- price
           fimse
        fimse
    fimpara
    escreval("The most expensive price was: ", max)
    escreval("The Cheapest price was: ", min)
fimalgoritmo


algoritmo "Age Converter"
var
    acYear, birYear, age: inteiro
inicio
    escreva("What year we're in? ")
    leia(acYear)
    escreva("What's your birth Year? ")
    leia(birYear)
    age <- acYear - birYear
    escreval("You have ", age, " years.")
    se (age >= 18) entao
        escreval("You're of legal age.")
    senao
        escreval("You're minor.")
    fimse
fimalgoritmo




algoritmo "The Triangle of Shadows"
var
    n1, n2, sum: inteiro
inicio
    escreva("Type a number: ")
    leia(n1)
    escreva("Type another number: ")
    leia(n2)
    sum <- n1 + n2
    se (sum%2 = 0) entao
        escreval("Even sum!")
    senao
        escreval("Odd sum!")
    fimse
    escreval("The sum between ", n1, " and ", n2, " is: ", sum)
fimalgoritmo




algoritmo "Smart Count"
var
    start, end: inteiro
inicio
    escreva("Start number: ")
    leia(start)
    escreva("End number: ")
    leia(end)
    se (start < end) entao
        para start <- start ate end passo 1 faca
            escreva(start, "...")
        fimpara
    senao
        para start <- start ate end passo -1 faca
            escreva(start, "...")
        fimpara
    fimse
fimalgoritmo



algoritmo "Small Stock"
var
    count: inteiro
    pName, expProd: caractere
    price, sum, expPrice, med: real
inicio
        escreva("How many products do you want to registrate? ")
        leia(count)
        para count <- 1 ate count faca
            escreval("===============")
            escreva("Product", count, " Name: ")
            leia(pName)
            escreva("Product Price: ")
            leia(price)
            se (price > expPrice) entao
                expPrice <- price
                expProd <- pName
            fimse           
            sum <- sum + price
        fimpara
        med <- sum / count
        escreval("The price medium of all products is: ", med)
        escreval("The most expensive product is ", expProd, " with a value of R$", expPrice)
fimalgoritmo