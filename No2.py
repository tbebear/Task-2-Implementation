from datetime import time
import string 

currentime = time(13,0,0) #declare time now 
star = time(8,0,0)
end = time(17,0,0)
Basefee = 0
x : int
Addfee = 0
drop : string


x = int(input("Welcome please input the computer-amount : "))
if (x == 1 or x == 2):
    Basefee += 50
    Addfee = 0
elif (x >= 3 and x <= 10):
    Basefee += 100 
    for i in range(0,x):
        Addfee += 10
elif (x >10):
    Basefee+= 500
    for i in range(0,x):
        Addfee += 10
if (currentime < star and currentime > end):
    Basefee = Basefee * 2
drop = int(input("Are you willing to drop off and pick up type (1 if yes): "))
if (drop == 1):
    Basefee = Basefee / 2

print("Total fee : ",Basefee + Addfee)
