while True:
    try:
        fahrenheit = int(input("Enter the temperature in fahrenheit: "))
        break
    except (ValueError, OverflowError):
        print("Error, enter a valid integer!")

try:
    celsius = (fahrenheit - 32) * 5/9
except OverflowError:
    print("Error, that number is too big!")
else:
    print(f"The temperature in celsius is {celsius} degrees!")
finally:
    print("Thank you for using the weather forecast application")