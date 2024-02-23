"""
Created on Tue Feb 20 10:05:11 2024

@author: ethan
"""
import json


def main():
    #runs the main loop
    game = getDefaultGame()
    keepGoing = True
    while keepGoing:
        userChoice = getuserChoice()
 #calls a menu
 # 0-5, exit game, play default gmae, load game, save game, edit
        if userChoice == "0":
            keepGoing = False
        elif userChoice == "1":
            print("Load default game")
            game = getDefaultGame()
        elif userChoice == "2":
            print("Load a game file")
            game = loadGame()
        elif userChoice == "3":
            print("save the current game")
            saveGame(game)
        elif userChoice == "4":
            print("edit or add node")
            game = editNode(game)
        elif userChoice == "5":
            playGame(game)
        else:
            print("Please choose 1-5")
    # sends control to other parts of program
    
 #getMenuChoice()
#prints a menu of user options    
def getuserChoice():
    
    keepgoing = True
    while keepgoing:
        print("""
            0) exit
            1) load default game 
            2) load a game file
            3) save the current game
            4) edit or add a node
            5) play the current game""")
        userChoice = input("what will you do? ")
    return userChoice


def getDefaultGame():
    """creates the default game"""
    
    game = {"start": ["default start node", "Start over", "start", "Quit", "quit"]}
    return game
    
    
def saveGame(game):
    """uses json module to print game and save it"""
    
    fileOut = open("game.json", "w")
    print(json.dumps(game, indent =2))
    json.dump(game, fileOut, indent =2)    
    fileOut.close()
    
def loadGame():
    """uses json to load game from game.json"""
    
    fileIn = open("game.json", "r")
    game = json.load(fileIn)
    fileIn.close()
    return game



def playGame():
    """plays the game"""
    keepGoing = True
    currentNode = "start"
    while keepGoing:
        if currentNode == "quit":
            keepGoing = False
        else: 
            currentNode = playNode(game, currentNode)
            
def playNode(game, currentNode):
    """plays node if possible returning new or quit"""
    if currentNode in game.keys():
        (desc, menuA, nodeA, menuB, nodeB) = game[currentNode]
        print(f"""
              {desc}
              1) {menuA}
              2){menuB}
              3){nodeA}
              4){nodeB}
    """) 
    return playNode

def editGame():
    
    
    