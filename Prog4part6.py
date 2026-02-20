'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 4 part 6
'''

PA = 0
PC = 0
NA = 0
NC = 0
Pcalc = 0
Ncalc = 0
x = int(input("Enter a value: "))
while x != 0:
    if x > 0:
        PA = PA + x
        PC = PC + 1   
    else:
        NA = NA + x
        NC = NC + 1
    x = int(input("Enter a value: "))
if PC > 0:
    Pcalc = PA / PC
else:
    Pcalc = 0
if NC > 0:
    Ncalc = NA / NC
else:
    Ncalc = 0
print(f"Average of positive values:{Pcalc:.2f}")
print(f"Average of negative values:{Ncalc:.2f}")