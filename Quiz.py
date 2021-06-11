from tkinter import *
from tkinter.ttk import *
window = Tk()
window.geometry("200x200")

flagbasket = 0
flagomada = 0
flaginsta = 0
flagconsole = 0
def barchange(*args):
    global flagbasket
    global flagomada
    global flaginsta
    global flagconsole
    if basket.get() == "Timwros" and flagbasket == 0:
        progr.set(progr.get() + 25)
        flagbasket = 1
    if omada.get() == "Vazelia" and flagomada == 0:
        progr.set(progr.get() + 25)
        flagomada = 2
    if insta.get() == "olympiacosfc" and flaginsta == 0:
        progr.set(progr.get() + 25)
        flaginsta = 3
    if console.get() == "Ps5" and flagconsole == 0:
        progr.set(progr.get() + 25)
        flagconsole = 4
progr = IntVar()
progr.set(0)
bar = Progressbar(window, length=300, style='grey.Horizontal.TProgressbar', variable=progr)
bar.grid(column = 0, row = 0)

basket = StringVar()
basket.trace("w", barchange)
lbl1 = Label(window,justify = 'right', text = "Poios einai goat sto basket")
lbl1.grid(column = 1, row = 1)
rad1= Radiobutton(window, text="Michael Jordan", value="Michael Jordan", variable = basket)
rad1.grid(column = 1, row = 2, padx = 10, sticky = "w")
rad2= Radiobutton(window, text="Lebron James", value="Lebron James", variable = basket)
rad2.grid(column = 2, row = 2, padx = 10, sticky = "w")
rad3= Radiobutton(window, text="Timwros", value="Timwros", variable = basket)
rad3.grid(column = 3, row = 2, padx = 10, sticky = "w")

omada = StringVar()
omada.trace("w", barchange)
lbl2 = Label(window,justify = 'right', text = "Poia einai i kaliteri omada")
lbl2.grid(column = 1, row = 4)
rad4= Radiobutton(window, text="Gayroi", value="Gayroi", variable = omada)
rad4.grid(column = 1, row = 5, padx = 10, sticky = "w")
rad5= Radiobutton(window, text="Vazelia", value="Vazelia", variable = omada)
rad5.grid(column = 2, row = 5, padx = 10, sticky = "w")
rad6= Radiobutton(window, text="Kolopetinitsa", value="Kolopetinitsa", variable = omada)
rad6.grid(column = 3, row = 5, padx = 10, sticky = "w")

insta = StringVar()
insta.trace("w", barchange)
lbl3 = Label(window,justify = 'right', text = "Poios exei toys perissoteroys followers")
lbl3.grid(column = 1, row = 7)
rad7= Radiobutton(window, text="paobc", value="paobc", variable = insta)
rad7.grid(column = 1, row = 8, padx = 10, sticky = "w")
rad8= Radiobutton(window, text="aekfc", value= "aekfc", variable = insta)
rad8.grid(column = 2, row = 8, padx = 10, sticky = "w")
rad9= Radiobutton(window, text="olympiacosfc", value="olympiacosfc", variable = insta)
rad9.grid(column = 3, row = 8, padx = 10, sticky = "w")

console = StringVar()
console.trace("w", barchange)
lbl4 = Label(window,justify = 'right', text = "Poia consola einai i kaliteri")
lbl4.grid(column = 1, row = 10)
rad10= Radiobutton(window, text="Ps5", value= "Ps5", variable=console)
rad10.grid(column = 1, row = 11, padx = 10, sticky = "w")
rad11= Radiobutton(window, text="Xbox", value="Xbox", variable=console)
rad11.grid(column = 2, row = 11, padx = 10, sticky = "w")
rad12= Radiobutton(window, text="Pc", value="Pc", variable=console)
rad12.grid(column = 3, row = 11, padx = 10, sticky = "w")

window.mainloop()
