#A calculator that requires input of two numbers and an operator
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = str(input("Choose the operation (+, -, *, /): "))
match operation:
    case "+":
        print(f"The result is {first_number + second_number}.")
              
    case "-":
        print(f"The result is {first_number - second_number}.")

    case "*":
        print(f"The result is {first_number * second_number}.")

    case "/":
        print(f"The result is {first_number - second_number}.")

    case _:
        print(f"Invalid operation. Please try again!")