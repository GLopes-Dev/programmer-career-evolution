#My first practical tiny project in Python
#I started by developing a simple calculator in the terminal and, through research about graphical interfaces, I upgraded the project using Tkinter library and then
#to CustomTkinter, learning how to customize buttons, manage grid layouts and handle events
#Sin, Cos and Tan buttons don't work yet

import tkinter as tk
import math
import customtkinter as ctk

#Main Window
window = ctk.CTk()
window.title("Simple Calculator")
window.geometry("360x410")
window.configure(fg_color="#252423")

for col in range(0, 4):
    window.grid_columnconfigure(col, weight=1)


#Visor
visor = ctk.CTkEntry(
    window,
    font=("Arial", 20, "bold"),
    text_color="#D4CDCD",
    justify="right",
    height=40
)
visor.grid(
    row=0, 
    column=0, 
    columnspan=11,
    padx=10, 
    pady=20,
    sticky="ew"
)
visor.configure(
    fg_color="#312F2F",
    border_color="#252424"
)



#Label
label = ctk.CTkLabel(
    window, 
    text="By BielDev", 
    text_color="#4E4A4A", 
    fg_color="#252423"
)
label.place(
    relx=0.42, 
    rely=0.93
)



#Functions
def press_button(num):
    visor.insert(tk.END, num)

def calculate():
    try:
        expression = visor.get()
        expression = expression.replace('x', '*')
        expression = expression.replace('^', '**')
        expression = expression.replace('÷', '/')
        result = eval(expression)
        visor.delete(0, tk.END)
        visor.insert(0, str(result))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Error")


def clear():
    visor.delete(0, tk.END)


def delete():   
    size = len(visor.get())
    if size > 0:
        visor.delete(size - 1)


#Buttons
btn1 = ctk.CTkButton(
    window, 
    text="1",
    font=("Arial", 16, "bold"), 
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("1")
)

btn2 = ctk.CTkButton(
    window, 
    text="2",
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("2")
)

btn3 = ctk.CTkButton(
    window, 
    text="3",
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",  
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("3")
)

btn4 = ctk.CTkButton(
    window, 
    text="4",
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",  
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("4")
)

btn5 = ctk.CTkButton(
    window, 
    text="5",
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",  
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("5")
)

btn6 = ctk.CTkButton(
    window, 
    text="6", 
    font=("Arial", 16, "bold"), 
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("6")
)

btn7 = ctk.CTkButton(
    window, 
    text="7", 
    font=("Arial", 16, "bold"), 
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("7")
)

btn8 = ctk.CTkButton(
    window, 
    text="8", 
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("8")
)

btn9 = ctk.CTkButton(
    window, 
    text="9", 
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("9")
)

btn0 = ctk.CTkButton(
    window, 
    text="0", 
    font=("Arial", 16, "bold"),
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("0")
)

btnSum = ctk.CTkButton(
    window, 
    text="+", 
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("+")
)

btnSub = ctk.CTkButton(
    window, 
    text="-", 
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25,
    command=lambda: 
    press_button("-")
)

btnMult = ctk.CTkButton(
    window, 
    text="X", 
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("x")
)

btnDiv = ctk.CTkButton(
    window,
    text="÷",
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50,
    height=45,
    corner_radius=25,
    command=lambda:
    press_button("÷")
)

btnEqual = ctk.CTkButton(
    window, 
    text="=", 
    font=("Arial", 16, "bold"),
    fg_color="#595F8D",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#595F8D",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25,
    command=calculate
)

btnCE = ctk.CTkButton(
    window, 
    text="CE", 
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25,
    command=clear
)

btnFloat = ctk.CTkButton(
    window, 
    text=".", 
    font=("Arial", 16, "bold"), 
    fg_color="#2C2A2A",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25,
    command=lambda: 
    press_button(".")
)

btnDel = ctk.CTkButton(
    window, 
    text="Del",
    font=("Arial", 16, "bold"), 
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424", 
    width=50, 
    height=45,
    corner_radius=25, 
    command=delete
)

btnExp = ctk.CTkButton(
    window, 
    text="Exp", 
    font=("Arial", 16, "bold"), 
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25, 
    command=lambda: 
    press_button("^")
)

btnSin = ctk.CTkButton(
    window,
    text="Sin",
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50,
    height=45,
    corner_radius=25,
    command=lambda:
    press_button("Sin(")
)

btnCos = ctk.CTkButton(
    window,
    text="Cos",
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50,
    height=45,
    corner_radius=25,
)

btnTan = ctk.CTkButton(
    window,
    text="Tan",
    font=("Arial", 16, "bold"),
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#252735",
    hover_color="#252424",
    width=50,
    height=45,
    corner_radius=25
)

btnPL = ctk.CTkButton(
    window, 
    text="(", 
    font=("Arial", 16, "bold"), 
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50, 
    height=45,
    corner_radius=25,
    command=lambda: 
    press_button("(")
)

btnPR = ctk.CTkButton(
    window, 
    text=")", 
    font=("Arial", 16, "bold"), 
    fg_color="#252735",
    text_color="#D4CDCD",
    border_width=2,
    border_color="#2B2828",
    hover_color="#252424",
    width=50,
    height=45,
    corner_radius=25,
    command=lambda: 
    press_button(")")
)




#Buttons Positions
btn1.grid(row=1, column=0, padx=5, pady=8)
btn2.grid(row=1, column=1, padx=5, pady=8)
btn3.grid(row=1, column=2, padx=5, pady=8)
btn4.grid(row=2, column=0, padx=5, pady=8)
btn5.grid(row=2, column=1, padx=5, pady=8)
btn6.grid(row=2, column=2, padx=5, pady=8)
btn7.grid(row=3, column=0, padx=5, pady=8)
btn8.grid(row=3, column=1, padx=5, pady=8)
btn9.grid(row=3, column=2, padx=5, pady=8)
btn0.grid(row=4, column=1, padx=5, pady=8)
btnSum.grid(row=1, column=3, padx=5, pady=8)
btnSub.grid(row=2, column=3, padx=5, pady=8)
btnMult.grid(row=3, column=3, padx=5, pady=8)
btnDiv.grid(row=4, column=3, padx=5, pady=8)
btnEqual.grid(row=4, column=2, padx=5, pady=8)
btnCE.grid(row=1, column=4, padx=5, pady=8)
btnFloat.grid(row=4, column=0, padx=5, pady=8)
btnDel.grid(row=2, column=4, padx=5, pady=8)
btnExp.grid(row=3, column=4, padx=5, pady=8)
btnSin.grid(row=4, column=4, padx=5, pady=8)
btnCos.grid(row=5, column=3, padx=5, pady=8)
btnTan.grid(row=5, column=4, padx=5, pady=8)
btnPL.grid(row=5, column=0, padx=5, pady=8)
btnPR.grid(row=5, column=2, padx=5, pady=8)




window.mainloop()