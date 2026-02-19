'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 4 part 5
'''

x = int(input("Enter Width: "))
y = int(input("Enter height: "))
z = input("Enter Character: ")
xX = 0
yY = 0

for yY in range(y):
    for xX in range(x):
        print(z,sep="",end="")
        xX = xX + 1
    print("\n",sep="",end="")
    yY = yY + 1