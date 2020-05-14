import random
import tkinter


def reset():
    player_score.set("Player\n0")
    computer_score.set("Computer\n0")
    game_progress.set("")


def button_clicked(player_choice):
    computer_choice = computer_options[random.randint(0, 2)]
    if player_choice == "Rock":
        if computer_choice == "Rock":
            game_progress.set("Draw")
        elif computer_choice == "Paper":
            game_progress.set("Rock    vs    Paper\nPaper wins")
            computer_score.set("Computer\n" + str(int(computer_score.get()[9:]) + 1))
        elif computer_choice == "Scissors":
            game_progress.set("Rock    vs    Scissors\nRock wins")
            player_score.set("Player\n" + str(int(player_score.get()[7:]) + 1))
    elif player_choice == "Paper":
        if computer_choice == "Rock":
            game_progress.set("Paper    vs    Rock\nPaper wins")
            player_score.set("Player\n" + str(int(player_score.get()[7:]) + 1))
        elif computer_choice == "Paper":
            game_progress.set("Draw")
        elif computer_choice == "Scissors":
            game_progress.set("Paper    vs    Scissors\nScissors win")
            computer_score.set("Computer\n" + str(int(computer_score.get()[9:]) + 1))
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            game_progress.set("Scissors    vs    Rock\nRock wins")
            computer_score.set("Computer\n" + str(int(computer_score.get()[9:]) + 1))
        elif computer_choice == "Paper":
            game_progress.set("Scissors    vs    Paper\nScissors win")
            player_score.set("Player\n" + str(int(player_score.get()[7:]) + 1))
        elif computer_choice == "Scissors":
            game_progress.set("Draw")


window = tkinter.Tk()
window.title("RPS Game")
window.geometry("190x180")
window.resizable(False, False)

button_frame = tkinter.Frame(window)
player_frame = tkinter.Frame(window)

SCISSORS = tkinter.PhotoImage(file="symbols/scissors.png")
PAPER = tkinter.PhotoImage(file="symbols/paper.png")
ROCK = tkinter.PhotoImage(file="symbols/rock.png")
computer_options = ["Rock", "Paper", "Scissors"]
player_score = tkinter.StringVar()
computer_score = tkinter.StringVar()
game_progress = tkinter.StringVar()
player_score.set("Player\n0")
computer_score.set("Computer\n0")

reset_button = tkinter.Button(window, text="Reset", font="bold", command=reset)
button_rock = tkinter.Button(button_frame, image=ROCK, command=lambda: button_clicked("Rock"), bg="dodger blue")
button_paper = tkinter.Button(button_frame, image=PAPER, command=lambda: button_clicked("Paper"), bg="lime green")
button_scissors = tkinter.Button(button_frame, image=SCISSORS, command=lambda: button_clicked("Scissors"),
                                 bg="orange red")

player = tkinter.Label(player_frame, textvariable=player_score)
empty_space = tkinter.Label(player_frame)
computer = tkinter.Label(player_frame, textvariable=computer_score)
game_label = tkinter.Label(window, textvariable=game_progress)

reset_button.pack()
button_rock.grid(row=0, column=0)
button_paper.grid(row=0, column=1)
button_scissors.grid(row=0, column=2)
button_frame.pack(pady=10)
player.grid(row=0, column=0)
empty_space.grid(row=0, column=1, padx=15)
computer.grid(row=0, column=2)
player_frame.pack()
game_label.pack(pady=5)

window.mainloop()
