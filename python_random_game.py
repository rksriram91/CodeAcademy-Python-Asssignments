'''Game user vs computer'''
from random import randint
from time import sleep
def get_user_guess():
  user_guess = int(raw_input("Guess a whole number :"))
  return user_guess

def roll_dice(number_of_sides):
  first_roll= randint(1,number_of_sides)
  second_roll= randint(1,number_of_sides)
  max_val=2*number_of_sides
  print "the max value in roll is " +str(max_val)
  sleep(1)
  user_guess=get_user_guess()
  if(user_guess > max_val ):
    print "user guess should be less than max_value"
    return 
  else:
    print "Rolling...."
    sleep(2)
    print "First roll is %d" %first_roll
    sleep(1)
    print "Second Roll is %d" %second_roll
    sleep(1)
    total_roll=first_roll+second_roll
    print "Result..."
    sleep(1)
    if(total_roll>user_guess):
      print "You won Fucker!!"
      return
    else:
      print "Oops you lost :sad LOSER :D"
      return
    
roll_dice(6) #calling the function
  
  