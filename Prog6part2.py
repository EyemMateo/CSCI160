'''
name: Mateo Sandoval-Luna
email: mateo.sandoval@und.edu

Project 6 part 2
'''

fname = input("Enter file name: ")
lower = float(input("Enter low limit: "))
upper = float(input("Enter high limit: "))

highest = None
lowest = None
total = 0
count = 0
file_has_content = False
foundUpper = 0
foundLower = 0
try:
    with open(fname, 'r') as fhand:
        if fhand == 0:
            print('no data found')
            exit()
        for line in fhand:
            file_has_content = True
            clean = line.strip()
            score = float(clean)
            if score == lower:
                foundLower = 1
            if score == upper:
                foundUpper = 1
            if lower <= score <= upper:
                count += 1
                total += score
                if highest is None or score > highest:
                    highest = score
                if lowest is None or score < lowest:
                    lowest = score
                    
except FileNotFoundError:
    print("There's been an issue, goodbye!")
    exit()
if count > 0:
    average = total / count
    print(count)
    if foundUpper == 1:
        print("Found value of high limit")
    else:
        print(highest)
    if foundLower == 1:
        print("Found Value of low limit")
    else:
        print(lowest)
    print(average)
else:
    print("\nNo scores were found within the specified range.")