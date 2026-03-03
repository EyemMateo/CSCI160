'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 5
'''
import math
def square(intValue):
    #Returns the suare of the int value
    suare = intValue * intValue
    return suare
def sumOfSquares(intValue):
    #returns the sum of suares from 1 to intvalue
    i = int(0)
    summ = int(0)
    while intValue >= i:
        summ = summ + (i * i)
        i = i + 1
    return summ
def numberOfBuses(numOfStudents):
    i = int(0)
    stuL = numOfStudents
    bus = int(1)
    while stuL >= 30:
        bus = bus + 1
        stuL = stuL - 30
    return bus

def distance(x1,y1,x2,y2):
    dxS = (x2 - x1) ** 2
    dyS = (y2 - y1) ** 2
    
    return float(math.sqrt(dxS + dyS))
def slope(x1,y1,x2,y2):
    Y = y2 - y1
    X = x2 - x1
    if x1 == x2:
        return("None")
    else:
        return((Y / X))
def compareTo(intValue1, intValue2):
    if intValue1 < intValue2:
        return(-1)
    elif intValue1 > intValue2:
        return(1)
    elif intValue1 == intValue2:
        return(0)

#print(square(int(input("Square input"))))
print(compareTo((int(input("SquareSum input"))), (int(input("SquareSum input")))))
