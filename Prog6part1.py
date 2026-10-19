'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 6 part 1
'''
fname = input("enter file name")
fhand = open(fname,'w')
i = 1

while i < 100 and i > 0:
    i = int(input('please input a number'))
    fhand.write(str(i))
fhand.close()