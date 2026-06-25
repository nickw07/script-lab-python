
# conversions from celsius
def celsius_to_kel(celsius):
    return celsius + 273.15  # -> kelvin


def celsius_to_fahrenheit(celsius):
    return (celsius * 1.8) + 32  # -> fahrenheit


# conversions from fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8  # -> celsius


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) / 1.8  # -> kelvin


# conversions from kelvin
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15  # -> celsius


def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 1.8) - 459.67  # -> fahrenheit


# constants & options
CELSIUS_SIGN = "°C"
FAHRENHEIT_SIGN = "°F"
KELVIN_SIGN = "K"

OPTIONS = [
    "1. Celsius to Kelvin",
    "2. Celsius to Fahrenheit",
    "3. Fahrenheit to Celsius",
    "4. Fahrenheit to Kelvin",
    "5. Kelvin to Celsius",
    "6. Kelvin to Fahrenheit",
]


# helping methods
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")
            continue


def print_result(orig_unit, orig_sign, res_unit, res_sign):
    print(f"{orig_unit} {orig_sign} -> {res_unit:.3f} {res_sign}")


def main():
    while True:
        print("-"*5, "OPTIONS", "-"*5)
        for option in OPTIONS:
            print(option)

        user_selection = input("Select an operation: ")

        if user_selection == "1":
            celsius = get_float("Celsius: ")
            result = celsius_to_kel(celsius)
            print_result(celsius, CELSIUS_SIGN, result, KELVIN_SIGN)

        elif user_selection == "2":
            celsius = get_float("Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            print_result(celsius, CELSIUS_SIGN, result, FAHRENHEIT_SIGN)

        elif user_selection == "3":
            fahrenheit = get_float("Fahrenheit: ")
            result = fahrenheit_to_celsius(fahrenheit)
            print_result(fahrenheit, FAHRENHEIT_SIGN, result, CELSIUS_SIGN)

        elif user_selection == "4":
            fahrenheit = get_float("Fahrenheit: ")
            result = fahrenheit_to_kelvin(fahrenheit)
            print_result(fahrenheit, FAHRENHEIT_SIGN, result, KELVIN_SIGN)

        elif user_selection == "5":
            kelvin = get_float("Kelvin: ")
            result = kelvin_to_celsius(kelvin)
            print_result(kelvin, KELVIN_SIGN, result, CELSIUS_SIGN)

        elif user_selection == "6":
            kelvin = get_float("Kelvin: ")
            result = kelvin_to_fahrenheit(kelvin)
            print_result(kelvin, KELVIN_SIGN, result, FAHRENHEIT_SIGN)

        else:
            print("Invalid input. Try again.")
            continue

        if input("Convert again? (y/n): ").lower() != "y":
            break


if __name__ == '__main__':
    main()
