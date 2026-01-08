from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
def connect_db():
return mysql.connect(
host="localhost",
user="root",
password="Pheonix2025!",
database="my_database"
)
def Insert():
roll_no = roll_entry.get()
name = name_entry.get()
subject = subject_entry.get()
if roll_no == "" or name == "" or subject == "":
MessageBox.showinfo("ALERT", "Please enter all fields")
else:
con = connect_db()
cursor = con.cursor()
cursor.execute("INSERT INTO Student (roll_no, name, subject) VALUES (%s, %s, %s)",
(roll_no, name, subject))
con.commit()
MessageBox.showinfo("Status", "Successfully Inserted")
con.close()
def Update():
roll_no = roll_entry.get()

name = name_entry.get()
subject = subject_entry.get()
if name == "" or subject == "":
MessageBox.showinfo("ALERT", "Please enter fields you want to update!")
else:
con = connect_db()
cursor = con.cursor()
cursor.execute("UPDATE Student SET name = %s, subject = %s WHERE roll_no = %s",
(name, subject, roll_no))
con.commit()
MessageBox.showinfo("Status", "Successfully Updated")
con.close()
def Del():
if roll_entry.get() == "":
MessageBox.showinfo("ALERT", "Please enter Roll No to delete row")
else:
con = connect_db()
cursor = con.cursor()
cursor.execute("DELETE FROM Student WHERE roll_no = %s", (roll_entry.get(),))
con.commit()
roll_entry.delete(0, 'end')
name_entry.delete(0, 'end')
subject_entry.delete(0, 'end')
MessageBox.showinfo("Status", "Successfully Deleted")
con.close()
def Select():
if roll_entry.get() == "":
MessageBox.showinfo("ALERT", "Roll No is required to select row!")
else:
con = connect_db()
cursor = con.cursor()
cursor.execute("SELECT * FROM Student WHERE roll_no = %s", (roll_entry.get(),))
rows = cursor.fetchall()
if rows:
for row in rows:
name_entry.insert(0, row[1])
subject_entry.insert(0, row[2])
else:
MessageBox.showinfo("ALERT", "No record found with this Roll No.")
con.close()
root = Tk()

root.geometry("500x300")
root.title("MySQL CRUD Operations")
roll_label = Label(root, text="Roll No:", font=("verdana 15"))
roll_label.place(x=50, y=30)
roll_entry = Entry(root, font=("verdana 15"))
roll_entry.place(x=150, y=30)
name_label = Label(root, text="Name:", font=("verdana 15"))
name_label.place(x=50, y=80)
name_entry = Entry(root, font=("verdana 15"))
name_entry.place(x=150, y=80)
subject_label = Label(root, text="Subject:", font=("verdana 15"))
subject_label.place(x=50, y=130)
subject_entry = Entry(root, font=("verdana 15"))
subject_entry.place(x=150, y=130)
Button(root, text="Insert", command=Insert, font=("verdana", 12), width=10).place(x=50, y=190)
Button(root, text="Update", command=Update, font=("verdana", 12), width=10).place(x=180,
y=190)
Button(root, text="Delete", command=Del, font=("verdana", 12), width=10).place(x=50, y=240)
Button(root, text="Select", command=Select, font=("verdana", 12), width=10).place(x=180,
y=240)
root.mainloop()