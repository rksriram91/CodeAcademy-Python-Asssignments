'''Command line Calender Program
We can do CRUD of events in calender'''
from time import sleep,strftime
USER_FIRST_NAME='Sriraman'
calendar={}

def welcome():
  print "Welcome to Event Manager %s" %USER_FIRST_NAME
  sleep(1)
  strftime("%A, %b %d %Y +0000",localime())
  strftime("%H:%M:%S",localime())
  sleep(1)
  print "You succesfully used a new function, congrats! \n"
  print "What would you like to do ?"
  
def start_calendar():
  welcome()
  start=True
  while start:
    print "choose Any option \n A to add:U to update;V to view;D to delete"
    user_choice=raw_input("enter ur choice").upper()
    if(user_choice == 'V'):
      if(len(calendar.keys()) < 1):
        print "Calender is empty"
      else:
        print calendar
    elif(user_choice == 'U'):
      date=raw_input("What date?")
      update=raw_input("Enter the Update")
      calendar[date]=update
      print "\n Calendar Updated !!"
    elif(user_choice == 'A'):
      event=raw_input("Enter event :")
      date=raw_date("Enter date MM/DD/YYYY:")
      
      if((len(date) not in 10)):
        print "Invalid date"
        try_again=raw_input("Try Again? Y for Yes, N for No: ").upper()
        if(try_again=='Y'):
		  continue
		else:
		  start=False 
      else:   
        if(strftime("%Y",date)<= strftime("%Y",date)) ):
          print "Invalid date Previous years addition not allowed"
          try_again=raw_input("Try Again? Y for Yes, N for No: ").upper()
          if(try_again=='Y'):
			      continue
		      else:
			      start=False
        else:
          calendar[date]=event
          print "Event successfully added"
    elif(user_choice=='D'):
      if(len(calendar.keys()) < 1):
        print "Cannot delete.Calender is already empty"
      else:
        event=raw_input("Enter event to be deleted :")
        for date in calendar:
          if(calendar[date]==event):
            del calendar[date]
            print "Successfully Deleted"
          else:
            print "incorrect event was specified"
            
    elif(user_choice == 'X'):
    	start=False
     
    else:
      print "Invalid Command"
      

 start_calendar()     
        
      
      
      
      
        
  

