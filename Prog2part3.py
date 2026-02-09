'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 2 part 3
'''
fn = int(input("Enter the first number:"))
op = input("Enter the operation:")
sn = int(input("Enter the second number:"))

if op == "+":
    re = fn + sn
elif op == "-":
    re = fn - sn
elif op == "*":
    re = fn * sn
elif op == "/":
    re = fn / sn
elif op == "//":
    re = fn // sn
print("The result is:",re)