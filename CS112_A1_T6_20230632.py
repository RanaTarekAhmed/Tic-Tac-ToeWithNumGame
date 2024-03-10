# Program: tic-tac-toe with numbers a 3x3 is displayed and player 1 takes odd numbers 1,3,5,7,9 and player 2 takes even numbers 0,2,4,6,8.Players take turns take a number only once and a position number. Odd numbers start.the first person to complete a line that adds up to 15 is the winner. The line can have both odd and even numbers.
# Author: Rana Tarek Ahmed Fouad Ibrahim  رنا طارق احمد فؤاد ابراهيم
# Version : last version
# Date : 3 - 3 - 2024

#  Display a welcome massage and instructions how game is played
print("*** Welcome to Tic-Tac-Toe game!***\n")
print("Rules: A 3x3 is displayed and player 1 takes odd numbers {1,3,5,7,9} and player 2 takes even numbers {0,2,4,6,8}.\n"
"Players take turns take a number only once and a position number as shown at the bottom game table. Odd numbers start.\n"
"The first person to complete a line that adds up to 15 is the winner. The line can have both odd and even numbers.\n->Positions numbers:")

# Initialize the board game
BoardGame = ["1", "|", "2", "|", "3",
             "4", "|", "5", "|", "6",
             "7", "|", "8", "|", "9"]
print(BoardGame[0], BoardGame[1], BoardGame[2], BoardGame[3] , BoardGame[4])
print("-----------")
print(BoardGame[5],BoardGame[6] , BoardGame[7],BoardGame[8] , BoardGame[9])
print("-----------")
print(BoardGame[10],BoardGame[11] , BoardGame[12], BoardGame[13], BoardGame[14])
print("-----------")
BoardGame =["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# make first and second players list to choose from it (odd numbers for first player and even numbers for second player)
player1numbers = [1, 3, 5, 7, 9]
player2numbers = [0, 2, 4, 6, 8]

# variable for player
player = 1

# variable for winner
winner = None

# variable for knowing that the round is still running
GamePlaying = True

# function to display the board to the user
def printboard(BoardGame):
    print(BoardGame[0], "|", BoardGame[1], "|", BoardGame[2])
    print("----------")
    print(BoardGame[3], "|", BoardGame[4], "|", BoardGame[5])
    print("----------")
    print(BoardGame[6], "|", BoardGame[7], "|", BoardGame[8])

# function for game round
def Gameround():
    if player == 1:
        print("**First player turn**")
        print("Enter a number from {", *player1numbers, "} and the position of it")
        num = input("Number:")
        x = num.isnumeric()
        while x == False:
            print("please enter a number")
            num = input("Number:")
            x = num.isnumeric()
        num = int(num)
        pos = input("Position:")
        x = pos.isnumeric()
        while x == False:
            print("please enter a number position")
            pos = input("Position:")
            x = pos.isnumeric()
        pos = int(pos)
        if pos < 1 or pos > 9:
            print("The position is out of table !!")
            Gameround()
        elif num in player1numbers and BoardGame[pos - 1] == "-":
            BoardGame[pos - 1] = num
            player1numbers.remove(num)
        elif num not in player1numbers and BoardGame[pos - 1] == "-":
            print("Wrong number!! please enter a valid number")
            Gameround()
        elif  num  in player1numbers and  BoardGame[pos - 1] != "-":
            print("Already used position!!")
            Gameround()
        else:
            print("Wrong number and already used position!!!")
            Gameround()
    else:
        print("**Second player Turn**")
        print("Enter a number from {", *player2numbers, " } and the position of it")
        num = input("Number:")
        x = num.isnumeric()
        while x == False:
            print("please enter a number")
            num = input("Number:")
            x = num.isnumeric()
        num = int(num)
        pos = input("Position:")
        x = pos.isnumeric()
        while x == False:
            print("please enter a number position")
            pos = input("Position:")
            x = pos.isnumeric()
        pos = int(pos)
        if pos < 1 or pos > 9:
            print("The position is out of table !!")
            Gameround()
        elif num in player2numbers and BoardGame[pos - 1] == "-":
            BoardGame[pos - 1] = num
            player2numbers.remove(num)
        elif num not in player2numbers and BoardGame[pos - 1] == "-":
            print("Wrong number!! please enter a valid number")
            Gameround()
        elif num in player2numbers and BoardGame[pos - 1] != "-":
            print("Already used position!!")
            Gameround()
        else:
            print("Wrong number and already used position!!!")
            Gameround()

#  function for Checking all the three rows if any of them sums up to 15
def checkhorizontal(BoardGame):
     global winner
     if BoardGame[0] != "-" and BoardGame[1] != "-" and BoardGame[2] != "-":
         if BoardGame[0] + BoardGame[1] + BoardGame[2] == 15 :
             winner = str(player)
             return True
     if BoardGame[3] != "-" and BoardGame[4] != "-" and BoardGame[5] != "-":
         if BoardGame[3] + BoardGame[4] + BoardGame[5] == 15 :
             winner = str(player)
             return True
     if BoardGame[6] != "-" and BoardGame[7] != "-" and BoardGame[8] != "-":
         if BoardGame[6] + BoardGame[7] + BoardGame[8] == 15:
             winner = str(player)
             return True

# function for Checking all the three columns if any of them sums up to 15
def checkverticcal(BoardGame):
     global winner
     if BoardGame[0] != "-" and BoardGame[3] != "-" and BoardGame[6] != "-":
         if BoardGame[0] + BoardGame[3] + BoardGame[6] == 15 :
             winner = str(player)
             return True
     if BoardGame[1] != "-" and BoardGame[4] != "-" and BoardGame[7] != "-":
         if BoardGame[1] + BoardGame[4] + BoardGame[7] == 15 :
             winner = str(player)
             return True
     if BoardGame[2] != "-" and BoardGame[5] != "-" and BoardGame[8] != "-":
         if BoardGame[2] + BoardGame[5] + BoardGame[8] == 15:
             winner = str(player)
             return True

# function for checking  the diagonals if any of them sums up to 15
def checkdiagonals(BoardGame):
     global winner
     if BoardGame[0] != "-" and BoardGame[4] != "-" and BoardGame[8] != "-":
         if BoardGame[0] + BoardGame[4] + BoardGame[8] == 15 :
             winner = str(player)
             return True
     if BoardGame[2] != "-" and BoardGame[4] != "-" and BoardGame[6] != "-":
         if BoardGame[2] + BoardGame[4] + BoardGame[6] == 15 :
             winner = str(player)

             return True

# function for Checking if the winning situation was found to end the game
def winner():
    global GamePlaying
    if checkdiagonals(BoardGame) or checkhorizontal(BoardGame) or checkverticcal(BoardGame):
        printboard(BoardGame)
        if player == 1:
            print("*** The winner is the first player ***")
        else:
            print("*** The winner is the second player ***")
        GamePlaying = False

# function to check if the board is full and no one won (draw)
def checkdraw(BoardGame):
      global GamePlaying
      if checkverticcal(BoardGame) or checkhorizontal(BoardGame) or checkdiagonals(BoardGame) and "-" not in BoardGame:
          return None
      elif "-" not in BoardGame:
          print("**It is a draw!!!!!!!!**")
          GamePlaying = False

# function to switch players
def switchplayers():
      global player
      if player ==1 :
          player = 2
      else:
          player = 1

# The game is playing
while True:
    print("Choose:\nA) Start the game\nB) Exit")
    choiceone = input()
    while choiceone != "A" and choiceone != "a" and choiceone != "B" and choiceone != "b":
        print("Invalid input Try again")
        choiceone = input()
    if choiceone == "A"  or choiceone == "a":
        while GamePlaying:
                 printboard(BoardGame)
                 Gameround()
                 winner()
                 checkdraw(BoardGame)
                 switchplayers()
    elif choiceone == "B" or choiceone == "b":
        break