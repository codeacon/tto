# the playGame, availableSquares, and board functions exist in tGame. Also imports random and time
from tGame import *

#Skip to computerTurn() and read comments there first
#function definitions for the computer to decide which square to go on.


#This function takes the current board state, and the opposing token
# returns corners opposite the opposingToken, if any. False if none
def oppositeCorner(positions, opposingToken):
  options = []
  if (positions[0] == opposingToken) & (isinstance(positions[8], int)):
    options.append(8)
  if (positions[2] == opposingToken) & (isinstance(positions[6], int)):
    options.append(6)
  if (positions[6] == opposingToken) & (isinstance(positions[2], int)) :
    options.append(2)
  if(positions[8] == opposingToken) & (isinstance(positions[0], int)):
    options.append(0)
  if (len(options) > 0):
    return options
  else:
    return False

#this function takes the current board state, and checks for available corners. 
#it returns an array of available corners if any, and False if no available corners.
def emptyCorner(positions):
  availableCorners = []
  if isinstance(positions[0], int):
    availableCorners.append(0)
  if isinstance(positions[2], int):
    availableCorners.append(2)
  if isinstance(positions[6], int):
    availableCorners.append(6)
  if isinstance(positions[8], int):
    availableCorners.append(8)
  if(len(availableCorners) > 0):
    return availableCorners
  else:
    return False

#takes board state 
#returns list of empty sides
def emptySides(positions):
  availableSides = []
  if isinstance(positions[1], int):
    availableSides.append(1)
  if isinstance(positions[3], int):
    availableSides.append(3)
  if isinstance(positions[5], int):
    availableSides.append(5)
  if isinstance(positions[7], int):
    availableSides.append(7)
  if(len(availableSides) > 0):
    return availableSides
  else:
    return False

#takes board state and a token. 
#Iterates through all possible board states one move in advance and checks if any would cause a three in a row with given token
#returns winning moves for a given token
def checkWin(positions, token):
  avail = availableSquares(positions)
  wouldWin = []
  for i in avail:
    testPos = list(positions)
    testPos[i] = token
    if isOver(testPos):
      wouldWin.append(i)
  return wouldWin

#takes board state and a token
#iterates through all possible board states on move forward and checks if any of those states have more than one winning move
# returns forking squares for a given token
def checkFork(positions, token):
  avail = availableSquares(positions)
  forkSquares = []
  for i in avail:
    testPos = list(positions)
    testPos[i] = token
    possibleWin = checkWin(testPos, token)
    if len(possibleWin) > 1:
      forkSquares.append(i)
  return forkSquares

#computer decides which square to take
#follows the following rules:
# 1. If there are no tokens on the board, take a random corner
# 2. If there is an opportunity to win, take it
# 3. If the opponent goes first and take the two opposing corners, the computer will have taken the middle.
#    the only way to ensure a tie is to take an empty side
# 4. Fork, if possible
# 5. If the opponent can fork, block that fork.
# 6. Take center
# 7. Take opposite corner
# 8. Take empty corner
# 9. take an empty side
# The computer then makes that move in the positions array, and returns the positions array.

def computerTurn(positions, cToken, pToken):
  if len(availableSquares(positions)) == 9: computerMove = random.choice(emptyCorner(positions, cToken))

  elif checkWin(positions, cToken): computerMove = random.choice(checkWin(positions, cToken))

  elif checkWin(positions, pToken): computerMove = random.choice(checkWin(positions, pToken))

  elif (positions[0] == positions[8]) | (positions[2] == positions[6]): computerMove = random.choice(emptySides(positions))

  elif checkFork(positions, cToken): computerMove = random.choice(checkFork(positions, cToken))

  elif checkFork(positions, pToken): computerMove = random.choice(checkFork(positions, pToken))

  elif isinstance(positions[4], int): computerMove = 4

  elif oppositeCorner(positions, pToken): computerMove = random.choice(oppositeCorner(positions, pToken))

  elif emptyCorner(positions): computerMove = random.choice(emptyCorner(positions))

  elif emptySides(positions): computerMove = random.choice(emptySides(positions))

  positions[computerMove] = cToken
  return positions

#playGame function imported from tGame.py
#takes the name of the computerTurn function, and handles all other necessary aspects of the game.
#computer turn function must take position, computerToken and playerToken as arguments and return a valid game position array
playGame(computerTurn)
