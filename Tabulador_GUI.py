###### Bibliotecas ######
import tkinter as tk
from tkinter import ttk
from tkinter import *
import getpass
from tkinter import messagebox

###### Parameters ######
db = 'db_cadastro_contas.db'
login_user = getpass.getuser()
#Styles
l=('Consolas',12)
t=('Courier New',18)

###### Config. App ######
app=tk.Tk()
app.title(' L O G I N ')
app.geometry('350x550')
app.resizable(0,0)

###### Functions ######
j=0
r=10
for i in range(100):
    c=str(222222+r)
    Frame(app,width=10,height=550,bg="#"+c).place(x=j,y=0)   
    j=j+10                                                  
    r=r+1

Frame(app,width=250,height=450,bg='white').place(x=50,y=50)

def log_in():
    messagebox.showwarning("Information", "Developing")

def new_frame(): #Developing, 
    app2 = tk.Toplevel()
    app2.title('S I G N - U P')
    app2.geometry('350x550')
    app2.resizable(0,0)
    
    j=0
    r=10
    for i in range(100):
        c=str(222222+r)
        Frame(app2,width=10,height=550,bg="#"+c).place(x=j,y=0)   
        j=j+10                                                  
        r=r+1
    
    Frame(app2,width=250,height=450,bg='white').place(x=50,y=50)
    
    #Title
    t1 = tk.Label(app2,text='S I G N - U P',bg='white')
    t1.config(font=t)
    t1.place(x=80,y=80)
    
    '''t1 = tk.Label(app2,text='Username',bg='white')
    t1.config(font=l)
    t1.place(x=80,y=150)

    r1=Entry(app2,width=20,border=0)
    r1.config(font=l)
    r1.place(x=80,y=180)
    Frame(app2,width=180,height=2,bg='#141414').place(x=80,y=202)

    #Password
    t2 = tk.Label(app2,text='Password',bg='white')
    t2.config(font=l)
    t2.place(x=80,y=230)

    r2=Entry(app2,width=20,border=0)
    r2.config(font=l)
    r2.place(x=80,y=260)
    Frame(app2,width=180,height=2,bg='#141414').place(x=80,y=282)

    ###### Botão ######
    botao_tabular = tk.Button(app2,text='L O G I N',width=20,height=1,bg='white')
    botao_tabular.place(x=93,y=320)

    Frame(app2,width=180,height=1,bg='#141414').place(x=80,y=380)'''
    
    app2.grab_set()
    
    app2.mainloop()

#Title
l1 = tk.Label(app,text='L O G - I N',bg='white')
l1.config(font=t)
l1.place(x=90,y=80)

#Username
l1 = tk.Label(app,text='Username',bg='white')
l1.config(font=l)
l1.place(x=80,y=150)

e1=Entry(app,width=20,border=0)
e1.config(font=l)
e1.place(x=80,y=180)
Frame(app,width=180,height=2,bg='#141414').place(x=80,y=202)

#Password
l2 = tk.Label(app,text='Password',bg='white')
l2.config(font=l)
l2.place(x=80,y=230)

e2=Entry(app,width=20,border=0)
e2.config(font=l)
e2.place(x=80,y=260)
Frame(app,width=180,height=2,bg='#141414').place(x=80,y=282)

###### Botão ######
botao_tabular = tk.Button(app,text='L O G I N',width=20,height=1,bg='white',command=log_in)
botao_tabular.place(x=95,y=320)

l2 = tk.Label(app,text="Don't have an account?",bg='white')
l2.config(font=('Consolas',9))
l2.place(x=90,y=380)
Frame(app,width=180,height=1,bg='#141414').place(x=80,y=403)

botao_cadastro = tk.Button(app,text='S I G N - U P',width=20,height=1,bg='white',command=new_frame)
botao_cadastro.place(x=95,y=430)

app.mainloop()