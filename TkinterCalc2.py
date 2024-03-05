from tkinter import *
import tkinter.font as tkFont

formula = ""
history = []

def press(num):
    global formula
    formula = formula + str(num)
    equation.set(formula)

def equalpress(event=None):
    try:
        global formula, history
        total = str(eval(formula))
        equation.set(total)
        history.append(f"{formula} = {total}")
        update_history()
        formula = ""
    except Exception as e:
        equation.set(" error ")
        formula = ""

def clearpress(event=None):
    global formula
    formula = ""
    equation.set("")

def update_history():
    history_listbox.delete(0, END)
    for item in history[-5:]:
        history_listbox.insert(END, item)

def _quit():
    gui.quit()
    gui.destroy()

if __name__ == "__main__":
    gui = Tk()

    fontStyle = tkFont.Font(family="Lucida Grande", size=14)

    gui.configure(background="#566553")

    gui.title("Basic Calculator")

    gui.geometry("300x290")  # Adjusted height to accommodate the history listbox
    gui.resizable(width=False, height=False)
    gui.protocol("WM_DELETE_WINDOW", _quit)

    equation = StringVar()

    expression_field = Entry(gui, font=fontStyle, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=27)

    button1 = Button(gui, font=fontStyle, text=' 1 ', fg='black', highlightbackground='light green',
                     command=lambda: press(1), height=1, width=4)
    button1.grid(row=2, column=0)
    gui.bind('1', lambda e: press(1))
    
    button2 = Button(gui, font=fontStyle, text=' 2 ', fg='black', highlightbackground='light green',
                     command=lambda: press(2), height=1, width=4)
    button2.grid(row=2, column=1)
    gui.bind('2', lambda e: press(2))
    
    button3 = Button(gui, font=fontStyle, text=' 3 ', fg='black', highlightbackground='light green',
                     command=lambda: press(3), height=1, width=4)
    button3.grid(row=2, column=2)
    gui.bind('3', lambda e: press(3))
    
    button4 = Button(gui, font=fontStyle, text=' 4 ', fg='black', highlightbackground='light green',
                     command=lambda: press(4), height=1, width=4)
    button4.grid(row=3, column=0)
    gui.bind('4', lambda e: press(4))
    
    button5 = Button(gui, font=fontStyle, text=' 5 ', fg='black', highlightbackground='light green',
                     command=lambda: press(5), height=1, width=4)
    button5.grid(row=3, column=1)
    gui.bind('5', lambda e: press(5))
    
    button6 = Button(gui, font=fontStyle, text=' 6 ', fg='black', highlightbackground='light green',
                     command=lambda: press(6), height=1, width=4)
    button6.grid(row=3, column=2)
    gui.bind('6', lambda e: press(6))
    
    button7 = Button(gui, font=fontStyle, text=' 7 ', fg='black', highlightbackground='light green',
                     command=lambda: press(7), height=1, width=4)
    button7.grid(row=4, column=0)
    gui.bind('7', lambda e: press(7))
    
    button8 = Button(gui, font=fontStyle, text=' 8 ', fg='black', highlightbackground='light green',
                     command=lambda: press(8), height=1, width=4)
    button8.grid(row=4, column=1)
    gui.bind('8', lambda e: press(8))
    
    button9 = Button(gui, font=fontStyle, text=' 9 ', fg='black', highlightbackground='light green',
                     command=lambda: press(9), height=1, width=4)
    button9.grid(row=4, column=2)
    gui.bind('9', lambda e: press(9))
    
    button0 = Button(gui, font=fontStyle, text=' 0 ', fg='black', highlightbackground='light green',
                     command=lambda: press(0), height=1, width=4)
    button0.grid(row=5, column=0)
    gui.bind('0', lambda e: press(0))
    plus = Button(gui, font=fontStyle, text=' + ', fg='black', highlightbackground='light green',
                  command=lambda: press("+"), height=1, width=4)
    plus.grid(row=2, column=3)
    gui.bind('+', lambda e: press("+"))
    
    minus = Button(gui, font=fontStyle, text=' - ', fg='black', highlightbackground='light green',
                   command=lambda: press("-"), height=1, width=4)
    minus.grid(row=3, column=3)
    gui.bind('-', lambda e: press("-"))
    
    multiply = Button(gui, font=fontStyle, text=' * ', fg='black', highlightbackground='light green',
                      command=lambda: press("*"), height=1, width=4)
    multiply.grid(row=4, column=3)
    gui.bind('*', lambda e: press("*"))
    
    divide = Button(gui, font=fontStyle, text=' / ', fg='black', highlightbackground='light green',
                    command=lambda: press("/"), height=1, width=4)
    divide.grid(row=5, column=3)
    gui.bind('/', lambda e: press("/"))

    history_listbox = Listbox(gui, font=fontStyle, height=5, width=33)
    history_listbox.grid(row=8, column=0, columnspan=4)

    equal = Button(gui, font=fontStyle, text=' = ', fg='black', highlightbackground='light green',
                   command=equalpress, height=1, width=4)
    equal.grid(row=5, column=2)
    gui.bind('=', equalpress)
    gui.bind('<Return>', equalpress)

    clear = Button(gui, font=fontStyle, text='Clear', fg='black', highlightbackground='light green',
                   command=clearpress, height=1, width=4)
    clear.grid(row=6, column=3)
    gui.bind('<BackSpace>', clearpress)

    Decimal = Button(gui, font=fontStyle, text='.', fg='black', highlightbackground='light green',
                     command=lambda: press('.'), height=1, width=4)
    Decimal.grid(row=5, column=1)
    gui.bind('.', lambda e: press("."))
    
    LeftPar = Button(gui, font=fontStyle, text='(', fg='black', highlightbackground='light green',
                     command=lambda: press('('), height=1, width=4)
    LeftPar.grid(row=6, column=1)
    gui.bind('(', lambda e: press("("))

    RightPar = Button(gui, font=fontStyle, text=')', fg='black', highlightbackground='light green',
                     command=lambda: press(')'), height=1, width=4)
    RightPar.grid(row=6, column=2)
    gui.bind(')', lambda e: press(")"))
    
    Exponent = Button(gui, font=fontStyle, text='^', fg='black', highlightbackground='light green',
                     command=lambda: press('**'), height=1, width=4)
    Exponent.grid(row=6, column=0)
    gui.bind('^', lambda e: press("**"))

    test = Label(gui, text="Made by Groeneveld", bg="#566553", fg="white")
    test.grid(row=9, column=1, columnspan=2)

    gui.mainloop()