algoritmo "TheDojoEntrance"
var
    userAge: inteiro
    belt: logico
    days: inteiro
inicio
        escreval("-----------------------------")
        escreval("      THE DOJO ENTRANCE      ")
        escreval("-----------------------------")
        escreval(" Your age: ")
         leia(userAge)
        escreval(" Do you have a Yellow Belt? ")
         leia(belt)
        escreval(" How many Days have you practiced?")
         leia(days)
        escreval("-----------------------------")
        se (age >= 18 e belt = verdadeiro) ou (idade < 18 e days > 30) entao
            escreva(" Welcome to the advanced Class!")
        senao
            escrreva(" Acess Denied.")
        fimse
fimalgoritmo