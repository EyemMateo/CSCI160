'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 3 part 5
'''
x = int(input("starting value: "))
y = int(input("ending value: "))

if x > y:
    while x >= y:
        print(x)
        x = x - 1
else:
    while x <= y:
        print(x)
        x = x + 1
