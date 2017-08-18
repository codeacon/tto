from tGame import *

#this file uses a minimax algorithm to brute force a game of tic-tac-toe
#uses tGame to manage the game, and only provides the computerTurn algorithm
#algorithm uses 10 for win, 0 for tie, -10 for loss
#checks all possible moves
#alternates between taking the highest possible score, and then lowest possible score as it traverses the move tree
#this simulates perfect players playing tic-tac-toe and each selecting the optimal move based on possible moves and final states

#helper function that finds the largest values in a dictionary
#stores largest values in a list
#returns random choice from list (to keep the game interesting)
def helpMax(d):
  maxVal = -1
  maxKeys = []
  for i in d:
    if d[i] > maxVal:
      maxKeys = [i]
      maxVal = d[i]
    elif d[i] == maxVal:
      maxKeys.append(i)
  return random.choice(maxKeys)

#recursive-ish maxi function
#takes game positions, computer token and player token
#checks if the game is over, and returns values according to who won, or tie
#iterates over all possible moves and calls mini function on each
#(mini will either return the end of game, or iterate over each possible possition with maxi)
#returns the largest score from each move after the mini function has processed it
def maxi(positions, cToken, pToken):
  if isOver(positions) == cToken:
    return 10
  elif isOver(positions) == pToken:
    return -10
  elif len(availableSquares(positions)) == 0:
    return 0
  else:
    avail = availableSquares(positions)
    values = []
    for pos in avail:
      newPos = list(positions)
      newPos[pos] = cToken
      values.append(mini(newPos, cToken, pToken))
    return max(values)

#recursive-ish mini function
#takes game positions, computer token and player token
#checks if the game is over, and returns values according to who won, or tie
#iterates over all possible moves and calls maxi function on each 
#(maxi will either return the end of game, or iterate over each possible possition with mini)
#returns the largest score from each move after the maxi function has processed it    
def mini(positions, cToken, pToken):
  if isOver(positions) == cToken:
    return 10
  elif isOver(positions) == pToken:
    return -10
  elif len(availableSquares(positions)) == 0:
    return 0
  else:
    avail = availableSquares(positions)
    values = []
    for pos in avail:
      newPos = list(positions)
      newPos[pos] = pToken
      values.append(maxi(newPos, cToken, pToken))
    return min(values)

#computerTurn takes board state, computer token and player token
#finds all available squares and sets up a dictionary to store move options
#iterates over available moves using the mini function, and stores the move and scores in a dict
#calls helpMax to choose best move from dict
#updates and returns the board state
def computerTurn(positions, cToken, pToken):
  avail = availableSquares(positions)
  moveVals = {}
  for i in avail:
    newPos = list(positions)
    newPos[i] = cToken
    moveVals[i] = mini(newPos, cToken, pToken)
  moveChoice = helpMax(moveVals)
  positions[moveChoice] = cToken
  return positions

playGame(computerTurn)
