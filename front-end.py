from Tkinter import *
from database_handler import *

'''
Function For Buttons
'''

def view_command():
    list1.delete(0, END)
    for tup in view_all():
        list1.insert(END, tup)

def search_command():
    list1.delete(0, END)
    for tup in search(e1_variable.get(), e2_variable.get(), e3_variable.get()):
        list1.insert(END, tup)

def add_command():
    insert(e1_variable.get(), e2_variable.get(), e3_variable.get(), e4_variable.get())
    list1.delete(0, END)
    list1.insert(END, "Sucesso!!!")

def delete_command():
    delete(selected_tup[0])
    view_command()

def update_command():
    update(selected_tup[0], e1_variable.get(), e2_variable.get(), e3_variable.get(), e4_variable.get())
    view_command()

def get_select_row(event):
    global selected_tup
    try:
        index = list1.curselection()[0]
        selected_tup = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tup[1])
        e2.delete(0, END)
        e2.insert(END, selected_tup[2])
        e3.delete(0, END)
        e3.insert(END, selected_tup[3])
        e4.delete(0, END)
        e4.insert(END, selected_tup[4])
    except IndexError:
        pass


window = Tk()
window.wm_title('Books Repository')

'''
/---------/
/ Entries /
/---------/
'''
#Title
var = StringVar()
label1 = Label(window, textvariable = var)
var.set('Title')
label1.grid(row=0,column = 0)

e1_variable = StringVar()
e1 = Entry(window, textvariable = e1_variable)
e1.grid(row=0, column = 1)

#Year
var = StringVar()
label2 = Label(window, textvariable = var)
var.set('Year')
label2.grid(row=1,column = 0)

e2_variable = StringVar()
e2 = Entry(window, textvariable = e2_variable)
e2.grid(row=1, column = 1)

#Author
var = StringVar()
label3 = Label(window, textvariable = var)
var.set('Author')
label3.grid(row=0,column = 2)

e3_variable = StringVar()
e3 = Entry(window, textvariable = e3_variable)
e3.grid(row=0, column = 3)

#ISBN
var = StringVar()
label4 = Label(window, textvariable = var)
var.set('ISBN')
label4.grid(row=1,column = 2)

e4_variable = StringVar()
e4 = Entry(window, textvariable = e4_variable)
e4.grid(row=1, column = 3)

'''
Show Text
'''
list1 = Listbox(window, height = 10, width = 35)
list1.grid(row=2, column = 0, rowspan = 6, columnspan = 2)

list1.bind('<<ListboxSelect>>', get_select_row)

sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 2, rowspan = 6 )
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

sb2 = Scrollbar(window, orient = HORIZONTAL)
sb2.grid(row = 8, column = 0, columnspan = 2)
list1.configure(xscrollcommand = sb2.set)
sb2.configure(command = list1.xview)



'''
/---------/
/ Buttons /
/---------/
'''
# View Button
b1 = Button(window, text= 'VIEW', width = 12, command = view_command)
b1.grid(row=2, column = 3)

# Search Button
b2 = Button(window, text= 'SEARCH', width = 12, command = search_command)
b2.grid(row=3, column = 3)

# Add Button
b3 = Button(window, text= 'ADD', width = 12, command = add_command)
b3.grid(row=4, column = 3)

# UPDATE Button
b4 = Button(window, text= 'UPDATE', width = 12, command= update_command)
b4.grid(row=5, column = 3)

# DELETE Button
b5 = Button(window, text= 'DELETE', width = 12, command = delete_command)
b5.grid(row=6, column = 3)

# Close Button
b6 = Button(window, text= 'CLOSE', width = 12, command = window.destroy)
b6.grid(row=7, column = 3)




window.mainloop()
