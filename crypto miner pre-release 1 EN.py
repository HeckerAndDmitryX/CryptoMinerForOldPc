from tkinter import *
from tkinter.ttk import Combobox
import random


window1=Tk()
window1.title('registration')
window1.geometry('400x300')
window1.resizable(False, False)


def clicked():
    print("+0.00001 BTC")
def click1():
    n=10000000000000000000000000
    while n>0:
        n-=1 
        print("+0.000000001 BTC")
        
def click2():
    
    window2=Tk()
    window2.title("crypto miner pre-release 1")
    window2.geometry('384x166')
    window2.resizable(False, False)

    
    lbl4=Label(window2, text='Start mining bitcoin now!', font=font_header2
               , justify=CENTER, **header_padding2)
    lbl4.grid(column=0,row=0)

    
    btn2=Button(window2,text=' auto  ',command=click1,fg='black',
               bg='green',activebackground='red',
               activeforeground='white',padx=30)
    btn2.grid(column=0,row=2)

    
    btn3=Button(window2,text='clicker',command=clicked,fg='black',
               bg='green',activebackground='green',
               activeforeground='black',padx=30)
    btn3.grid(column=0,row=1)
    window2.mainloop()


font_header=('Arial',15)
font_header2=('Arial',18)
font_entry=('Arial',12)
label_font=('Arial',11)
base_padding={'padx':10, 'pady':8}
header_padding={'padx':10, 'pady':12}
header_padding2={'padx':63, 'pady':12}


lbl1=Label(window1, text='Registration', font=font_header, justify=CENTER, **header_padding)
lbl1.pack()
lbl2=Label(window1, text='Username', font=label_font , **base_padding)
lbl2.pack()


username=Entry(window1, bg='#fff', fg='#444', font=font_entry)
username.pack()


lbl3=Label(window1, text='Password', font=label_font , **base_padding)
lbl3.pack()


password=Entry(window1, bg='#fff', fg='#444', font=font_entry)
password.pack()


btn=Button(window1, text='Register', command=click2)
btn.pack(**base_padding)
window1.mainloop()
