####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MichaelM'
strategy_name = 'Use early history'
strategy_description = '''\
Collude first round. Compare all rounds to the previous round and 
assume opponent will behave the same as the first time the previous 
round's result occurred. If the previous round's result never has 
happened, collude except after being severly punished.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
   #1 = collude
   #0 = defect

beNice = True

def play(opponentMove):
  opponentHistory= []
  global beNice
  opponentHistory.append(opponentMove)
  if opponentMove == 'start':
    beNice = True
    opponentHistory.append(1)
    return 1
  if opponentHistory[-1] == 0: #this refers to the last move
    beNice = False
  if beNice==True:
    return 1
  else:
    return 0

def name():
  return 'Michael'
