import random
import tkinter


def throw_dice():
    global first_dice, second_dice
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    btn_color = "#%02x%02x%02x" % (r, g, b)
    throw_dice_button["bg"] = btn_color
    first_cube["file"] = f"dices/dice{first_dice}.png"
    second_cube["file"] = f"dices/dice{second_dice}.png"


window = tkinter.Tk()
window.title("DR")
window.geometry("150x100")
window.resizable(width=False, height=False)
main_frame = tkinter.Frame(window)
first_cube = tkinter.PhotoImage(file="dices/dice1.png")
second_cube = tkinter.PhotoImage(file="dices/dice1.png")
first_dice = tkinter.Label(main_frame, image=first_cube)
second_dice = tkinter.Label(main_frame, image=second_cube)
throw_dice_button = tkinter.Button(main_frame, padx=2, pady=3, text="Throw dice",
                                   relief="solid", bd=1, command=throw_dice,
                                   font="Verdana 10 bold")

first_dice.grid(row=0, column=0)
second_dice.grid(row=0, column=1)
throw_dice_button.grid(row=1, columnspan=2)
main_frame.pack(pady=(5, 0))

window.mainloop()
