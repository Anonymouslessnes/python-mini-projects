from tkinter import *
from time import sleep
window=Tk()
window.geometry("400x200")
window.title("timer")
n=0
run=False

l1=Label(window,font=("consolas",16),height=6,width=12)
l1.pack()


def update():
    global n , run
    if run:
        l1.config(text=f"{(n//3600):02}:{(n//60)%60:02}:{(n%60):02}")
        n+=1
        l1.after(1000,update)

def buttonclick():
    global run
    if button['text']=='START':
        run=True
        button.config(text="STOP")
        sleep(1)
        update()
    else:
        run=False
        button.config(text="START")

button=Button(window,text="START",font=("Consolas",18),height=3,width=6,command=buttonclick)
button.pack()

window.mainloop()