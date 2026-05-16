algoritmo "BiDevOs"
var


//Enter to go Back trick
procedimento Wait()
var
    enter: caractere
inicio
    leia(enter)
fimprocedimento


//BIDEVOS MAIN MENU
procedimento Menu()
var
    op: inteiro
inicio
    repita
        limpatela
        escreval(" ===============[03-05-26]=============== ")
        escreval("|                Welcome!                |")
        escreval("|  [1] App Hub            [2] Info       |")
        escreval("|  [3] Donate             [4] Changelog  |")
        escreval("|               [5] Leave                |")
        escreval(" ======================================== ")
        escreval("Select Option: ")
        leia(op)
        escolha (op)
            caso 1
               AppHub()
            caso 2
               Info()
            caso 3
               Donate()
            caso 4
               Changelog()
        fimescolha
    ate (op = 5)
fimprocedimento

//MAIN Menu AppHub Option UI
procedimento AppHub()
var
    op: inteiro
inicio
    repita
        limpatela
        escreval(" =========[App Hub]========= ")
        escreval("| [1] Calculator            |")
        escreval("| [2] Register App          |")
        escreval("| [3] Age Checker           |")
        escreval("| [4] Back...               |")
        escreval(" =========================== ")
        escreval("Select Option: ")
        leia(op)
        escolha (op)
            caso 1
                Calculator()
            caso 2

            caso 3
        fimescolha
    ate (op = 4)
fimprocedimento

//MAIN Menu Info Option UI
procedimento Info()
inicio
    limpatela
    escreval(" ========================= ")
    escreval("| Program Name: BiDevOS   |")
    escreval("| Program Version: 2.0    |")
    escreval("| Creation Date: 03/05/26 |")
    escreval("| Last Updated: 10/05/26  |")
    escreval("| Scripted by GabrielDev  |")
    escreval(" ========================= ")
    escreval(" Press ENTER to go back...")
    Wait()
fimprocedimento

//MAIN Menu Donate Option UI
procedimento Donate()
var
    op: inteiro
inicio
    repita
        limpatela
        escreval(" =========[Donate]========= ")
        escreval("| [1] To donate $5        |")
        escreval("| [2] To donate $10       |")
        escreval("| [3] To donate $20       |")
        escreval("| [4] To donate $50       |")
        escreval("| [5] Back...             |")
        escreval(" ========================= ")
        escreva(" Select Option: ")
        leia(op)
            escolha (op)
                caso 1
                    escreval("You donated $5. Thank you!")|
                    escreval("==========================")
                    escreval("[1] Continue")
                    leia(op)
                    limpatela
                caso 2
                    escreval("You donated $10. Thank you!")
                    escreval("==========================")
                    escreval("[1] Continue")
                    leia(op)
                    limpatela
                caso 3
                    escreval("You donated $20. Thank you!")
                    escreval("==========================")
                    escreval("[1] Continue")
                    leia(op)
                    limpatela
                caso 4
                    escreval("You donated $50. Thank you!")
                    escreval("==========================")
                    escreval("[1] Continue")
                    leia(op)
                    limpatela
           fimescolha
    ate (op = 5)
fimprocedimento

//Calculator App UI
procedimento Calculator()
var
  op: inteiro
inicio
        limpatela
        escreval(" ========================================== ")
        escreval("   W E L C O M E  TO  C A L C U L A T O R   ")
        escreval(" ========================================== ")
        escreval("|               O P T I O N S              |")
        escreval("|------------------------------------------|")
        escreval("| [1] Sum (+)         |   [2] Subtract (-) |")
        escreval("| [3] To divide (÷)   |   [4] Multiply (X) |")
        escreval("| [5] Square Root     |   [6] Power        |")
        escreval("| [7] Back...")
        escreval("|------------------------------------------|")
        escreval("Select Option: ")
        leia(op)
        escolha (op)
            caso 1
                CalculatorSumSys()
            caso 2
                CalculatorSubSys()
            caso 3
                CalculatorDivSys()
        fimescolha
fimprocedimento

///Calculator Sum Option
procedimento CalculatorSumSys()
var
   q, i, b: inteiro
   n, s: real
inicio
    repita
        limpatela
        escreval("==============")
        escreval("  SUM SYSTEM  ")
        escreval("==============")
        escreval("How many numbers do you want to sum? ")
        leia(q)
        escreval("--------------")
        para i de 1 ate q faca
            escreval("Type the ", i, "º number: ")
            leia(n)
            s <- s + n
        fimpara
        escreval("--------------")
        escreval("The sum between the numbers is ", s)
        escreval("--------------")
        escreval("[1] Continue")
        escreval("[2] Back...")
        leia(b)
        s <- 0
    ate (b = 2)
fimprocedimento

//Calculator SubTract Option
procedimento CalculatorSubSys()
var
   q, b: inteiro
   s, n, firstN: real
inicio
    repita
        limpatela
        escreval("===================")
        escreval("  SUBTRACT SYSTEM  ")
        escreval("===================")
        escreval("How many numbers do you want to subtract? ")
        leia(q)
        escreval("Type the 1 number: ")
        leia(firstN)
        para q de 2 ate q faca
            escreval("Type the", q, " number: ")
            leia(n)
            firstN <- firstN - n
            s <- firstN
        fimpara
        escreval("-------------------")
        escreval("The result is ", s)
        escreval("-------------------")
        escreval("[1] Continue")
        escreval("[2] Back")
        leia(b)
        s <- 0
    ate (b = 2)
fimprocedimento

//To Divide Calculator Option
procedimento CalculatorDivSys()
var
    q, b: inteiro
    firstN, n, s: real
inicio
    repita
        limpatela
        escreval("====================")
        escreval("  TO DIVIDE SYSTEM  ")
        escreval("====================")
        escreval("How many numbers do you want to divide? ")
        leia(q)
        escreval("Type the 1 number: ")
        leia(firstN)
        para q de 2 ate q faca
            escreval("Type the ", q, " number: ")
            repita
                leia(n)
                se (n = 0) entao
                    escreval("--------------------------")
                    escreval("ERRO! Can't divide 0 by 0")
                    escreval("Try Again: ")
                    escreval("------------")
                    escreval("Type the ", q, " number: ")
                senao
                    interrompa
                fimse
            ate (n > 0)
            firstN <- firstN / n
            s <- firstN
        fimpara
        escreval("-------------------")
        escreval("The result is ", s)
        escreval("-------------------")
        escreval("[1] Continue")
        escreval("[2] Back")
        leia(b)
        s <- 0
    ate (b = 2)
fimprocedimento

//RegisterApp UI
procedimento RegisterApp()
inicio

fimprocedimento

//RegisterApp SYSTEM
procedimento RegisterAppSys()
inicio

fimprocedimento

//AgeChecker App UI
procedimento AgeChecker()
inicio

fimprocedimento

//AgeChecker App SYSTEM
procedimento AgeCheckerSys()
inicio

fimprocedimento

//MAIN Menu Changelog Option UI
procedimento Changelog()
inicio
    limpatela
    escreval("|======================================================================================================|")
    escreval("|/                                                                                                    \|")
    escreval("|<-------------->                                                                                      |")
    escreval("| V1.5 ChangeLog |                                                                                     |")
    escreval("|<-------------->                                                                                      |")
    escreval("|[FIXED]                                                                                               |")
    escreval("| Data Security:                                                                                       |")
    escreval("| - Solved the to divide by 0 critic ERROR.                                                            |")
    escreval("| - Validantion Filter Implemented, preventing system CRASH.                                           |")
    escreval("|------------                                                                                          |")
    escreval("|[IMPROVED]                                                                                            |")
    escreval("| Global Refactoring:                                                                                  |")
    escreval("| - 30 Global Variables reduction to 0 (Local Scope Improvement.                                       |")
    escreval("| Modularization:                                                                                      |")
    escreval("| - System got transformed in Independent Blocks.                                                      |")
    escreval("| - Main Code has just 2 lines now, calling specifics procedures.                                      |")
    escreval("|------------                                                                                          |")
    escreval("|[ADDED]                                                                                               |")
    escreval("| Calculator Update:                                                                                   |")
    escreval("| - Subtraction and To divide logic is done, supporting multiple numbers and dynamics accumulators.    |")
    escreval("| ChangeLog:                                                                                           |")
    escreval("| - New section added to Main Menu, allowing the user to see the update and improvements historic.     |")
    escreval("|------------                                                                                          |")
    escreval("|[COMING SOON...]                                                                                      |")
    escreval("| Sign Up and Login System, with Global Arrays.                                                        |")
    escreval("| Complete Calculator App System.                                                                      |")
    escreval("|\                                                                                                    /|")
    escreval("|======================================================================================================|")
    escreval("Press ENTER to go BACK...")
    Wait()
fimprocedimento

//BiDevOs Leaving Message
procedimento Leaving()
inicio
    limpatela
    escreval(" =========[03-05-26]======== ")
    escreval("| Turning Off...            |")
    escreval("| Thank you!                |")
    escreval("| See you nextime!          |")
    escreval(" ==========[BiDevOS]=========")
fimprocedimento

//Principal Code
inicio
        Mudacor("Branco", "Fundos")
        Mudacor("Preto", "Frente")
        Menu()
        Leaving()
fimalgoritmo