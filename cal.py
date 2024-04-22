from tkinter import * 
window=Tk()
window.geometry("500x500")
def add():
    sum=int(e1.get())+int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(sum))

def sub():
    diff=int(e1.get())-int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(diff))

def mul():
    prod=int(e1.get())*int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(prod))

def div():
    div=int(e1.get())/int(e2.get())
    e3.delete(0,END)
    e3.insert(0,str(div))
    
l1=Label(window,text="Calculator",font=("Arial",18)) 
l1.place(x=200,y=30)
l2=Label(window,text="Type Value 1:",font=("Arial",13)) 
l2.place(x=100,y=120)
l3=Label(window,text='Type Value 2:',font=('Arial',13))
l3.place(x=100,y=150)
l4=Label(window,text='Result:',font=('Arial',14))
l4.place(x=120,y=350)
e1=Entry(window,textvariable=IntVar)
e1.place(x=225,y=122)
e2=Entry(window,textvariable=IntVar)
e2.place(x=225,y=152)
e3=Entry(window)
e3.place(x=225,y=355)
b1=Button(window,text='+',bg='green',command=add)
b1.grid(ipadx=20,ipady=5,row=0,column=0,padx=50,pady=250)
b2=Button(window,text='-',bg='green',command=sub)
b2.grid(ipadx=20,ipady=5,row=0,column=1,padx=10,pady=10)
b3=Button(window,text='x',bg='green',command=mul)
b3.grid(ipadx=20,ipady=5,row=0,column=2,padx=40)
b4=Button(window,text='/',bg='green',command=div)
b4.grid(ipadx=20,ipady=5,row=00,column=3)
window.mainloop()