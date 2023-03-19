import tkinter as tk
import sys

filename = sys.argv[1]

main_window = tk.Tk()
main_window.title("Checklist")
main_window.lift()

var = tk.StringVar()
checklistTitle_Label = tk.Label(main_window, textvariable = var, bg = "lightblue", relief=tk.RAISED)
var.set("Checklist")
checklistTitle_Label.config(font=("Courier",35))
checklistTitle_Label.grid(row=0,padx=20, pady=20)

with open(filename) as fileObject:
        dailyTasks = [line.strip() for line in fileObject]

r = 1
for item in dailyTasks:
    itemNumber = str(r) + ". "
    tk.Checkbutton(main_window, text=itemNumber + item, font =(30)).grid(row=r,column=0,sticky=tk.W)
    r = r + 1

main_window.mainloop()