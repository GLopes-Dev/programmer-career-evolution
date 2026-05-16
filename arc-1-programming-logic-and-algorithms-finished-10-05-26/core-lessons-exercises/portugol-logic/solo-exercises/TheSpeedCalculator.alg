algoritmo "BikeTripPerfomance"
var
    km, hours, minutes, velocity, pace: real
procedimento Menu()
inicio
        escreval("============================")
        escreval("    BIKE TRIP PERFOMANCE    ")
        escreval("============================")
fimprocedimento  
procedimento KmAverage(var k, h, m: real)
inicio
    velocity <- k / h
    pace <- m / k 
fimprocedimento
inicio
        Menu()
        escreva("Distance Traveled: ")
        leia(km)
        escreva("Time elapsed: ")
        leia(minutes)
        hours <- minutes / 60
        escreval("(", hours, ") hours.")
        escreval("----------------------------")
        KmAverage(km, hours, minutes)
        escreval("RESULT: ", velocity:3:1, "Km/h")
        escreval("Estimated time to cover 1Km: ", pace, " minutes.")
        escreval("============================")
fimalgoritmo