'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 6 part 2
'''
fname = input("enter file name")
try:
    fhand = open(fname,'r')
    file = fhand.read()
except FileNotFoundError:
    print("There's been a issue, goodbye!")
    exit
i = 1

while i < 100 and i > 0:
    i = int(input('please input a number'))
    fhand.write(str(i))
fhand.close()