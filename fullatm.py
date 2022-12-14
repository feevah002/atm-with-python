# this application helps a user create a bank account and withdraw money
from sys import api_version


yes = 1
no = 2
service = {1: 'Cash transaction', 2: 'Change pin', 3: 'Block account'}
service[1]= 1
service[2]= 2
service[3]= 3

def pinrule():
  pin = int(input('please enter your card pin: '))
  if len(str(pin)) == 4:
    print('')
  else: 
    print('invalid pin, please try again')   
    return pinrule()
    
def usernewpin():
  pin = int(input('please enter a new pin: '))
  if len(str(pin)) == 4:
    repin = int(input('please enter pin again: '))
    if pin == repin:
      print ('\npin successfully created!!\n')
      print ('you can now perform transactions with your card.\n')
    else:
      print ('\npin doesnt match!!\n')
      return usernewpin() 

  else: 
    print('invalid pin, pin must be a four digit number') 
    
    return usernewpin() 
    
def accountnumberrule():
  accountnumber = int(input())
  if len(str(accountnumber)) == 10:
    print('')
  else: 
    print('invalid account number, please try again')   
    return accountnumberrule() 

def accountlimit():
  amount = int(input())
  lat = 100
  hat = 9000000
  if amount >= lat and amount <= hat:
      print('') 
  elif amount < lat:
    print('amount too little, try again!! ')
    return accountlimit()
  elif amount > hat:
    print ('amount exceeding daily limit, please try again')
    return accountlimit()

def service():
  print('please choose a service\n\n1. cash transaction\t2. change pin\t3. block account\t4. cancel: ')
  servicechoice = int(input(''))
  if servicechoice == 1:  
    sendmoney() 
    
    
  elif servicechoice == 2:
    pinchange()

  elif servicechoice == 3:
    blockaccount()

  elif servicechoice == 4:
    print ('Have a good day sir/ma')

  else:
    print('invalid option please try again')
    service()

def sendmoney():
  cashTransOpt= int(input('please select\n1. send money\t2. cash withdrawal\n'))
  if cashTransOpt == 1:
    print('please select the bank you wish to send to\n1. firstbank\t2. zenith bank\t3. uba')
    bankselected()
        
  elif cashTransOpt == 2:
    pinrule()
    print('how much do you wish to withdrawl: ')
    accountlimit()
    print('successful, please take your cash')
  
 
  else:
      print ('invalid choice!!!\n')
      sendmoney()

def bankselected():
  selected = int(input())


  if selected == 1:
    bankselect()
  elif selected == 2:
    bankselect()
  elif selected ==3:
    bankselect()
  else:
    print ('invalid choice, please try again')
    bankselected()

def bankselect(): 
  acct = int(input('\nplease insert account number: '))
  if len(str(acct)) == 10:
    print('amount to send: ')
    accountlimit()
    pinrule()
    print('sucessful!!!')
    return 0
  else:   
    print ('invalid account number')
    bankselect()
    return 0

def pinchange():
  oldpin = int(input('please input your old pin: '))
  if len(str(oldpin)) == 4:
    newpin = int(input('please input your new pin: '))
    if len(str(newpin)) == 4:
      print ('pin successfully changed')
      if newpin == oldpin:
        print('new pin cannot be same as old pin')
        pinchange()
    else:
      print('new pin must be for digits')
      pinchange()
  else: 
    print ('both pins must be four digits')
    pinchange()
    return 0

def blockaccount():
  pin = int(input('please input your pin: '))
  if len(str(pin)) == 4:
    print ('please enter account you wish to block')
    accountnumberrule()
    print ('account number successfully blocked')
  else: 
    print('invalid pin, please try again\n')
    return blockaccount()

def newuserinfo():
  print('Please enter your information')
  firstname = str(input('firstname: '))
  lastname = str(input('lastname: '))
  middlename = str(input('middlename: '))
  phonenumber = str(input('phone number: '))
  Email = str(input('Email: '))
  dob = int(input('DD\MM\YY: ')) 
  bvn = str(input('Bank Verification Number (BVN): '))
  maidenname = str(input('mum\'s maiden name: '))

  
userpin_db = (usernewpin)
userdb= {
  "emmanuel":{

  },
  
  "joy":{

  },

  }

print ('\n...Welcome to the Bank of Time...\n')
print ('please do you have a bank account with us')
userstats = int(input('1. yes\n2. no\n'))
if userstats == yes:
  service()
elif userstats == no:
  createAcct = int(input("""\nplease create an account in order to use our service
            Do you wish to create an account with us?
            1. yes
            2. no\n"""))
  if createAcct == 1:
    newuserinfo()
    print('\nyour BOT account has been sucessfully created\n')
    usernewpin()
    service()
else:
  print('invalid selection')

