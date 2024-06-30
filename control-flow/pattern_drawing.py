#Printing a square pattern using input from the user
size = int(input("Enter the size of the pattern: "))
i=0
while i<size:
    j=0
    while j<size:
        print("*", end="")
        j = j+1
    print("\n")
    i = i+1