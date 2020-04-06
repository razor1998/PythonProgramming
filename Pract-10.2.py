from tkinter import *
import sqlite3 as db


def fetchdata():
    conn=db.connect('stdb.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Student")
    list0 = cur.fetchall()
    cur.close()
    conn.close()
    output=''
    for x in list0:
        output = output+'Name'+'   '+'UID'+'    '+'Gender'+' '+'Stream'+'  '+'S-TYPE'+'\n'+x[0]+' '+x[1]+' '+x[2]+'   '+x[3]+'    '+x[4]
    return output

master = Tk()

text = Text(master, height=5, width=40)
text.grid(row=4, columnspan=2)

Button(master, text='Fetch Data', command=lambda: text.insert(END, fetchdata())).grid(row=2, column=0)

mainloop()
