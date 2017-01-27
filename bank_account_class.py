class BankAccount():
  balance=0
  def __init__(self,name):
    self.name=name
    
  def __repr__(self):
    return "Account belongs to %s" %self.name
  
  def show_balance(self):
    print "Balance is %.2f" %self.balance
    
  def deposit(self,amount):
    if(amount<=0):
      print "Cannot deposit zero or less"
      return
    else:
      self.balance=self.balance+amount
      print "Amount deposited is %.2f"%amount
      self.show_balance()
      
  def withdraw(self,amount):
    if(amount>=self.balance):
      print "Cannot wthdraw more than the balance"
      return
    elif(amount<=0):
      print "Cannot withdraw zero or less"
      return
    else:
      self.balance=self.balance-amount
      print "Amount withdrawn is %.2f"%amount
      self.show_balance()
      

rk=BankAccount("sriram")  
print rk
print rk.show_balance()
rk.deposit(2000)
rk.withdraw(1000)
print rk
print rk.show_balance()
