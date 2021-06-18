def LetsGame():
    print('lets play a game')
def hello():
    print('Namaskara')
    print('yella Aaarama')
    print('Hope you are staying safe')
def inputint():
    r=None
    while r is None:
        i=input()
        print('enter a value')
        try:
            r=int(i)
        except ValueError:
            print('Thats a wrong one, enter a number')
    
    return r
    


hello()
LetsGame()

inputint()

print('how many days')
myDays=inputint()
print('Oh Great'+str(myDays))
print('those'+str(myDays)+'has hours')
myHours=inputint()
try:
    print(int(myDays)+int(myHours))
except ValueError:
    print('thats a wrong one')
    
