#Open file
file = open("us-500.csv")
#initialize counter x
x = 0
for line in file:
    #Separate words using comma separate variables
    words = line.split(",")
    lastname = words[1]
    x = x + 1
    print(lastname)

print('Total number of lastnames is '+ str(x)) > output.txt

file.close()
