'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 2 part 2
'''
x = int(input("x:"))
y = int(input("y:"))

if x > 0 and y > 0:
    q = "quadrant I"
elif x > 0 and y < 0:
    q = "quadrant IV"
elif x < 0 and y < 0:
    q = "quadrant III"
elif x < 0 and y > 0:
    q = "quadrant II"
    
print("(",x,",",y,") Is in: ",q,sep="",end="")

