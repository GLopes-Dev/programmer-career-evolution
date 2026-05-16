///Smart Count: make a program that asks the Start number and final number to count, and make a count. If the start number is smaller than final number, do a progressive count
//If start number is bigger than final number, do a regressive count

algoritmo "Smart Count"
var
    start, end, count: inteiro
inicio
        escreval("-----------------------------------")
        escreval("            SMART COUNT            ")
        escreval("-----------------------------------")
        escreva(" Start: ")
        leia(start)
        escreva(" End: ")
        leia(end)
        escreval("-----------------------------------")
        escreval("              COUNTING             ")
        escreval("-----------------------------------")
        se (start < end) entao
             count <- start
            enquanto (count <= end) faca
                escreval(count, "... ")
                count <- count + 1
            fimenquanto
        senao
             count <- start
            enquanto (count >= end) faca
                escreval(count, "... ")
                count <- count - 1
            fimenquanto
        fimse
fimAlgoritmo
























//Best Class Student. Ask how many students the class has, after that ask the name and the grade of each student that the user said. Ex: if the user says 5 students
//ask the 5 students name and grade. After that shows which student got the highest average

algoritmo "BestClassStudent"
var
    studentAmount: inteiro
    count: inteiro
    bestStudent: caractere
    bestGrade: real
    studentName: caractere
    studentGrade: real
inicio
        escreval("-----------------------------------")
        escreval("  OSCAR MACEDO SOARES HIGH SCHOOL  ")
        escreval("-----------------------------------")
        escreva(" How many students the class has? ")
        leia(studentAmount)
        escreval("-----------------------------------")
        count <- 1
        bestGrade <- 0
        enquanto (count <= studentAmount) faca
            escreval(" ALUNO ", count)
            escreva("Name: ")
            leia(studentName)
            escreva("Grade: ")
            leia(studentGrade)
                se (studentGrade > bestGrade) entao
                     bestGrade <- studentGrade
                     bestStudent <- studentName
                fimse
            count <- count + 1
        fimenquanto
        escreval("The student with the best perfomance was ", bestStudent, " with an Average of ", bestGrade)
        escreval("---------------------------------------------------------------------------------------------")
fimalgoritmo










///

algoritmo "Jiu-Jitsu Tournament"
var
        athletesAmount, count: inteiro
        name, bestName: caractere
        weight, bestWeight: real

inicio
        escreval("--------------------------------------")
        escreval("        JIU JITSU CHAMPIONSHIP        ")
        escreval("--------------------------------------")
        escreva(" How many athletes will compete? ")
        leia(athletesAmount)
        se (athletesAmount = 0) entao
            escreval("------------------------------------------------")
            escreval("  That's so sad, no Athletes in a ChampionShip  ")
        fimse
        count <- 1
        bestWeight <- 0
        enquanto (count <= athletesAmount) faca
            escreval("----------------------")
            escreval(" Athlete ", count)
            escreva("Name: ")
            leia(name)
            escreva("Weight: ")
            leia(weight)
            se (weight < 70) entao
                escreval("Category: Light Weight ")
            senao
                se (weight >= 70) e (weight < 90) entao
                    escreval("Category: Medium Weight ")
                senao
                    escreval("Heavy Weight")
                fimse
            fimse
            se (weight > bestWeight) entao
                bestWeight <- weight
                bestName <- name
            fimse
            count <- count + 1
        fimenquanto
        escreval("-----------------------------------------------------------------------")
        escreval("   The most heavy Athlete is ", bestName, " with, ", bestWeight, "KG   ")
fimalgoritmo



///

algoritmo "Jiu-Jitsu Tournament"
var
        athletesAmount, count: inteiro
        name, bestName: caractere
        weight, bestWeight: real

inicio
        escreval("--------------------------------------")
        escreval("        JIU JITSU CHAMPIONSHIP        ")
        escreval("--------------------------------------")
        escreva(" How many athletes will compete? ")
        leia(athletesAmount)
        count <- 1
        enquanto (count <= athletesAmount) faca
            escreval(" Athlete ", count)
            escreva("Name: ")
            leia(name)
            escreva("Weight: ")
            leia(weight)
            bestWeight <- 0
            se (weight < 70) entao
                escreval("Category: Light Weight ")
            senao
                se (weight >= 70) e (weight < 90) entao
                    escreval("Category: Medium Weight ")
                senao
                    escreval("Heavy Weight")
                fimse
            fimse
        fimenquanto
        se (weight > bestWeight) entao
            bestWeight <- weight
            bestName <- name
        fimse
        escreval("-----------------------------------------------------------------------")
        escreval("   The most heavy Athlete is ", bestName, " with, ", bestWeight, "KG   ")
fimalgoritmo




//

algoritmo "Jiu-Jitsu Tournament"
var
        athletesAmount, count: inteiro
        name, bestName: caractere
        weight, bestWeight: real

inicio
        escreval("--------------------------------------")
        escreval("        JIU JITSU CHAMPIONSHIP        ")
        escreval("--------------------------------------")
        escreva(" How many athletes will compete? ")
        leia(athletesAmount)
        se (athletesAmount = 0) entao
            escreval("------------------------------------------------")
            escreval("  That's so sad, no Athletes in a ChampionShip  ")
        fimse
        count <- 1
        enquanto (count <= athletesAmount) faca
            escreval(" Athlete ", count)
            escreva("Name: ")
            leia(name)
            escreva("Weight: ")
            leia(weight)
            bestWeight <- 0
            se (weight < 70) entao
                escreval("Category: Light Weight ")
            senao
                se (weight >= 70) e (weight < 90) entao
                    escreval("Category: Medium Weight ")
                senao
                    escreval("Heavy Weight")
                fimse
            fimse
            se (weight > bestWeight) entao
                bestWeight <- weight
                bestName <- name
            fimse
            count <- count + 1
        fimenquanto
        escreval("-----------------------------------------------------------------------")
        escreval("   The most heavy Athlete is ", bestName, " with, ", bestWeight, "KG   ")
fimalgoritmo
