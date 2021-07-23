from tkinter import *
master = Tk()
master.config(background="blue")
label = Label(master, text="Hockey Pool")
label.config(background="black")
label.config(foreground="gold")
label.pack()
button = Button(master, text="QUIT", fg="red", command=quit)
button.pack(side=BOTTOM)
listbox = Listbox(master)
listbox.config(background="gold")
listbox.config(foreground="blue")
listbox.pack()
listbox.insert(END, "Player, Goals")
lst = [["connormcdavid", 208], ["sidney crosby", 234], ["steven stanmkos", 187], ["auston matthews", 78]]
for item in lst:
        listbox.insert(END, item[0] + "-" + str(item[1]))
	
mainloop()
