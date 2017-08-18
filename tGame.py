import random
import time

#Picks a random taunt from a pre-defined array of taunts.
#Returns said taunt
#What would a tic-tac-toe game be without taunts?
def randomTaunt():
  taunts = [
    "You're father was a hamster",
    "The force is strong with this one",
    "Do I look fat to you?",
    "No, Buzz. I AM your father.",
    "You're gonna be Jimmy Hoffa the Sequel.",
    "I've seen worse from Kindergarteners...",
    "Seriously, don't quit your day job."
  ]
  return random.choice(taunts)

#Takes a list of characters
#prints characters one at a time with no trailing newline
#prints trailing newline after all characters in list
def printRow(row):
  for i in row:
    print(i, end="")
  print()

#take a board state
#prints the board in said state
#requires printRow() helper function
def printBoard(positions):
  middleRow = ['_', '_', '_', '|', '_', '_', '_', '|', '_', '_', '_']
  lastRow = [' ', ' ', ' ', '|', ' ', ' ', ' ', '|', ' ', ' ', ' ']
  firstRow = [' ', positions[0], ' ', '|', ' ', positions[1], ' ', '|', ' ', positions[2], ' ']
  secondRow = [' ', positions[3], ' ', '|', ' ', positions[4], ' ', '|', ' ', positions[5], ' ']
  thirdRow = [' ', positions[6], ' ', '|', ' ', positions[7], ' ', '|', ' ', positions[8], ' ']
  printRow(firstRow)
  printRow(middleRow)
  printRow(secondRow)
  printRow(middleRow)
  printRow(thirdRow)
  printRow(lastRow)

#takes board state
#iterates over possible winning states
#returns winner if winning state is found
def isOver(positions):
  finalPos = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ]
  returnVar = False
  for i in finalPos:
    if positions[i[0]] == positions[i[1]] == positions[i[2]]:
      returnVar = positions[i[0]]
      break
  return returnVar

#takes board state
#iterates over all board squares
#returns all empty board squares
def availableSquares(positions):
  avail = []
  for i in positions:
    if isinstance(i, int):
      avail.append(i - 1)
  return avail

#takes board state and token
#prompts user for move
#checks move, and prompts user again, if invalid
#updates board state if valid
#returns board state
def userTurn(positions, userToken):
  avail = availableSquares(positions)
  userPos = False
  while(userPos == False):
    print("Your turn...")
    userPos = input("Which square would you like to take... \n")
    try:
      userPos = int(userPos) - 1
      if userPos in avail:
        break
      else:
        print("That square is already taken... please try again.")
        userPos = False
    except:
      userPos = False
  positions[userPos] = userToken
  return positions

#takes the logic of computerTurn as arg
#initiates blank board state
#prints welcome message
#asks user what token they would like to play, and validates token choice. Prompts user again if token choice is invalid
#uses printBoard to print the board. checks for end of game, prints winner or tie if over
#Executes player and computer turns based on what token the player selected
#asks user if they would like to play again when the game is over, and re-initiates the board.
def playGame(computerTurn):
  positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  print("Welcome to tic-tac-toe. Prepare to be crushed.")
  while(True):
    computerToken = 'x'
    userToken = False
    while (userToken == False):
      userToken = input("Which token do you prefer, x or o?\n").lower()
      if (userToken != 'x') & (userToken != 'o'):
        userToken = False
        print("Try selecting either an 'x' or an 'o'...")
      print("Excellent. Let the games begin")
    if userToken == 'x':
      computerToken = 'o'
      while(True):
        printBoard(positions)
        positions = userTurn(positions, userToken)
        if isOver(positions):
          print("The winner is ", isOver(positions))
          printBoard(positions)
          break
        elif len(availableSquares(positions)) == 0:
          print("Tie Game...", randomTaunt())
          printBoard(positions)
          break
        positions = computerTurn(positions, computerToken, userToken)
        print(randomTaunt())
        time.sleep(1.25)
        print("I'll go... here.")
        print()
        time.sleep(1.25)
        if isOver(positions):
          print("The winner is ", isOver(positions))
          break
        elif len(availableSquares(positions)) == 0:
          print("Tie Game... maybe next time")
          break
    else:
      userToken = 'o'
      while(True):
        positions = computerTurn(positions, computerToken, userToken)
        time.sleep(1.25)
        print("I'll go... here.")
        time.sleep(1.25)
        if isOver(positions):
          print("The winner is ", isOver(positions))
          printBoard(positions)
          break
        elif len(availableSquares(positions)) == 0:
          print("Tie Game... maybe next time")
          printBoard(positions)
          break
        printBoard(positions)
        positions = userTurn(positions, userToken)
        if isOver(positions):
          print("The winner is ", isOver(positions))
          printBoard(positions)
          break
        elif len(availableSquares(positions)) == 0:
          print("Tie Game...", randomTaunt())
          printBoard(positions)
          break
        print(randomTaunt())
        print()

    playAgain = input("Would you like to play again? (yes/no)").lower()
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if playAgain == 'yes':
      continue
    else:
      break
