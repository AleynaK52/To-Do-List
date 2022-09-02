from tkinter import *
from tkinter import messagebox

ws = Tk()

ws.geometry('500x450+500+200')
ws.title('To-Do List')
ws.config(bg='#d1ccc0')

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(frame, width=20, height=8, font=("Trajan ", 15), bd=0, fg="#2f3542", selectbackground='#CAD3C8',activestyle="none")
lb.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

for item in task_list:
    lb.insert(END, item)

my_entry = Entry(ws,font=('', 20))

button_frame = Frame(ws)
button_frame.pack(pady=20)

my_entry.pack(pady=20)

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)
    
addTask_btn = Button(button_frame,text='Görev Ekle <3',font=('Trajan  14'),bg='#227093',  padx=10, pady=10,command=newTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button( button_frame,text='Sil',font=('Trajan  14'),bg='#b33939',padx=10,pady=10, command=deleteTask)

delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)




ws.mainloop()

