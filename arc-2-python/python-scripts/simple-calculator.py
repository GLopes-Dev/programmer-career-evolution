import tkinter as tk
import math


window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x400")
window.configure(bg="#252423")


visor = tk.Entry(window, font=("Arial", 15), justify="right")
visor.grid(row=0, column=0, columnspan=10, padx=10, pady=10)
visor.configure(bg="#555555")

label = tk.Label(window, text="V0.0.1", fg="#C9C9C9", background="#252423")
label.place(relx=0.01, rely=0.9)


def press_button(num):
    visor.insert(tk.END, num)

def calculate():
    try:
        expression = visor.get()
        expression = expression.replace('x', '*')
        expression = expression.replace('^', '**')
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



btn1 = tk.Button(window, text="1", width=5, height=3, command=lambda: press_button("1"))
btn2 = tk.Button(window, text="2", width=5, height=3, command=lambda: press_button("2"))
btn3 = tk.Button(window, text="3", width=5, height=3, command=lambda: press_button("3"))
btn4 = tk.Button(window, text="4", width=5, height=3, command=lambda: press_button("4"))
btn5 = tk.Button(window, text="5", width=5, height=3, command=lambda: press_button("5"))
btn6 = tk.Button(window, text="6", width=5, height=3, command=lambda: press_button("6"))
btn7 = tk.Button(window, text="7", width=5, height=3, command=lambda: press_button("7"))
btn8 = tk.Button(window, text="8", width=5, height=3, command=lambda: press_button("8"))
btn9 = tk.Button(window, text="9", width=5, height=3, command=lambda: press_button("9"))
btn0 = tk.Button(window, text="0", width=5, height=3, command=lambda: press_button("0"))
btnSum = tk.Button(window, text="+", width=5, height=3, command=lambda: press_button("+"))
btnSub = tk.Button(window, text="-", width=5, height=3, command=lambda: press_button("-"))
btnMult = tk.Button(window, text="X", width=5, height=3, command=lambda: press_button("x"))
btnEqual = tk.Button(window, text="=", width=5, height=3, command=calculate)
btnCE = tk.Button(window, text="CE", width=5, height=3, command=clear)
btnFloat = tk.Button(window, text=".", width=5, height=3, command=lambda: press_button("."))
btnDel = tk.Button(window, text="Del", width=5, height=3, command=delete)
btnExp = tk.Button(window, text="Exp", width=5, height=3, command=lambda: press_button("^"))
btnPL = tk.Button(window, text="(", width=5, height=3, command=lambda: press_button("("))
btnPR = tk.Button(window, text=")", width=5, height=3, command=lambda: press_button(")"))





btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=1)
btnSum.grid(row=1, column=6)
btnSub.grid(row=2, column=6)
btnMult.grid(row=3, column=6)
btnEqual.grid(row=4, column=2)
btnCE.grid(row=1, column=10)
btnFloat.grid(row=4, column=0)
btnDel.grid(row=2, column=10)
btnExp.grid(row=3, column=10)
btnPL.grid(row=4, column=6)
btnPR.grid(row=4, column=10)

btn1.configure(fg="#D8D8D8", bg="#292727")
btn2.configure(fg="#D8D8D8", bg="#292727")
btn3.configure(fg="#D8D8D8", bg="#292727")
btn4.configure(fg="#D8D8D8", bg="#292727")
btn5.configure(fg="#D8D8D8", bg="#292727")
btn6.configure(fg="#D8D8D8", bg="#292727")
btn7.configure(fg="#D8D8D8", bg="#292727")
btn8.configure(fg="#D8D8D8", bg="#292727")
btn9.configure(fg="#D8D8D8", bg="#292727")
btn0.configure(fg="#D8D8D8", bg="#292727")
btnSum.configure(fg="#D8D8D8", bg="#292727")
btnSub.configure(fg="#D8D8D8", bg="#292727")
btnMult.configure(fg="#D8D8D8", bg="#292727")
btnEqual.configure(fg="#D8D8D8", bg="#292727")
btnCE.configure(fg="#D8D8D8", bg="#292727")
btnFloat.configure(fg="#D8D8D8", bg="#292727")
btnDel.configure(fg="#D8D8D8", bg="#292727")
btnExp.configure(fg="#D8D8D8", bg="#292727")
btnPL.configure(fg="#D8D8D8", bg="#292727")
btnPR.configure(fg="#D8D8D8", bg="#292727")

window.mainloop()