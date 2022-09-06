from tkinter import *
from tkinter import messagebox
from database import *
import sys

global gamesData
global labelListRem
global labeListDis
global gameListBox

labelListDis = []
labelListRem = []
gamesData = Database()

def mainMenu():#menu
    menu = Tk()
    menu.title("Video Game Database")
    menu.geometry("500x400")
    menu.configure(bg = "#0059b3")
    
    title = Label(menu, text = "Game Database\n", font = ("Consolas, 30"), bg = "#0059b3")
    title.pack()
    
    add = Button(menu, text = "Add a game", font = ("Consolas, 10"), command = addGameScreen, width = 30, height = 3)
    add.pack()
    
    find = Button(menu, text = "Find a game", command = search, font = ("Consolas, 10"), width = 30, height = 3)
    find.pack()
    
    dis = Button(menu, text = "Display all games", command = displayWin, font = ("Consolas, 10"), width = 30, height = 3)
    dis.pack()
    
    remove = Button(menu, text = "Remove a game", font = ("Consolas, 10"), width = 30, height = 3, command = removeWin)
    remove.pack()
    
    close = Button(menu, text = "Quit", command = quit)
    close.pack()
    
    
    menu.mainloop()
    

def addGameScreen(): #fields for game to be added to list and .txt file
    global nameField
    global yvar
    global gvarn
    global pvarn
    global creatorField
    
    new = Tk()
    new.title("Add a game")
    new.geometry("500x300")
    new.configure(bg = "#0059b3")
    
    name = Label(new, text = "Name:")
    nameField = Entry(new)
    name.pack()
    nameField.pack()
    
    genre = Label(new, text = "Genre:")
    gvarn = StringVar(new)
    gvarn.set("")
    genreList = OptionMenu(new, gvarn, "RPG", "FPS", "Sandbox", "Horror", "Fighting", "Puzzle", "Singleplayer")
    genre.pack()
    genreList.pack()
    
    year = Label(new, text = "Release Year:")
    yvar = StringVar(new)
    yvar.set("")
    yearList = OptionMenu(new, yvar, 
             "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983",
             "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000",
             "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017",
             "2018", "2019", "2020", "2021", "")
    
    year.pack()
    yearList.pack()
    
    platform = Label(new, text = "Platform:")
    platform.pack()
    pvarn = StringVar(new)
    pvarn.set("PC")
    platformList = OptionMenu(new, pvarn, "PC", "XBOX", "PS4", "Mobile", "Nintendo Switch")
    platformList.pack()
    
    creator = Label(new, text = "Creator:")
    creatorField = Entry(new)
    creator.pack()
    creatorField.pack()
    
    ok = Button(new, text = "Done", command = addGame)
    ok.pack()
    new.mainloop()
    
def addGame(): #adding to list and .txt file
    name = nameField.get()
    genre = gvarn.get()
    year = int(yvar.get())
    platform = pvarn.get()
    creator = creatorField.get()
    
    newGame = Game(name, genre, year, platform, creator)
    gamesData.add(newGame)
    messagebox.showinfo("Success", name + " has been added to the database")
    
    nameField.delete(0, END)
    gvarn.set("")
    yvar.set("")
    pvarn.set("")
    creatorField.delete(0, END)

def removeWin(): #fields to remove game from list and .txt file
    global rem
    global labelListRem
    rem = Tk()
    rem.title("Remove a game")
    rem.geometry("500x400")
    rem.configure(bg = "#0059b3")
    
    nameSearch = Label(rem, text = "Name of game you want to remove:")
    nameSearch.pack()
    
    nameSearchField = Entry(rem)
    nameSearchField.pack()
    labelListRem.clear()
    ok = Button(rem, text = "Delete", command = lambda:remove(nameSearchField.get()))
    ok.pack()
    
    rem.mainloop()
    
def remove(name): #compiles list of games to delete
    delList = []
    global labelListRem
    for x in labelListRem:
        x.destroy()
    delList.clear()
    delList = gamesData.findList(name, 0, 0, "", "", "")

    for x in delList:
        g = Label(rem, text = (x.name + ", " + x.genre + " Release Year: " + str(x.year) + " Platform: " + x.platform + " Developed by: " + x.creator))
        labelListRem.append(g)
    for x in labelListRem:
        x.pack()
    delLabel = Label(rem, text = "Delete these?")
    ok = Button(rem, text = "OK", command = lambda: removeLoop(delList))
    delLabel.pack()
    ok.pack()
    
        
def removeLoop(delList): #sends list fo games to delete to database.py delete function
    gamesRemoved = "The following games: "
    for x in delList:
        gamesData.delete(x.name)
        gamesRemoved += (x.name + " ")
    gamesRemoved += ("have been removed")
    messagebox.showinfo("Delete", gamesRemoved)
    
    
    rem.destroy()
    
    
def search(): #allows user to search for (a) specific game(s) based on paramters, fields can be left empty
    #to exclude that paramater from being a search parameter
    search = Tk()
    search.title("Search for a game")
    search.geometry("500x400")
    search.configure(bg = "#0059b3")
    
    
    info = Label(search, text = "(Parameters can be left blank exclude that search parameter)")
    info.pack()
    
    nameSearch = Label(search, text = "Name")
    nField = Entry(search)
    nameSearch.pack()
    nField.pack()
    
    yearSearch = Label(search, text = "Nelease year\nEnter two years to search in that range")
    yvar1 = StringVar(search)
    yvar2 = StringVar(search)
    yvar1.set("")
    yvar2.set("")
    yearList1 = OptionMenu(search, yvar1, 
             "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983",
             "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000",
             "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017",
             "2018", "2019", "2020", "2021", "")
    yearList2 = OptionMenu(search, yvar2, 
             "1967", "1968", "1969", "1970", "1971", "1972", "1973", "1974", "1975", "1976", "1977", "1978", "1979", "1980", "1981", "1982", "1983",
             "1984", "1985", "1986", "1987", "1988", "1989", "1990", "1991", "1992", "1993", "1994", "1995", "1996", "1997", "1998", "1999", "2000",
             "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017",
             "2018", "2019", "2020", "2021", "")
    
    yearSearch.pack()
    yearList1.pack()
    to = Label(search, text = "to")
    to.pack()
    yearList2.pack()
    
    genreSearch = Label(search, text = "Genre")
    gvar = StringVar(search)
    gvar.set("")
    genreList = OptionMenu(search, gvar, "RPG", "FPS", "Sandbox", "Horror", "Fighting", "Puzzle", "Singleplayer")
    genreSearch.pack()
    genreList.pack()
    
    platformSearch = Label(search, text = "Platform")
    pvar = StringVar(search)
    pvar.set("")
    platformList = OptionMenu(search, pvar, "PC", "XBOX", "PS4", "Mobile", "Nintendo Switch")
    platformSearch.pack()
    platformList.pack()
    
    creatorSearch = Label(search, text = "Creator")
    cField = Entry(search)
    creatorSearch.pack()
    cField.pack()
    
    ok = Button(search, text = "Search", command = lambda:findGame(nField.get(), yvar1.get(), yvar2.get(), gvar.get(), pvar.get(), cField.get()))
    ok.pack()
    
    search.mainloop()
    
def findGame(name, year1, year2, genre, platform, creator): #compiles and packs list of games to screen
    if year1 == "" or year2 == "":
        year1 = "0"
        year2 = "0"
    year1 = int(year1)
    year2 = int(year2)
    
    
    gameList = gamesData.findList(name, year1, year2, genre, platform, creator)
    
    results = Tk()
    results.geometry("500x800")
    results.title("Searching...")
    results.configure(bg = "#0059b3")
    for x in gameList:
        g = Label(results, text = (x.name + ", " + x.genre + " Release Year: " + str(x.year) + " Platform: " + x.platform + " Developed by: " + x.creator))
        g.pack()

def displayWin(): #displays all games depending on how user wants the data presented
    global svar
    global disp
    global labelListDis 
    disp = Tk()
    disp.title("Displaying all games...")
    disp.geometry("800x800")
    disp.configure(bg = "#0059b3")
    
    labelListDis.clear()
    
    displayMethod = Label(disp, text = "Sort by:")
    displayMethod.pack()
    svar = StringVar(disp)
    svar.set("")
    sortList = OptionMenu(disp, svar, "Alphabetically", "Reverse Alphabetically", "Year Newest", "Year Oldest")
    sortList.pack()
    
    dok = Button(disp, text = "Display", command = display)
    dok.pack()
    
    disp.mainloop()
    
def display():
    global labelListDis
    for x in labelListDis: #list is for destroying widgets in case user wants to display list multiple times so the
        #widgets dont stack on top of eachother
        x.destroy()
    labelListDis.clear()
    scroll = Scrollbar(disp)
    scroll.pack(side = RIGHT, fill = Y)
    gameList = gamesData.sortGames(svar.get())
    gameListBox = Listbox(disp, yscrollcommand = scroll.set, width = 110, height = 30)
    for x in gameList:
        gameListBox.insert(END, (x.name + ", " + x.genre + " Release Year: " + str(x.year) + " Platform: " + x.platform + " Developed by: " + x.creator))
        
    gameListBox.pack()
    labelListDis.append(gameListBox)
    labelListDis.append(scroll)
    scroll.config(command = gameListBox.yview)

    for x in labelListDis:
        x.pack()
    
mainMenu()