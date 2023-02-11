from tkinter import *
from backend import Database
database=Database("Books.db")
def get_selected_row(event):
    try:
        global selected_tuple
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)
    for row in database.view_db():
        list1.insert(END, row)

def insert_command():
    list1.delete(0,END)
    for row in database.insert(e1_val.get(), e3_val.get(), e2_val.get(), e4_val.get()):
        list1.insert(END, row)

def search_command():
    list1.delete(0,END)
    for row in database.search(e1_val.get(),e3_val.get(),e2_val.get(),e4_val.get()):
        list1.insert(END, row)

def delete_command():
    list1.delete(0,END)
    for row in database.delete(e4_val.get()):
        list1.insert(END, row)

def update_command():
    list1.delete(0,END)
    for row in database.update(e1_val.get(),e3_val.get(),e2_val.get(),e4_val.get()):
        list1.insert(END, row)




window= Tk()
########################################
l1=Label(window, text="Title")
l1.grid(row=0, column=0)

e1_val=StringVar()
e1=Entry(window, textvariable=e1_val)
e1.grid(row=0, column=1)
#########################################

#########################################
l2=Label(window, text="Year")
l2.grid(row=1, column=0)

e2_val=StringVar()
e2=Entry(window, textvariable=e2_val)
e2.grid(row=1, column=1)
#########################################

#########################################
l3=Label(window, text="Author")
l3.grid(row=0, column=2)

e3_val=StringVar()
e3=Entry(window, textvariable=e3_val)
e3.grid(row=0, column=3)
#########################################

#########################################
l4=Label(window, text="ISBN")
l4.grid(row=1, column=2)

e4_val=StringVar()
e4=Entry(window, textvariable=e4_val)
e4.grid(row=1, column=3)
##########################################

###########################################
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
###########################################

###########################################
b1=Button(window, text="View All", width=12, command= view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search Entry", width=12, command= search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Delete Entry", width=12, command= delete_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Insert", width=12, command= insert_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Update Selected", width=12, command= update_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command= window.destroy)
b6.grid(row=7, column=3)

s1=Scrollbar(window)
s1.grid(row=2, column=2, rowspan=6)
###########################################
list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview)
window.mainloop()
