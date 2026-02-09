'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 2 part 4
'''

credits = int(input("Number of completed credits: "))

if credits >= 0 and credits <= 23:
    print(" Class rank: Freshman")
elif credits >= 24 and credits <= 59:
    print(" Class rank: Sophmore")
elif credits >= 60 and credits <= 89:
    print(" Class rank: Junior")
elif credits >= 90:
    print(" Class rank: Senior")
