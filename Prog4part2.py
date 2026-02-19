'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 4 part 2
'''
x = int(input("Input: "))
y = x - 1
while y > 0:
    if x % y == 0:
        print("largest devisor:",y)
        break
    y -= 1