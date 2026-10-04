from tkinter import *
from tkinter.messagebox import showwarning,showinfo
#---------------------------Tic Tac Toe-----------------------------
#              status:incomplete
root =Tk()
root.geometry("500x470")
root.title("Tic Tac Toe")
#--------variables--------
sec=0
el=range(0,3)
clicks=0
tries=1
board=[
    ["","",""],
    ["","",""],
    ["","",""]
]
reb=[
    ["","",""],
    ["","",""],
    ["","",""]
]
xo={'X':'O','O':'X'}
win_count={"X":0,"O":0}
#-------------------------
#--------Functions--------

def if_Won(ply):
    global el,board,clicks,tries
    check=0
    if True in [(board[i].count(ply)==3) for i in el]:
        check+=1
    elif (board[0][2]==board[1][1]==board[2][0]==ply)or(board[0][0]==board[1][1]==board[2][2]==ply):
        check+=1
    elif (board[0][0]==board[1][0]==board[2][0]==ply)or(board[0][1]==board[1][1]==board[2][1]==ply)or(board[0][2]==board[1][2]==board[2][2]==ply):
        check+=1
    if check:
        turn_of_player["text"]=""
        return True
    else:
        return False

def if_Full():
    global board,tries
    if not any(("" in board[i])for i in el):
        board=reb
        tries+=1
        b00["text"]=""
        b01["text"]=""
        b02["text"]=""
        b10["text"]=""
        b11["text"]=""
        b12["text"]=""
        b20["text"]=""
        b21["text"]=""
        b22["text"]=""
def timr():
    global sec
    timer['text']=f"{sec//3600}:{sec//60}:{sec}"
    sec+=1
    timr()

def turn():
    global clicks
    if clicks%2==0:
        return "X"
    else:
        return "O"

def button_check(btuon):
    if not btuon["text"]=="":
        showwarning(title="Warning !",message="ILLEGAL MOVE")
        return False
    return True



def button_clicked(bton,a,b):
    global clicks,board,tries,xo,win_count
    if button_check(bton):
        trn=turn()
        turn_of_player["text"]=f"{xo[trn]}'s TURN"
        bton["text"]=trn
        board[a][b]=trn
        clicks+=1
        if_Full()
        if if_Won(trn):
            b00["text"]=""
            b01["text"]=""
            b02["text"]=""
            b10["text"]=""
            b11["text"]=""
            b12["text"]=""
            b20["text"]=""
            b21["text"]=""
            b22["text"]=""
            showinfo(title="GAME ENDED",message=f"{trn} WON!!\nTries : {tries}")
            win_count[trn]+=1
            player_win_count['text']=f"X:{win_count["X"]}\nO:{win_count['O']}"
            clicks=0
            tries=1
            board=[
                ["","",""],
                ["","",""],
                ["","",""]
            ]
#-------------------------
#---------Labels----------
turn_of_player=Label(root,text="",font=("Ariel",16),pady=20)
title=Label(root,text="TIC TAC TOE",font=("Ariel",14))
timer=Label(root,font=("Ariel",12),padx=15)
player_win_count=Label(root,text=f"X:{win_count["X"]}\nO:{win_count['O']}",font=("Ariel",12))
turn_of_player.grid(row=0,column=0)
player_win_count.grid(row=2,column=4)
timer.grid(row=0,column=4)
#-------------------------
#---------buttons---------
b00=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b00,0,0),font=("Calibri",20))
b01=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b01,0,1),font=("Calibri",20))
b02=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b02,0,2),font=("Calibri",20))
b10=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b10,1,0),font=("Calibri",20))
b11=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b11,1,1),font=("Calibri",20))
b12=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b12,1,2),font=("Calibri",20))
b20=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b20,2,0),font=("Calibri",20))
b21=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b21,2,1),font=("Calibri",20))
b22=Button(root,text="",bg="#86838a",width=7,height=3,command=lambda:button_clicked(b22,2,2),font=("Calibri",20))
b00.grid(row=1,column=0)
b01.grid(row=1,column=1)
b02.grid(row=1,column=2)
b10.grid(row=2,column=0)
b11.grid(row=2,column=1)
b12.grid(row=2,column=2)
b20.grid(row=3,column=0)
b21.grid(row=3,column=1)
b22.grid(row=3,column=2)
#-------------------------
root.mainloop()
#-------------------------------------------------------------------