'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 4 part 4
'''
x = input("initial string: ")
y = input("charecter to count: ")
num = int(0)
for char in x:
    if char == y:
        num = num + 1
print("Number of occurrences:",num)