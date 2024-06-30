#Printing a square pattern using input from the user
size = int(input("Enter the size of the pattern: "))
for i in range(size):
    for j in range(size):
        print("*", end="")
        
    print("\n")