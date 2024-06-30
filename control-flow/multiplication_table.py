#The code will display the multiplication table from 1 to 10 for a number entered by the user
number = int(input("Enter a number to see its multiplication table: "))
for i in range(1,11):
    print(number," * ",i," = ",number*i)