from tkinter import *

#open a text file with items for checklist
fileobject = open("input_file.txt")

#initialize an empty list
dailyTasks = []

#for loop to print lines of text file and append lines to dailyTasks list
for line in fileobject:
    dailyTasks.append(line)

# close file
fileobject.close()

# make a second empty list
dailyTasks2 = []

#removes last character from "/n" and puts elements in a different list
for task in dailyTasks:
    task = task[:-1]
    dailyTasks2.append(task)

print(dailyTasks2)

main_window = Tk()
main_window.title("Daily TaskList")

var = StringVar()
checklistTitle_Label = Label(main_window, textvariable = var, bg = "lightblue", relief=RAISED)
var.set("Daily TaskList")
checklistTitle_Label.config(font=("Courier",35))
checklistTitle_Label.grid(row=0,padx=20, pady=20)

'''
padx=
Optional horizontal padding to place around the widget in a cell. Default is 0.
pady=
Optional vertical padding to place around the widget in a cell. Default is 0.
'''

def do_a_task():
  global tasks_done
  tasks_done +=1

r = 1
for item in dailyTasks2:
    itemNumber = str(r) + ". "
    Checkbutton(main_window, text=itemNumber + item,command=do_a_task ,font =(30)).grid(row=r,column=0,sticky=W)
    r = r + 1

mainloop()