'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 6 part 1
'''
#x = input("please write testing")
fname = input("enter file name")
fhand = open(fname,'w')
var = 5
while var < 100 and var > 0:
    var = float(input('please input a number'))
    if var > 100 or var < 0:
        fhand.close()
        continue
    fhand.write(f"{var}\n")