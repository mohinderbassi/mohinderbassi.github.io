from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():
    id = e_id.get();
    name = e_name.get();
    phone = e_phone.get();

    if(id=="" or name=="" or phone==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host="localhost", user="root", password="1513", database="pydbtkinter")
        cursor = con.cursor()
        cursor.execute("insert into student values('"+ id +"','"+ name +"','"+ phone +"')")
        cursor.execute("commit");

        MessageBox.showinfo("insert Status", "Inserted Successfully");
        con.close();

root = Tk()
root.geometry("600x300")
root.title("Python+Tkinter+Mysql")

id = Label(root, text='Enter ID',font=('bold', 10))
id.place(x=20,y=30);

name = Label(root, text='Enter Name',font=('bold', 10))
name.place(x=20,y=60);

phone = Label(root, text='Enter Phone',font=('bold', 10))
phone.place(x=20,y=90);

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

insert = Button(root, text="insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

root.mainloop()


