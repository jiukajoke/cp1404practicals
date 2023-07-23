"""Temperature Conversion Functions"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    """Main function to demonstrate temperature conversions."""
    print("Temperature Conversion:")
    print("C. Celsius to Fahrenheit")
    print("F. Fahrenheit to Celsius")

    choice = input("Enter your choice (C or F): ")

    if choice.upper() == "C":
        celsius_value = float(input("Enter temperature in Celsius: "))
        fahrenheit_value = celsius_to_fahrenheit(celsius_value)
        print(f"{celsius_value:.2f}°C is equal to {fahrenheit_value:.2f}°F")
    elif choice.upper() == "F":
        fahrenheit_value = float(input("Enter temperature in Fahrenheit: "))
        celsius_value = fahrenheit_to_celsius(fahrenheit_value)
        print(f"{fahrenheit_value:.2f}°F is equal to {celsius_value:.2f}°C")
    else:
        print("Invalid choice. Please enter C or F.")

if __name__ == "__main__":
    main()
