'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 6 part 1
'''
x = input("please write testing")
fname = input("enter file name")
fhand = open(fname,'w')
var = 1

while var < 100 and var > 0:
    var = float(input('please input a number'))
    fhand.write(f"{var}\n")
fhand.close()