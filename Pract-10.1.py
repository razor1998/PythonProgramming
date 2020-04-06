from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Registration Form")


sname=StringVar()
suid=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=sname.get()
   useri=suid.get()
   gender=var.get()
   if(gender == 1):
      n_gender='Male'
   else:
      n_gender='Female'
   stream=c.get()
   sttp=var1.get()
   if(sttp == 1):
      stype='Hosteller'
   else:
      stype='Non-Hosteller'
   conn = sqlite3.connect('stdb.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (name TEXT,userid TEXT,Gender TEXT,stream TEXT,stype TEXT)')
   cursor.execute('INSERT INTO Student (name,userid,Gender,stream,stype) VALUES(?,?,?,?,?)',(name1,useri,n_gender,stream,stype))
   conn.commit()
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=sname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="UID",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=suid)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Stream",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['BCA','MCA','BTECH','MTECH','BBA','MBA'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your stream') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Student-Type",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text="Hosteller", variable=var1).place(x=235,y=330)

Checkbutton(root, text="Non-Hosteller", variable=var2).place(x=320,y=330)

Button(root, text='Submit',width=20,fg='black',command=database).place(x=180,y=380)

root.mainloop()
