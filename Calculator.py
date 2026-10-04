from tkinter import *
calcu=Tk()
calcu.title("Simple calculator")
e=Entry(calcu,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=5)
calcu.config(bg='#F7F7F7')
clicked=0
e_click=0
def click(num):
    global e_click
    if e_click:
        e_click-=1
        e.delete(0,END)
    e.insert(END,num)

def equals():
    global e_click
    try:
        e_click+=1
        op=e.get().replace("^","**")
        e.delete(0,END)
        fop=eval(op)
        e.insert(END,str(fop))
    except:
        e.delete(0,END)
        e.insert(END,"Syntax Error ! X _ X")        

def clr():
    c= e.get()
    e.delete(0, END)
    e.insert(0, c[:-1])

def themeChanged():                         #To change Theme
    if themeChange["text"]=="☀️":
        e.config(bg='#232a2e',fg="#e069ed")
        themeChange.config(fg="#E069ED",text="🌙")
        calcu.config(bg="#211925")
        for _ in buttons[0:9]:
            _.config(bg="#2E2C2E",fg='#e069ed')
        for _ in buttons[9:]:
            _.config(bg="#2a242a",fg="#e069ed")

    else:
        e.config(bg="#F7F7F7",fg="#000000")
        themeChange.config(text="☀️")
        calcu.config(bg="#fdebe8")
        for _ in buttons[0:9]:
            _.config(bg="#c3c3c3",fg='#000000')
        for _ in buttons[9:]:
            _.config(bg="#F7F7F7",fg="#000000")

add=Button(calcu,text="+",padx=22,pady=20,command=lambda:click("+"))
add.grid(row=3,column=3)
divide=Button(calcu,text="/",padx=22,pady=20,command=lambda:click("/"))
divide.grid(row=2,column=4)
multiply=Button(calcu,text="*",padx=24,pady=20,command=lambda:click("*"))
multiply.grid(row=2,column=3)
subtract=Button(calcu,text="-",padx=22,pady=20,command=lambda:click("-"))
subtract.grid(row=3,column=4)
equal=Button(calcu,text="=",width=15,height=3,command=equals)
equal.grid(row=4,column=3,columnspan=2,sticky='nwse')


one=Button(calcu,bg="#c3c3c3",text="1",padx=22,pady=20,command=lambda:click("1"))
one.grid(row=4,column=0)
two=Button(calcu,bg="#c3c3c3",text="2",padx=22,pady=20,command=lambda:click("2"))
two.grid(row=4,column=1)
three=Button(calcu,bg="#c3c3c3",text="3",padx=22,pady=20,command=lambda:click("3"))
three.grid(row=4,column=2)
four=Button(calcu,bg="#c3c3c3",text="4",padx=22,pady=20,command=lambda:click("4"))
four.grid(row=3,column=0)
five=Button(calcu,bg="#c3c3c3",text="5",padx=22,pady=20,command=lambda:click("5"))
five.grid(row=3,column=1)
six=Button(calcu,bg="#c3c3c3",text="6",padx=22,pady=20,command=lambda:click("6"))
six.grid(row=3,column=2)
seven=Button(calcu,bg="#c3c3c3",text="7",padx=22,pady=20,command=lambda:click("7"))
seven.grid(row=2,column=0)
eight=Button(calcu,bg="#c3c3c3",text="8",padx=22,pady=20,command=lambda:click("8"))
eight.grid(row=2,column=1)
nine=Button(calcu,bg="#c3c3c3",text="9",padx=22,pady=20,command=lambda:click("9"))
nine.grid(row=2,column=2)
zero=Button(calcu,text="0",padx=21,pady=20,command=lambda:click("0"))
zero.grid(row=1,column=0)
dot=Button(calcu,text=".",padx=24,pady=20,command=lambda:click("."))
dot.grid(row=1,column=1)
pow=Button(calcu,text="x^y",padx=20,pady=20,command=lambda:click("^"))
pow.grid(row=1,column=2)
ce=Button(calcu,text="CE",padx=20,pady=20,command=lambda:e.delete(0,END))
ce.grid(row=1,column=3)
clr=Button(calcu,text="<xI",padx=20,pady=20,command=clr)
clr.grid(row=1,column=4,columnspan=2)
themeChange=Button(calcu,text='☀️',width=2,command=themeChanged)
themeChange.grid(row=0,column=5,sticky='e',ipadx=3)
buttons=[one,two,three,four,five,six,seven,eight,nine,zero,themeChange,dot,ce,clr,pow,equal,subtract,add,multiply,divide]
calcu.mainloop()