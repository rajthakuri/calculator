from tkinter import * #importing tkinter

root = Tk()  #making a root window with Tk method of tkinter
root.geometry("250x400+100+100") #making the window of size 250x400 and shifiting its position on screen to 300 on x and y axis
root.resizable(0,0) #making the window not resizable
root.title("Calculator") #adding the title of window as Calculator

val = ""

data = StringVar()

def clicked(num):
    global val
    val = val + str(num)
    data.set(val)

def delete():
    global val
    val = ""
    data.set(val)

def result():
    global val
    try:
        result = eval(val)
        data.set(result)
    except:
        data.set('Error')

lbl = Label(
    root,
    font = ('Hobo', 20),
    anchor=SE,
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both")

# the frames section
btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")


# The buttons section
btn7 = Button(
    btnrow1,
    text = "7",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(7),
)
btn7.pack(side = LEFT, expand = True, fill = "both",)

btn8 = Button(
    btnrow1,
    text = "8",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(8),
)
btn8.pack(side = LEFT, expand = True, fill = "both",)

btn9 = Button(
    btnrow1,
    text = "9",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(9),
)
btn9.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(
    btnrow1,
    text = "+",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda:clicked("+"),
)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# buttons for frame 2

btn4 = Button(
    btnrow2,
    text = "4",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(4),
)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(
    btnrow2,
    text = "5",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(5),
)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(
    btnrow2,
    text = "6",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(6),
)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(
    btnrow2,
    text = "-",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda:clicked("-"),
)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

# button for frame 3

btn1= Button(
    btnrow3,
    text = "1",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(1),
)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(
    btnrow3,
    text = "2",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(2),
)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3= Button(
    btnrow3,
    text = "3",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(3),
)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnmult = Button(
    btnrow3,
    text = "*",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda:clicked("*"),
)
btnmult.pack(side = LEFT, expand = True, fill = "both",)

btnc = Button(
    btnrow4,
    text = "C",
    font = ('Hobo', 22),
    relief = GROOVE,
    bg="#9c880b",
    border = 0,
    command = delete,
)
btnc.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(
    btnrow4,
    text = "0",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda: clicked(0),
)
btn0.pack(side = LEFT, expand = True, fill = "both",)

btnequal = Button(
    btnrow4,
    text = "=",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both",)

btndiv = Button(
    btnrow4,
    text = "/",
    font = ('Hobo', 22),
    relief = GROOVE,
    border = 0,
    command = lambda:clicked("/"),
)
btndiv.pack(side = LEFT, expand = True, fill = "both",)

root.mainloop()