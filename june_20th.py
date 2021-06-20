def totalcash():
    print('Lets sum up the total sales we did today')
   

def Namaste():
    print('Namaste')
def inputint(r):
    p=None
    while p is None:
        print(r)
        i=input()
        try:
            p=int(i)
        except ValueError:
                print('Please enter a valid Number')

        return p

Namaste()
totalcash()
inputint('enter the total cash sales today')

print('whats the cash sales today?')
myCash=inputint('Enter the cash count here')
print('what is the total of Card sales today?')
myCard=inputint('Enter the Card sales here')
print('whats the Digital sales today?')
myDigital=inputint('Enter the Digital sales today')
print('this is the total sales today')
print(str(myCash+myCard+myDigital))
      
