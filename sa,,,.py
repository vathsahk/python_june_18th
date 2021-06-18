def aataadona ():
    print('lets play a game')

def letsGame ():
    print('Lets play a game')
def inputint():
    i=input()
    return int(i)


print('how many days ')
myDays=inputint()
print('oh great'+ str(myDays))
print('those'+str(myDays)+' has hours')
myHours=inputint()
try:
    print(int(myDays)+ int(myHours))
except:
    print('thats a wrong one')

aataadona()



print('how many cricket balls?')
myballs=input()
print('oh great'+myballs)
print('Add pellets')
mypellets=input()
print('we have total of ')
print(int(myballs)+int(mypellets))

letsGame()


