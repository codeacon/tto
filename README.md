# tto
A Simple Shell Tic-Tac-Toe game written in python3
  (not compatible with python2 because of formatting troubles)

File Structure:
  tGame.py: The framework for the game. It contains the functions necessary to make the game run, but it does not play a game.
  mm.py: Plays a game against a computer using a minimax algorithm
  ruleBase.py: Plays a game against a computer using a rule based method.

Game Play:
  mm.py is an implementation of tic-tac-toe that uses a minimax algorithm to brute force the game.
  If you would like to play against that algorithm, simply cd into this directory and type: python3 mm.py

  ruleBase.py is a rule based implementation of tic-tac-toe. It does not look ahead more than one move.
  If you would like to play against the rule based implementation, cd into this directory and type: python3 ruleBase.py

Planned Developments:
  Add an additional game brain using a deep learning algorithm

