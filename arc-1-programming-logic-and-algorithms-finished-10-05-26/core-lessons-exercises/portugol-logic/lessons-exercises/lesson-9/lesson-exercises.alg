algoritmo "ConteAte10"
var
   contador: inteiro
inicio
    contador <- 0
     Enquanto (contador <= 10) faca
       escreval(contador)
       contador <- contador + 1
    fimenquanto
    escreva("Count finished")
fimalgoritmo

//

algoritmo "somadorNumerico"
var
    count, num, sum, big, small: inteiro
inicio
        count <- 1
        sum <- 0
        Enquanto (count <= 5) faca
            escreva("Write the ", count, "th. number: ")
            leia(num)
             se (num > big) entao
               big <- num
             fimse
             se (count = 1) entao
                small <- num
             senao
                  se (num < small) entao
                     small <- num
                  fimse
             fimse
            sum <- sum + num
            count <- count + 1
        fimEnquanto
        escreval(" The sum of all values was ", sum)
        escreval(" The biggest number was ", big)
        escreval(" The smallest number was ", small)
fimalgoritmo

//

aalgoritmo "ConversorMoedas"
var
    reais, dolar: real
    count, userCount: inteiro
inicio
    count <- 1
    escreva("How many converts do you want to do? ")
    leia(userCount)
    enquanto (count <= userCount) faca
        escreva("What's the value in R$? ")
        leia(reais)
        dolar <- reais/2.20
        escreval("The converted value is US$", dolar:5:2)
        count <- count + 1
    fimEnquanto
fimalgoritmo

//

algoritmo "LoopInfinitoProblema"
var

inicio

fimalgoritmo