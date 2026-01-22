'''
name:Mateo Sandoval-Luna
email:mateo.sandoval@und.edu

Part two
'''
penny = int(input("Pennies:"))
uarter = int(penny / 25)
running = penny - (uarter * 25)
dime = int((running) / 10)
running = running - (dime * 10)
nickle = int(running /5)
running = running - (nickle * 5)
pennies = int(running)


print("Quarters: ",uarter)
print("Dimes: ",dime)
print("Nickles: ",nickle)
print("Pennies: ",pennies)