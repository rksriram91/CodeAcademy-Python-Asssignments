'''RGB to HEX converter'''
def rgb_hex():
  invalid_msg = "ERROR!!Invalid values"
  red=int(raw_input("Enter red Value(0-255) :"))
  if(red not in range(0,256)):
    print invalid_msg
    return
  green=int(raw_input("Enter green Value(0-255 :"))
  if(green not in range(0,256)):
    print invalid_msg
    return
  blue=int(raw_input("Enter blue Value(0-255 :"))
  if(blue not in range(0,256)):
    print invalid_msg
    return
  val=(red<<16)+(green<<8)+blue
  print hex(val).upper()

'''RGB to HEX converter'''
def hex_rgb():
  invalid_msg = "ERROR!!Invalid values"
  hex_val=raw_input("Enter hexadecimal Value :")
  if(len(hex_val) != 6):
    print invalid_msg
  else:
    hex_val=int(hex_val,16)
  two_hex_digits=2**8
  blue=hex_val%two_hex_digits
  hex_val=hex_val >> 8
  green=hex_val%two_hex_digits
  hex_val=hex_val >> 8
  red=hex_val%two_hex_digits
  print "RGB value is %d%d%d"%(red,green,blue)
  
def convert():
  while True:
    option=raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:.")
    if(option=='1'):
      rgb_hex()
    elif(option=='2'):
      hex_rgb()
    elif(option=='X' or option=='x'):
      break
    else:
      print "Error!no such option"
      
convert()      
    
      
    
    