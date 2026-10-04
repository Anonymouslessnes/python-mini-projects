from string import ascii_letters,punctuation,digits
from random import choices
from csv import *
def pswd(size:int):
    characters=ascii_letters+punctuation+digits
    passwd = ''.join(choices(characters,k=size))
    print(f'Your password !!: {passwd} ')
    label=input("Enter label (Ex :Instagram, Google, Reddit)\n:")
    with open('password/password.csv','a+',newline='') as file:
        w=writer(file)
        w.writerow([label,passwd])
        print("Password saved !!")

pswd(int(input('Enter password size (>8):')))