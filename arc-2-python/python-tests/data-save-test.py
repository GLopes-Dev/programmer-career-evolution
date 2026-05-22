import os
import time
from pathlib import Path

script_path = Path(__file__).parent
file_path = script_path / "clients.txt"


def menu():
    clearScreen()
    global option
    print("=" * 10, "M E N U", "=" * 10)
    print(" [1] Register Student\n [2] All registered students\n [3] Leave...")
    print("=" * 29)
    option = int(input("Select Option: "))
    return option

def clearScreen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def regMenu():
    clearScreen()
    print("=" * 10, "REGISTER MENU", "=" * 10)
    nm = input("Name: ")
    cp = input("CPF: ")
    print("=" * 33)
    return nm, cp

def listMenu():
    clearScreen()
    with open(file_path, "r") as file:
        for linha in file:
            print(linha.strip())
    back()


def back():
    b = input("Press ENTER to go back...")

option = 0

while option != 3:
    option = menu()
    match option:
        case 1:
            name, cpf = regMenu()
            with open(file_path, "a") as file:
                file.write(f"Name: {name} | CPF: {cpf} \n ")
            print("Student registered successfully!")
            back()
        case 2:
            listMenu()

        case 3:
            clearScreen()
            print("Leaving...")
            break
