//Super Contador

algoritmo "Super Counter"
var
    userChoice, count, num: inteiro
inicio
    repita
        escreval("=================")
        escreval("|    M E N U    |")
        escreval("=================")
        escreval("| [1] from 1 to 10 ")
        escreval("| [2] from 10 to 1 ")
        escreval("| [3] Leave        ")
        escreval("=================")
        leia(userChoice)
        se (userChoice = 1) entao
            count <- 1
            repita
                escreval(count, "...")
                count <- count + 1
            ate (count > 10)
        fimse
        se (userChoice = 2) entao
            count <- 10
            repita
                escreval(count, "...")
                count <- count - 1
            ate (count < 1)
        fimse
        se (userChoice > 3) entao
            escreval("Invalid Option. Try again.")
        fimse
    ate (userChoice = 3)
    escreval("Leaving...")
fimalgoritmo
