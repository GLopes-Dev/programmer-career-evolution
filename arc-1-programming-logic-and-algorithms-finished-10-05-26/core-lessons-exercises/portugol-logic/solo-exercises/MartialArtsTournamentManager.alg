algoritmo "MartialArtsTournamentManager"
var
    num, num2: inteiro
    weight, hWeight, sWeight: real
    name, hName, sName: caractere
procedimento Menu()
inicio
    limpatela
    escreval("=======================")
    escreval("    TOURNAMENT MENU    ")
    escreval("=======================")
    escreval("[1] Register Fighter ")
    escreval("[2] Show Tournament Stats")
    escreval("[3] Exit")
    escreval("=======================")  
fimprocedimento
procedimento Check(var n: caractere; w: real)
inicio
    se (w > hWeight) entao
        hWeight <- w
        hName <- n 
    fimse
    se (w < sWeight) entao
        sWeight <- w
        sName <- n
    fimse
fimprocedimento
inicio
    hWeight <- 0
    sWeight <- 99999999999
    repita
        Menu()
        leia(num)
        escolha (num) caso
            caso 1
                Menu()
                escreva("What's the fighter name? ")
                leia(name)
                escreva("What's the fighter weight? ")
                repita
                    leia(weight)
                    se (weight <=0) entao
                        escreval("Invalid Option. The weight must be greater than 0")
                        escreva("Try again.")
                    fimse
                ate weight>0
                Check(name, weight)
            caso 2
            limpatela
            escreval("     STATUS     ")
            escreval("================")
            escreval("The fighter with the highest weight is ", hName, " with ", hWeight, "KG")
            escreval("The fighter with the smallest weight is ", sName, " with ", sWeight, "KG")
            escreval("================")
            escreval("[4] Back ")
            leia (num2)
        fimescolha
    ate num = 3
        limpatela
        escreval("======================")
        escreval("Leaving program... Thank you!")
        escreval("======================")
fimalgoritmo