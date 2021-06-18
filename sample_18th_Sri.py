def letsGame():
    print('lets play a game')
    print('enter a number')
    
def Hello():
    print('hello All..')

def inputint(r):
    p=None
    while p is None:
        
        print(r)
        
        i=input()
        
        try:
            p=int(i)
        except ValueError:
            print('thats a wrong one, enter a number')

    return p

Hello()
letsGame()
inputint('Enter the value')

print('how many days')
myDays=inputint('Enter number of days')
print('Oh,Great'+str(myDays))
print('those'+str(myDays)+ 'has Hours')
myHours=inputint('Enter number of hours' )
print('this is the total of'+str(myDays+myHours))

    
