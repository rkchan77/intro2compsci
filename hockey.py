from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

print("Downloading hockey data, wait?")
site = requests.get('https://www.hockey-reference.com/leagues/NHL_2019_skaters.html')

root = Tk()
root.geometry("500x550+850+50")
root.configure(background="LightBlue1")
root.title("Hockey pool")

can = Canvas(root, width=475, height=250)
can.place(x=10, y=60)
image10 = Image.open("tavares.jpg")
photo = ImageTk.PhotoImage(image10)
can.create_image(0, 0, anchor=NW, image=photo)

can1 = Canvas(root, width=500, height=40)
can1.place(x=10, y=10)
titleRect = can1.create_rectangle(0, 0, 480, 150, fill='DodgerBlue')
text = can1.create_text(60, 20, text="RK Hockey Pool", fill="black")

can2 = Canvas(root, width=120, height=165)
can2.place(x=205, y=350)
image1 = Image.open("headshots/marnemi01.jpg")
photo1 = ImageTk.PhotoImage(image1)
myimg = can2.create_image(0, 0, anchor=NW, image=photo1)

if site.status_code is 200: 
    content = BeautifulSoup(site.content, "html.parser")
else:
    content = -99
  
def scrape():
    if (messagebox.askyesno("Wait?", "This could take a few seconds. Wait?") == False):
       return
    if site.status_code is 200:
        content = BeautifulSoup(site.content, 'html.parser')                    
        totalpts = 0
        for myplayer in lst:
            dTag = content.find(attrs={"csk": myplayer})
            parent = dTag.findParent('tr')
            playerpts = int(parent.contents[8].text)
            print(myplayer + " " + str(playerpts))
            totalpts = totalpts + playerpts
        mypts.configure(text=totalpts)
            
def updatelab():
    lstprint = ""
    for item in lst:
        lstprint = lstprint + item + "\n"
    mylab.configure(text=lstprint)

def addItem():
   item = entry.get()
   if (lst.count != 0):
      lst.append(item)
      entry.delete(0, END) 
      updatelab()

def remItem():
   item = entry.get()
   if (len(lst) != 0):
      lst.remove(item)
      entry.delete(0, END) 
      updatelab() 
      
def saveList():
    myfile = open("myplayers.txt","w")
    for player in lst:
        myfile.write(player + "\n")
    myfile.close()
    messagebox.showinfo("myplayers.txt", "Players saved to disk")
      
def addPlayerOptions():
    if(content != -99):
        names = content.findAll(attrs={"data-stat" : "player"})
        playerOptions = []
        for player in names:
            if(player != "None"):
                playerOptions.append(player.get('csk'))
        return playerOptions
    
def addPlayer(evt):
    global players
    name = variable.get()
    if players.count(name) > 0:
        return
    listbox.insert(END, name)
    lst.append(name)
    
def remPlayer(value):
    var=listbox.get(ACTIVE)
    listbox.delete(listbox.index(ACTIVE))
    lst.remove(var)
    
def lstinfo(value):
    lstprint = ""
    if len(listbox.curselection()) == 0:
        lstprint = lst[0]
    else: 
        lstprint = listbox.get(ANCHOR)
        
def switchPhoto():
     global photo
     fullname = listbox.get(ANCHOR)
     firstname = fullname.split(",")[1]
     lastname = fullname.split(",")[0]
     filename = lastname[0:4] + firstname[0:2] + "01.jpg"
     switchPhoto = filename
    
    #a,b = filename/split(",")
    #filename = a[0:5].lower() + b[0:2].lower() + "01.jpg"
    #image1 = Image.open("headshots/" + filename)
    #photo = ImageTk.PhotoImage(image1)  
    #can.create_image(0, 0, anchor=NW, image=photo)
    
      
def comparePlayers():
    root1 = Tk()
    root1.geometry("490x540+860+50")
    root1.configure(background="LightBlue1")
    root1.title("Hockey pool")
    
    can1 = Canvas(root1, width=490, height=40)
    can1.place(x=10, y=10)
    titleRect = can1.create_rectangle(0, 0, 480, 150, fill='DodgerBlue')
    text = can1.create_text(60, 20, text="RK Hockey Pool", fill="black")
    
    def addPlayer(evt):
        global players
        name = variable.get()
        if players.count(name) > 0:
            return
        listbox.insert(END, name)
        lst.append(name)
        
    def addPlayerOptions():
        if(content != -99):
            names = content.findAll(attrs={"data-stat" : "player"})
            playerOptions = []
            for player in names:
                if(player != "None"):
                    playerOptions.append(player.get('csk'))
            return playerOptions
    
    listbox3 = Listbox(width=20,height=5)
    listbox3.place(x=10, y=80) 
    
    listbox4 = Listbox(width=20,height=5)
    listbox4.place(x=300, y=80)
    
    OPTIONS = addPlayerOptions()
    variable = StringVar(root1)
    variable.set(OPTIONS[0])
    w = OptionMenu(root1, variable, *OPTIONS, command=addPlayer)
    w.place(x=10, y=60)
    
    OPTIONS = addPlayerOptions()
    variable = StringVar(root1)
    variable.set(OPTIONS[0])
    w = OptionMenu(root1, variable, *OPTIONS, command=addPlayer)
    w.place(x=300, y=60)
    
    var=listbox3.get(ANCHOR)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        points=int(parent.contents[8].text)
        gp=int(parent.contents[5].text)
        age=int(parent.contents[2].text)
        team=str(parent.contents[3].text)
        position=str(parent.contents[4].text)
        plus=int(parent.contents[9].text)
        pim=int(parent.contents[10].text)
        
    listbox2 = Listbox(width=16,height=10)
    listbox2.place(x=10, y=350)
    listbox2.insert(END, "Stats(2018-2019)")
    listbox2.insert(END, "Games Played:" + str(gp))
    listbox2.insert(END, "Age:" + str(age))
    listbox2.insert(END, "Team:" + str(team))
    listbox2.insert(END, "Position:" + str(position))
    listbox2.insert(END, "Goals:" + str(goals))
    listbox2.insert(END, "Assists:" + str(assists))
    listbox2.insert(END, "Points:" + str(points))
    listbox2.insert(END, "+/-:" + str(plus))
    listbox2.insert(END, "PIM:" +str(pim))
    
    print("running")
    
    
def createlistbox(value):
    global image1
    global photo
    var=listbox.get(ANCHOR)
    filename = str(var)
    if var!=NONE:
        dTag=content.find(attrs={"csk":var})
        parent=dTag.findParent("tr")
        goals=int(parent.contents[6].text)
        assists=int(parent.contents[7].text)
        points=int(parent.contents[8].text)
        gp=int(parent.contents[5].text)
        age=int(parent.contents[2].text)
        team=str(parent.contents[3].text)
        position=str(parent.contents[4].text)
        plus=int(parent.contents[9].text)
        pim=int(parent.contents[10].text)
        
    listbox2 = Listbox(width=16,height=10)
    listbox2.place(x=345, y=350)
    listbox2.insert(END, "Stats(2018-2019)")
    listbox2.insert(END, "Games Played:" + str(gp))
    listbox2.insert(END, "Age:" + str(age))
    listbox2.insert(END, "Team:" + str(team))
    listbox2.insert(END, "Position:" + str(position))
    listbox2.insert(END, "Goals:" + str(goals))
    listbox2.insert(END, "Assists:" + str(assists))
    listbox2.insert(END, "Points:" + str(points))
    listbox2.insert(END, "+/-:" + str(plus))
    listbox2.insert(END, "PIM:" +str(pim))

listbox = Listbox(width=20,height=10)
listbox.place(x=10, y=350)
    
listbox.bind("<<ListboxSelect>>", createlistbox)
listbox.bind("<<ListboxSelect>>", )
listbox.bind("<Double-Button>", remPlayer)

OPTIONS = addPlayerOptions()
variable = StringVar(root)
variable.set(OPTIONS[0])
w = OptionMenu(root, variable, *OPTIONS, command=addPlayer)
w.place(x=10, y=320)

players = []

lst = []
lstprint = ""
totalpts = 0
print("Downloading Hockey Data")

comparebutton = Button(root, text="Compare players", command=comparePlayers)
comparebutton.place(x=210, y=320)

savebutton = Button(root, text="Save", command=saveList)
savebutton.place(x=135, y=525)

ptsbutton = Button(root,text="Check pts", command=scrape)
ptsbutton.place(x=20, y=525)

mypts = Label(root,text=totalpts)
mypts.place(x=100, y=525)

#create a canvas object
#place it in the location with the size that you want


mainloop()
