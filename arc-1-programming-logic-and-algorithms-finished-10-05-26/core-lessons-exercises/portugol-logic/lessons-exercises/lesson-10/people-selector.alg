///Show total amount of Males with more than 18 years and that have Brown hair
///Show total amount os Females with age between 25-30 years and that have Blonde hair
///Solved Exercise from CursoEmVideo course.


algoritmo "PeopleSelector"
var
    gender, userChoice: caractere
    age, hairColor, totalM, totalF: inteiro
inicio
    totalM <- 0
    totalF <- 0
    repita
        escreval("==========================")
        escreval("    PEOPLE SELECTOR    ")
        escreval("==========================")
        escreva("What's the gender? [M/F] ")
        leia(gender)
        escreva("What's the age? ")
        leia(age)
        escreval("What's the hair color? ")
        escreval("-----------------------")
        escreval("[1] Black")
        escreval("[2] Brown")
        escreval("[3] Blonde")
        escreval("[4] Redhair")
        leia(hairColor)
        se (((gender = "M") ou (gender = "m")) e (age >= 18) e (hairColor = 2)) entao
            totalM <- totalM + 1       
        fimse
        se (((gender = "F") ou (gender = "f")) e ((age >= 25) e (age <= 30)) e (hairColor = 3)) entao
            totalF <- totalF + 1
        fimse
        escreval("Continue? [S/N]")
        leia(userChoice)
        limpatela
    ate ((userChoice = "N") ou (userChoice = "n"))
    limpatela
    escreval("-----------------------")
    escreval("        RESULTS        ")
    escreval("-----------------------")
    escreval("Total amount of Males with more than 18 years and Brown hairs: ", totalM)
    escreval("Total amount of Females with age between 25-30 years and Blonde hair: ", totalF)
fimalgoritmo