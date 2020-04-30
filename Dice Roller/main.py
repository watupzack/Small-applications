import tkinter, random

def throw_dice():
    global first_cube, second_cube
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)

    first_cube["file"] = "dices/dice{0}.png".format(first_dice)
    second_cube["file"] = "dices/dice{0}.png".format(second_dice)

window = tkinter.Tk()
window.resizable(width=False, height=False)

canvas = tkinter.Canvas(window, width=90, height=80)
first_cube = tkinter.PhotoImage(file="dices/dice1.png")
second_cube = tkinter.PhotoImage(file="dices/dice1.png")
canvas.create_image(20, 40, image=first_cube)
canvas.create_image(70, 40, image=second_cube)
canvas.pack()

throw_dice_button = tkinter.Button(window, text="Throw dice", command=throw_dice)
throw_dice_button.pack()

window.mainloop()
