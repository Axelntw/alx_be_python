from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date(futurenumdays):
    future_date = display_current_datetime() + timedelta(days=futurenumdays)
    return future_date

def main():
    print(f"Current date and time: {display_current_datetime().strftime('%Y-%m-%d %H:%M:%S')}")
    future_number_of_days = int(input("Enter the number of days to add to the current date: "))
    print(f"Future date: {calculate_future_date(future_number_of_days).strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()