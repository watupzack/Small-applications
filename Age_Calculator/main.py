import calendar
import tkinter
from datetime import date
from tkinter import ttk


def calculate_age():
    name_value = name_entry.get()
    year_value = year_entry.get()
    month_value = month_entry.get()
    day_value = day_entry.get()

    if name_value != "" and year_value != "" and month_value != "" and day_value != "":
        name_value = name_entry.get()
        year_value = int(year_entry.get())
        month_value = int(month_entry.get())
        day_value = int(day_entry.get())

        user_year_old = int(today_year) - year_value
        user_month_old = int(today_month) - month_value - 1
        user_day_old = calendar.monthrange(year_value, int(today_month) - 1)[1] + int(today_day) - day_value
        if int(user_day_old) > calendar.monthrange(year_value, int(today_month) - 1)[1]:
            user_month_old += 1
            user_day_old = user_day_old - calendar.monthrange(year_value, int(today_month) - 1)[1]

        age = name_value + " is " + str(user_year_old) + " year(s), " + str(user_month_old) + " month(s), " + str(
            user_day_old) + " day(s) old."
        result.set(age)


window = tkinter.Tk()
window.title("Age Calculator")
window.geometry("250x210")
window.resizable(False, False)
result = tkinter.StringVar()
main_frame = tkinter.Frame(window)

today = date.today().strftime("%Y/%m/%d")
today_year = today[:4]
today_month = today[5:7]
if today_month[0] == "0":
    today_month = today_month[1]
today_day = today[8:10]
if today_day[0] == "0":
    today_day = today_day[1]

name_label = ttk.Label(main_frame, text='Name')
year_label = ttk.Label(main_frame, text='Year')
month_label = ttk.Label(main_frame, text='Month')
day_label = ttk.Label(main_frame, text='Day')
age_label = ttk.Label(window, textvariable=result)
name_entry = ttk.Entry(main_frame)
year_entry = ttk.Entry(main_frame)
month_entry = ttk.Entry(main_frame)
day_entry = ttk.Entry(main_frame)
calculate_button = ttk.Button(window, text="Calculate Age", command=calculate_age)

name_label.grid(row=0, column=0)
year_label.grid(row=1, column=0)
month_label.grid(row=2, column=0)
day_label.grid(row=3, column=0)
name_entry.grid(row=0, column=1)
year_entry.grid(row=1, column=1)
month_entry.grid(row=2, column=1)
day_entry.grid(row=3, column=1)

main_frame.pack(pady=20)
age_label.pack()
calculate_button.pack(pady=20)

window.mainloop()
