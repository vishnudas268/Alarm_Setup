import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Digital-7"
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 3
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_task():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 3 == 0:
        count_down(short_break)
    elif reps % 7 == 0:
        count_down(long_break)
    else:
        count_down(work_time)


def reset_task():
    pass


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
window = Tk()
window.title("Work Alarm")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)

converted_time = WORK_MIN * 60


def count_down(count):
    # print(count)
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text_canvas, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #


timer_label = Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=RED, bg=YELLOW)
timer_label.grid(column=1, row=0)

alarm_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 85, image=alarm_image)
timer_text_canvas = canvas.create_text(100, 100, text="00:00", fill="black", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_task)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_task)
reset_button.grid(column=2, row=2)

window.mainloop()
