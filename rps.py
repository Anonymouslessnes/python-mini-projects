from tkinter import *
from tkinter.messagebox import showerror,showwarning
from random import choice

game=Tk()
game.geometry("600x400")
game.title("Rock paper scissors")
#----------------------------------------Labels-------------------------------
beat=Label(game,text="",font=("Monospace",16),padx=35,pady=10)
beat.grid(row=3,column=0,columnspan=3, sticky="nsew")
rounds=Label(game,text="",font=("Monospace",16),padx=30,pady=15)
rounds.grid(row=2,column=0,columnspan=3, sticky="nsew")
points=Label(game,text="",font=("Monospace",16),padx=30,pady=10)
points.grid(row=1,column=0,columnspan=3, sticky="nsew")
# ---------------------------------------Variables-----------------------------
sps={"Rock":"scissors","scissors":"paper","paper":"Rock"}
sel=("Rock","paper","scissors")
rps={"Rock":"🪨","scissors":"✂️","paper":"📃"}
Start_is_clicked=False
bot=None
Round=None
playerPoint=None
botPoint=None
currentRound=None
# ---------------------------------------functions------------------------------
def start():
    global botPoint,playerPoint,currentRound,bot
    botPoint=0
    playerPoint=0
    currentRound=1

def clicked_r():
    global Round,beat,Start_is_clicked
    beat["text"]=""
    if (NoR.get())=="":
        showwarning(title="! ! ERRoR ! !",message=f"Cannot start game without entering the Rounds")
        return
    if Start_is_clicked==True:
        showwarning(title="! ! WARNING ! !",message="Game started!!\nCannot enter more than once")
        return
    if int(NoR.get())<3:
        showwarning(title="! ! WARNING ! !",message=f"Minimum Rounds is 3, not {NoR.get()}")
        return
    if int(NoR.get())>31:
        showwarning(title="! ! WARNING ! !",message=f"Maximum Rounds is 30, not {NoR.get()}")
        return
    Round=int(NoR.get())
    Start_is_clicked=True
    Buttonframe.grid(row=5,column=0,columnspan=3,sticky="news")
    start()
    rounds["text"]=f"Round {currentRound} of {Round}"
    points["text"]=f"|Bot points : {botPoint}|\n|Player points : {playerPoint}|"

def gameEnd(winner):
    global botPoint,playerPoint,currentRound,bot,Start_is_clicked,Round,beat
    Buttonframe.grid_forget
    rounds["text"]=""
    beat["text"]=f"Round Ends!\n{winner}"
    Start_is_clicked=False
    bot=None
    Round=None
    playerPoint=None
    botPoint=None
    currentRound=None

def game_start(player):
    global botPoint,playerPoint,points,rounds,beat,bot,currentRound
    if Start_is_clicked==True:
        rounds["text"]=f"Round {currentRound} of {Round}"
        points["text"]=f"|Bot points : {botPoint}|\n|Player points : {playerPoint}|"
        bot=choice(sel)
        if bot==sps[player]:
            playerPoint+=1
            beat["text"]=f"Player's {rps[player]} beats bot's {rps[bot]}"
        elif player==sps[bot]:
            botPoint+=1
            beat["text"]=f"Bot's {rps[player]} beats Player's {rps[bot]}"
        else:
            beat["text"]="Draw"
        if currentRound==Round:
            if botPoint>playerPoint:
                gameEnd("!!! Bot wins !!!")
            elif playerPoint>botPoint:
                gameEnd("!!! Player wins !!!")
            elif botPoint==playerPoint:
                gameEnd("! ! ! Draw ! ! !")
        else:
            currentRound+=1
    else:
        showerror(title="! ! ERRoR ! !",message="Game not started!")

NoR=Entry(game,border=80,borderwidth=5,font=("Monospace",18))
NoR.grid(ipadx=30,ipady=20,row=0,column=0,sticky="news")
SG=Button(game,text="Start\nGame",font=("monospace",10),padx=30,pady=15,command=clicked_r).grid(row=0,column=1)

class ButtonFrame(Frame):
    # """Improved frame for the buttons: padding, responsive columns and a safe
    # behaviour when gameEnd accesses .grid_forget (it was referenced without
    # calling it in the original code)."""
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(padx=6, pady=6, bg=master.cget("bg"))
        for i in range(3):
            self.columnconfigure(i, weight=1)

    def show(self):
        self.grid(row=5, column=0, columnspan=3, sticky="news")

    def hide(self):
        Frame.grid_forget(self)

    def __getattribute__(self, name):
        # If code accesses .grid_forget (without calling it) we execute it
        # immediately to preserve expected behavior in the existing code.
        if name == "grid_forget":
            try:
                Frame.grid_forget(self)
            except Exception:
                pass
            return lambda *a,**k: None
        return object.__getattribute__(self, name)

Buttonframe = ButtonFrame(game)
Button(Buttonframe,text="🪨",width=13,height=4,font=("Monospace",15),bg="#a4a4a4",command=lambda:game_start("Rock")).grid(column=0,row=0)
Button(Buttonframe,text="📃",width=13,height=4,font=("Monospace",15),bg="#a4a4a4",command=lambda:game_start("paper")).grid(column=1,row=0)
Button(Buttonframe,text="✂️",width=13,height=4,font=("Monospace",15),bg="#a4a4a4",command=lambda:game_start("scissors")).grid(column=2,row=0)

game.mainloop()