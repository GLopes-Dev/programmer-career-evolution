algoritmo "Rank Checker"
var
    age, num: inteiro
    category: caractere
procedimento CheckCategory(var ag: inteiro)
inicio
    se (ag < 12) entao
        category <- "denied"
    senao
        se (ag >= 12) e (ag <=15) entao
            category <- "Junior"
        senao
            se (ag >= 16) e (ag <= 18) entao
                category <- "Intermediate"
            senao
                category <- "Senior"
            fimse
        fimse
    fimse
fimprocedimento
inicio
    repita
        escreval("====================")
        escreval("    RANK CHECKER    ")
        escreval("====================")
        escreval("What's the athlete's age? ")
        leia(age)
        CheckCategory(age)
        escreval("====================")
        se (category = "denied") entao
            escreval("Age not permitted ")
        senao 
            escreval("The Athlete's category is ", category)
        fimse
        escreval("====================")
        escreval("[1] Continue")
        escreval("[2] Leave")
        escreval("====================")
        leia(num)
        limpatela
    ate num = 2
    limpatela
    escreval("===================")
    escreval("Leaving program...")
    escreval("===================")
fimalgoritmo