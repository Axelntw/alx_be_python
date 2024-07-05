#This script will convert between celsius and fahrenheit based on the input

def convert_to_celsius(fahrenheit):
    FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    temperature = int(input("Enter the temperature to convert: "))
    choice = str(input("Is this temperature in Celsius or Fahrenheit? (C/F):")).upper()
    if choice == "C":
        print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")
    elif choice == "F":
        print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")
if __name__ == "__main__":
    main()