from tkinter import *

with open("input_file.txt") as fileObject:
    dailyTasks = [line.strip() for line in fileObject]

main_window = Tk()
main_window.title("Daily TaskList")

var = StringVar()
checklistTitle_Label = Label(main_window, textvariable = var, bg = "lightblue", relief=RAISED)
var.set("Daily TaskList")
checklistTitle_Label.config(font=("Courier",35))
checklistTitle_Label.grid(row=0,padx=20, pady=20)

r = 1
for item in dailyTasks:
    itemNumber = str(r) + ". "
    Checkbutton(main_window, text=itemNumber + item, font =(30)).grid(row=r,column=0,sticky=W)
    r = r + 1

mainloop()