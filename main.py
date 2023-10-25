from tkinter import *
import math
#CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps=0
timer=None
frequency = 2500
duration = 1000
# TIMER RESET
def reset_timer():
    window.after_cancel(timer)
    label.config(text="TIMER",font=(FONT_NAME,50,"normal"),bg=YELLOW,fg=GREEN)
    check_mark.config(text="")
    canvas.itemconfigure(text,text="00:00")
    global reps
    reps=0
#TIMER MECHANISM
def start_timer():
    global reps
    reps+=1
    work_secs=WORK_MIN*60
    short_break_secs=SHORT_BREAK_MIN*60
    long_break_secs=LONG_BREAK_MIN*60
    if reps%8==0:
        window.bell()
        window.attributes('-topmost', 1)
        count_down(long_break_secs)
        label.config(text="Break ☕️",fg=RED)
    elif reps%2==0:
        window.bell()
        window.attributes('-topmost', 1)
        count_down(short_break_secs)
        label.config(text="Break ☕️", fg=PINK)
    else:
        window.attributes('-topmost', 0)
        count_down(work_secs)
        label.config(text="WORK!", fg=GREEN)

#COUNTDOWN MECHANISM
def count_down(count):
    mark=""
    count_min=math.floor(count/60)
    count_second=count%60
    if count_second<10:
        count_second=f"0{count_second}"
    canvas.itemconfigure(text,text=f"{count_min}:{count_second}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        global reps
        for _ in range(math.floor(reps/2)):
            mark+="✔"
        check_mark.config(text=mark)
#UI SETUP
window=Tk()
window.title("Pomodoro")
window.minsize(width=500,height=400)
window.config(padx=100,pady=50,bg=YELLOW)
tomato_img=PhotoImage(file="tomato.png")

label=Label(text="TIMER",font=(FONT_NAME,50,"normal"),bg=YELLOW,fg=GREEN)
label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

start_button=Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0,row=2)
reset_button=Button(text="Reset",command=reset_timer,highlightthickness=0)
reset_button.grid(column=2,row=2)
check_mark=Label(font=(FONT_NAME,30,"normal"),bg=YELLOW,fg=GREEN)
check_mark.grid(column=1,row=3)
window.mainloop()