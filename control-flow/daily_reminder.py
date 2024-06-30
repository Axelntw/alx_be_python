#Gives a user a reminder in terms of the priority-level and time bound of the task
task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): "))
time_bound = str(input("Is it time-bound? (yes/no): "))
match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"{task} is a high priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time bound! Please enter 'yes' or 'no'.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires attention today!")
        elif time_bound == "no":
            print(f"{task} is a medium priority task. Consider completing it when you have free time.")
        else:
            print("Invalid input for time bound! Please enter 'yes' or 'no'.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low priority task that requires attention today!")
        elif time_bound == "no":
            print(f"{task} is a low priority task. Consider completing it when you have free time")
        else:
            print("Invalid input for time bound! Please enter 'yes' or 'no'.")
    case _:
        print("Invalid input for priority! Please enter 'high', 'medium' or 'low'.")