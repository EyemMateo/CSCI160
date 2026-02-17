'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 3 part 6
'''
f = 0
s = 0
j = 0
S = 0
x = int(input("How many students in the clas: "))
y=1
while y <= x:
    cr = input("Enter the student rank: ")
    if cr == "Freshman":
        f = f + 1
    elif cr == "Sophomore":
        s = s + 1
    elif cr == "Junior":
        j = j + 1
    elif cr == "Senior":
        S = S + 1
    y = y + 1
print("Freshman:", f)
print("Sophomores:", s)
print("Juniors:", j)
print("Seniors:", S)