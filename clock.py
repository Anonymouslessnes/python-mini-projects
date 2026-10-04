from time import *
from tkinter import *
window=Tk()

window.geometry("800x120")
window.title("CLOCK")

def update():
    timelabel.config(text=(strftime("%A - %d %b\n%I :%M .%S %p").upper()))
    timelabel.after(20,update)

timelabel=Label(window,text='',font=("gaia display",40),bg="#B5B5B5")
timelabel.pack()
update()
window.mainloop()

#Commonly used format codes:
# %Y Year with century as a decimal number.
# %m Month as a decimal number [01,12].
# %d Day of the month as a decimal number [01,31].
# %H Hour (24-hour clock) as a decimal number [00,23].
# %M Minute as a decimal number [00,59].
# %S Second as a decimal number [00,61].
# %z Time zone offset from UTC.
# %a Locale's abbreviated weekday name.
# %A Locale's full weekday name.
# %b Locale's abbreviated month name.
# %B Locale's full month name.
# %c Locale's appropriate date and time representation.
# %I Hour (12-hour clock) as a decimal number [01,12].
# %p Locale's equivalent of either AM or PM.