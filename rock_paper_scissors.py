'''Rock paper scissiors Game'''
from random import randint
from time import sleep
options=["R","P","S"]
lose="you Lost!!"
win="you Won!!"
def decide_winner(user_choice,computer_choice):
  print "user_choice"
  print "Computer selecting..."
  sleep(1)
  print computer_choice
  user_choice_index=options.index(user_choice)
  computer_choice_index=options.index(computer_choice)
  if(user_choice == computer_choice):
    print "Its a tie"
  elif((user_choice=="R" and computer_choice=="S") or (user_choice=="P" and computer_choice=="R") or (user_choice=="S" and computer_choice=="P")):
    print "User wins"
  else:
    print "Computer Wins"
    
def input():
  print "Welcome To Rock Paper Scissors"
  option=raw_input("Select R for rock, P for Paper, S for Scissors").upper()
  if option not in options:
    print "Invalid option Selected"
  else:
    computer_choice=options[randint(0,2)]
    decide_winner(option,computer_choice)
 
input()