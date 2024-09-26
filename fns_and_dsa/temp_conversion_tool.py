# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    return fahrenheit

# Main function to handle user interaction
def main():
    try:
        # User input: temperature and unit (C/F)
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        # Convert based on the unit
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        else:
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        # Handle non-numeric input for temperature
        print("Invalid temperature. Please enter a numeric value.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
