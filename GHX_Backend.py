import webbrowser,os


DeBug = True





def loadedYet():
    print("GHXBE Loaded!")

def makeURL(st):
    gs = "https://www.google.com/search?as_q="
    #gs=google string
    #st=Searchterms
    print("MAKEURL")
    makeURL.gs = str(gs) + str(st)

def openURL(URL,DeBug=False):
    if(DeBug == True):
        print("Opening: ",URL)
    webbrowser.open_new(URL)

def main(st):
    makeURL(st)
    openURL(makeURL.gs)



