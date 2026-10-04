from tkinter import *

actual=Tk()
main=Toplevel()
actual.config(bg="#000000")
actual.withdraw()
e=Entry(main,width=10,font=('Ariel',15))
e.pack(side="left")
start=250
Str=''
pos=0
var=''
def Textfx():
    global start,Str,pos 
    if pos>=len(var):
        actual.after(5000,actual.destroy)
        return
    if start==ord(var[pos]):
        start=250
        Str+=var[pos]
        pos+=1
        if pos>=len(var):
            cool_Text.set(Str)
            actual.after(5000,actual.destroy)
            return
    cool_Text.set(Str+chr(start))
    start-=1
    actual.after(10,Textfx)

def run():
    global var
    var=e.get()
    main.destroy()
    width=max(400,len(var)*30)
    actual.geometry(f'{width}x100')
    actual.deiconify()
    Textfx()
cool_Text=StringVar(actual)
Label(actual,textvariable=cool_Text,bg="#000000",fg="#ff0000",font=('OCR A Extended',45)).pack(anchor='center')
Button(main,text='Click me ! ',width=7,height=2,command=run).pack(side='right')
actual.mainloop()