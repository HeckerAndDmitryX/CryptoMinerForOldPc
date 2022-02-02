print("created by 'HeckerAndDmitryX team' project on github:https://github.com/HeckerAndDmitryX/CryptoMinerForOldPc")
import turtle
turtle. color('yellow')
turtle. write('BitcoinMinerForOldPC')
from tkinter import*
import random
def clicked():
    print("+0.00001 BTC")
def click():
    n=1000000000000000000
    while n>0:
        n-=1 
        print("+0.000000001 BTC")
    
window=Tk()
window.title("crypto miner")
window.geometry('192x108')
lbl=Label(window,text="начни майнить биткоин сейчас!",font=("Arial",10))
lbl.grid(column=0,row=0)
btn1=Button(window,text='автомат',command=click,fg='black',
           bg='green',activebackground='red',
           activeforeground='white',padx=14)
btn1.grid(column=0,row=2)
btn2=Button(window,text='кликер ',command=clicked,fg='black',
           bg='green',activebackground='green',
           activeforeground='black',padx=15)
btn2.grid(column=0,row=1)
window.mainloop()
