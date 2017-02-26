from tkinter import *
from tkinter import ttk
import os
import GHX_Backend

ZoomAMT = 10 #10 small, 20 med, 30 large logoSize
DeBug = False
CK = True #changes from regular qurys to pirate mode

def about_program():
    GHX_Backend.openURL("https://en.wikipedia.org/wiki/Google_hacking")
def help_HelpDocs():
    GHX_Backend.openURL("https://github.com/ChocolaKuma/KumaGoogleHaxing")
def CK_ON():
    global CK
    CK = True
    print(CK)
    #TODO: MAKE THIS CHANGE THE GUI
    
def CK_OFF():
    global CK
    CK = False
    print(CK)
    #TODO: MAKE THIS CHANGE THE GUI
    
    
def HaxGen(event):
    #print("click")
    if(CK == True):
        intitleSTR = "intitle:+Index+of+"
    searchTerm = intitleSTR + str(Watcha.get())
    if(DeBug == True):
        print(searchTerm)
        GHX_Backend.loadedYet()
    x = int(var.get())
    if( x == 1):
        print("Movies selected")
        searchTerm = searchTerm+"+mp4+avi+mkv"
    if( x == 2):
        print("Music selected")
        searchTerm = searchTerm+"+mp3"
    GHX_Backend.makeURL(searchTerm)
    searchTerm = GHX_Backend.makeURL.gs
    print(searchTerm)
    GHX_Backend.openURL(searchTerm)    




root = Tk()
r = root
var = IntVar()

r.title("GHX by J.Hinebrook")

if(DeBug == False):
    #TODO Remove scaler and resize logo img
    #TODO ADD random logo art
    logo = PhotoImage(file="img/2.png")
    logo = logo.zoom(ZoomAMT) 
    logo = logo.subsample(40)
    logoPNG = Label(root, image=logo).grid(row=1,sticky=N,pady=4)

f = Frame(r)



Label(r,text="What are you looking for?").grid(row=2,sticky=N,pady=4)
Watcha = Entry(r)
Watcha.grid(row=3,sticky=N,pady=4)

if(CK == True):
    r1=Radiobutton(r,text="Movies",variable=var,value=1)
    r1.grid(row=4,sticky=W,pady=4)

    r2=Radiobutton(r,text="Music",variable=var,value=2)
    r2.grid(row=4,sticky=E,pady=4)

b = Button(r,text="Enter")
b.bind("<Button-1>",HaxGen)
b.grid(row=5,sticky=N,pady=4)

m = Menu(r)
fm = Menu(m)
fm.add_command(label="About Program",command = about_program)
m.add_cascade(label="About",menu=fm)

hm = Menu(m)
hm.add_command(label="Help Docs",command = help_HelpDocs)
m.add_cascade(label="Help",menu=hm)
r.config(menu=m)


pm = Menu(m)
pm.add_command(label="Feature Comming soon")
pm.add_command(label="CK_on",command = CK_ON)
pm.add_command(label="CK_off",command = CK_OFF)
m.add_cascade(label="Captain_Kuma",menu=pm)
r.config(menu=m)

r.mainloop()


#https://www.youtube.com/watch?v=-tbWoZSi3LU
#https://www.youtube.com/watch?v=DuLFA_aAu8M&list=PL8BEB66FBE6DB97AF&index=6
