'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Project 2 part 1
'''
#noc number of checks
noc = int(input("Number of checks: "))

if noc < 20:
    price = noc * .12
    
elif noc >= 20 and noc <= 39 :
    price = noc * .10
    
elif noc >= 40 and noc <= 59 :
    price = noc * .08
    
elif noc >= 60 :
    price = noc * .06

price = price + 10
price = f"{price:.2f}"
print("Service fee: $", price,sep="",end="")
