from tkinter import Tk,Label,Entry,Button,END,IntVar,StringVar
from tkinter.messagebox import showerror

root=Tk()
root.title("Cipher-Decipher")
root.geometry("460x200")
root.config(bg="#cccccc",relief="sunken")
PlainText=StringVar(root)
CipherText=StringVar(root)
shiftInput=IntVar(root)

Label(master=root,text="PlainText :",font="Ariel,15",bg="#cccccc").grid(column=0,row=0,ipadx=30,ipady=10)
Entry(master=root,font="Ariel,15",textvariable=PlainText,width=20,borderwidth=5).grid(column=1,row=0)

Button(master=root,command=lambda:textToCipher(PlainText.get()),text="String To Cipher",font="Ariel,15").grid(column=0,row=1,padx=10)
Button(master=root,command=lambda:cipherToText(CipherText.get()),text="Cipher To String",font="Ariel,15").grid(column=1,row=1,padx=10)

Label(master=root,text="CipherText :",font="Ariel,15",bg="#cccccc").grid(column=0,row=2,ipadx=30,ipady=10)
Entry(master=root,font="Ariel,15",textvariable=CipherText,width=20,borderwidth=5).grid(column=1,row=2)

Label(master=root,text="Shift value :",font="Ariel,15",bg="#cccccc").grid(column=0,row=3,ipadx=30,ipady=10)
Entry(master=root,textvariable=shiftInput,font="Ariel,15",width=5,borderwidth=2).grid(column=1,row=3)

def cipherToText(inp):
    try:
        subtract=shiftInput.get()%26
    except ValueError:
        showerror(title="Error",message="Enter the shift value ")
        return
    res=''
    for i in inp:
        if i.isupper():
            res += chr((ord(i) - 65 - subtract) % 26 + 65)
        elif i.islower():
            res += chr((ord(i) - 97 - subtract) % 26 + 97)
        else:
            res+=i
    PlainText.set(res)

def textToCipher(inp):
    try:
        concat=shiftInput.get()%26
    except ValueError:
        showerror(title="Error",message="Enter the shift value ")
        return
    res=''
    for i in inp:
        if i.isupper():
            res += chr((ord(i) - 65 + concat) % 26 + 65)
        elif i.islower():
            res += chr((ord(i) - 97 + concat) % 26 + 97)
        else:
            res+=i
    CipherText.set(res)

root.mainloop()