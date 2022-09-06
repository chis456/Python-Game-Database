from game import *

class Database():
    def __init__(self):
        global games
        games = []
        data = open("games.txt", "r")
        
        #read data from games.txt, fields are seperated by commas
        for line in data:
            name = ""
            genre = ""
            yearStr = ""
            year = 0
            platform = ""
            creator = ""
            nextLine = line
            
            for x in range(len(nextLine)):
                if nextLine[x] == ",":
                    toReplace = name + ", "
                    nextLine = nextLine.replace(toReplace, "", 1)
                    break
                name += nextLine[x]
                
            for i in range(len(nextLine)):
                if nextLine[i] == ",":
                   toReplace = genre + ", "
                   nextLine = nextLine.replace(toReplace, "", 1)
                   break
                genre += nextLine[i]
                
            for q in range(len(nextLine)):
                if nextLine[q] == ",":
                   toReplace = yearStr + ", "
                   nextLine = nextLine.replace(toReplace, "", 1)
                   break
                yearStr += nextLine[q]
            year = int(yearStr)
            yearStr = ""
            
            for k in range(len(nextLine)):
                if nextLine[k] == ",":
                   toReplace = platform + ", "
                   nextLine = nextLine.replace(toReplace, "", 1)
                   break
                platform += nextLine[k]
                
            for j in range(len(nextLine)):
                if nextLine[j] == ",":
                   break
                creator += nextLine[j]
            
            games.append(Game(name, genre, year, platform, creator))
                
    def getList(self):
        return games
    
    #takes game and writes its info to file
    def add(self, game):
        games.append(game)
        lineData = "\n"
        lineData += game.name
        lineData += ", "
        lineData += game.genre
        lineData += ", "
        lineData += str(game.year)
        lineData += ", "
        lineData += game.platform
        lineData += ", "
        lineData += game.creator
        data = open("games.txt", "a")
        data.write(lineData)
        data.close()
    
    #deletes game from .txt file
    def delete(self, name):
        lineList = []
        dataFile = open("games.txt", "r")
        for line in dataFile:
            lineList.append(line)
            nextName = ""
            for i in line:
                if i == ",":
                    break
                nextName += i
            if nextName == name:
                lineList.pop()
        dataFile.close()
        dataFile = open("games.txt", "w")
        for x in lineList:
            dataFile.write(x)
        for i in range(len(games)):
            if games[i].name == name:
                games.pop(i)
                break
            
    #searches for game(s) on parameters
    def findList(self, name, year1, year2, genre, platform, creator):
        name = name.strip().lower()
        creator = creator.strip().lower()
        gameList = games[:] #first all games are loaded into a list
        i = 0
        
        #any game that does not match criteria are removed
        while i < len(gameList):
            if name != "":
                if gameList[i].name.strip().lower().find(name) != 0:
                    gameList.pop(i)
                    if i != 0:
                        i -= 1
                    continue
            if year1 != 0 and year2 != 0:
                if year1 > gameList[i].year or year2 < gameList[i].year:
                    gameList.pop(i)
                    if i != 0:
                        i -= 1
                    continue
            if genre != "":
                if gameList[i].genre != genre:
                    gameList.pop(i)
                    if i != 0:
                        i -= 1
                    continue
            if platform != "":
                if gameList[i].platform != platform:
                    gameList.pop(i)
                    if i != 0:
                        i -= 1
                    continue
            if creator != "":
                if gameList[i].creator != creator:
                    gameList.pop(i)
                    if i != 0:
                        i -= 1
                    continue
            i += 1
        return gameList
        
    #sort based on user selection of alphabetically, year released, and its ascending and descending orders
    def sortGames(self, method):
        gameList = games
        if method == "Alphabetically":
            for i in range(len(gameList)):
                for j in range(1, len(gameList) - i):
                    if gameList[j - 1].name > gameList[j].name:
                        temp = gameList[j]
                        gameList[j] = gameList[j - 1]
                        gameList[j - 1] = temp
            return gameList
        if method == "Reverse Alphabetically":
            for i in range(len(gameList)):
                for j in range(1, len(gameList) - i):
                    if gameList[j - 1].name > gameList[j].name:
                        temp = gameList[j]
                        gameList[j] = gameList[j - 1]
                        gameList[j - 1] = temp
            gameList.reverse()
            return gameList
        if method == "Year Newest":
            for i in range(len(gameList)):
                for j in range(1, len(gameList) - i):
                    if gameList[j - 1].year < gameList[j].year:
                        temp = gameList[j]
                        gameList[j] = gameList[j - 1]
                        gameList[j - 1] = temp
            return gameList
        if method == "Year Oldest":
            for i in range(len(gameList)):
                for j in range(1, len(gameList) - i):
                    if gameList[j - 1].year > gameList[j].year:
                        temp = gameList[j]
                        gameList[j] = gameList[j - 1]
                        gameList[j - 1] = temp
        return gameList
            
    
            
                    
                
 
        
        

        