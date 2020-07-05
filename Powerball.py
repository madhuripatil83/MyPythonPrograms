import random

def Powerball():

    drawno = random.randrange(1,36)
    x = random.randrange(1,60)
    y = random.randrange(1,60)          
    a = random.randrange(1,60)  
    b = random.randrange(1,60)
    c = random.randrange(1,60)
    print("Today's numbers are " + str(x) + "  " +str(y) + " " + str(a) + " "+str(b) +" "+ str(c))
    print(" The Powerball number is " +str(drawno))
    if ( drawno == x):
         print("Yahoo!! You have just won a jackpot! Congratulations!")
    elif (drawno == y):
         print("Yahoo!! You have just won a jackpot! Congratulations!")
    elif(drawno == a):
         print("Yahoo!! You have just won a jackpot! Congratulations!")
    elif(drawno == b):
         print("Yahoo!! You have just won a jackpot! Congratulations!")
    elif(drawno == c):
         print("Yahoo!! You have just won a jackpot! Congratulations!")
    else :
          print("Better luck next time!!")

          
Powerball()
Powerball()
Powerball()
    
    

    
