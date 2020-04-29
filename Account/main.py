import tkinter

temp_account = []

file = open('moneyData.txt', 'r')
for line in file:
    # remove linebreak which is the last character of the string
    currentCurrency = float(line.replace("\n", ""))
    # add item to the list
    temp_account.append(currentCurrency)
file.close()

account =  {"MDL": 0, "EUR": 0, "USD": 0, "RON": 0, "UAH": 0}
account["MDL"] = temp_account[0]
account["EUR"] = temp_account[1]
account["USD"] = temp_account[2]
account["RON"] = temp_account[3]
account["UAH"] = temp_account[4]

window = tkinter.Tk()

def update_balance():
    global entry_mdl, entry_eur, entry_usd, entry_ron, entry_uah, \
           label_mdl, label_eur, label_usd, label_ron, label_uah, \
           mdl_amount, eur_amount, usd_amount, ron_amount, uah_amount, account

    entry_mdl_input = entry_mdl.get()
    entry_eur_input = entry_eur.get()
    entry_usd_input = entry_usd.get()
    entry_ron_input = entry_ron.get()
    entry_uah_input = entry_uah.get()

    if entry_mdl_input:
        account["MDL"] = eval(str(account["MDL"]) + entry_mdl_input[0] + str(float(entry_mdl_input[1:])))
    if entry_eur_input:
        account["EUR"] = eval(str(account["EUR"]) + entry_eur_input[0] + str(float(entry_eur_input[1:])))
    if entry_usd_input:
        account["USD"] = eval(str(account["USD"]) + entry_usd_input[0] + str(float(entry_usd_input[1:])))
    if entry_ron_input:
        account["RON"] = eval(str(account["RON"]) + entry_ron_input[0] + str(float(entry_ron_input[1:])))
    if entry_uah_input:
        account["UAH"] = eval(str(account["UAH"]) + entry_uah_input[0] + str(float(entry_uah_input[1:])))

    mdl_amount.set("\nMDL" + "\n\n" + str(account["MDL"]))
    eur_amount.set("\nEUR" + "\n\n" + str(account["EUR"]))
    usd_amount.set("\nUSD" + "\n\n" + str(account["USD"]))
    ron_amount.set("\nRON" + "\n\n" + str(account["RON"]))
    uah_amount.set("\nUAH" + "\n\n" + str(account["UAH"]))

    file = open("moneyData.txt", "w")
    file.write("\n".join((str(account["MDL"]), str(account["EUR"]), str(account["USD"]), str(account["RON"]), str(account["UAH"]))))
    file.close()


mdl_amount = tkinter.StringVar()
eur_amount = tkinter.StringVar()
usd_amount = tkinter.StringVar()
ron_amount = tkinter.StringVar()
uah_amount = tkinter.StringVar()

mdl_amount.set("\nMDL" + "\n\n" + str(account["MDL"]))
eur_amount.set("\nEUR" + "\n\n" + str(account["EUR"]))
usd_amount.set("\nUSD" + "\n\n" + str(account["USD"]))
ron_amount.set("\nRON" + "\n\n" + str(account["RON"]))
uah_amount.set("\nUAH" + "\n\n" + str(account["UAH"]))

main_frame = tkinter.Frame(window)

label_mdl = tkinter.Label(main_frame, textvariable=mdl_amount)
label_eur = tkinter.Label(main_frame, textvariable=eur_amount)
label_usd = tkinter.Label(main_frame, textvariable=usd_amount)
label_ron = tkinter.Label(main_frame, textvariable=ron_amount)
label_uah = tkinter.Label(main_frame, textvariable=uah_amount)

entry_mdl = tkinter.Entry(main_frame)
entry_eur = tkinter.Entry(main_frame)
entry_usd = tkinter.Entry(main_frame)
entry_ron = tkinter.Entry(main_frame)
entry_uah = tkinter.Entry(main_frame)

submit = tkinter.Button(main_frame, text="SUBMIT", fg="red", command=update_balance)

main_frame.grid(row=0, column=0)

submit.grid(row=2, columnspan=5, sticky=tkinter.W+tkinter.E)

label_mdl.grid(row=0, column=0, pady=10)
label_eur.grid(row=0, column=1)
label_usd.grid(row=0, column=2)
label_ron.grid(row=0, column=3)
label_uah.grid(row=0, column=4)

entry_mdl.grid(row=1, column=0, padx=20, pady=20)
entry_eur.grid(row=1, column=1, padx=20, pady=20)
entry_usd.grid(row=1, column=2, padx=20, pady=20)
entry_ron.grid(row=1, column=3, padx=20, pady=20)
entry_uah.grid(row=1, column=4, padx=20, pady=20)


window.mainloop()
