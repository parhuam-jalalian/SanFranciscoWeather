"""Main for SanFranciscoWeather"""
from temperature import print_all_temperature
from sea_level import print_all_sea_level
from wind_speed import print_all_wind_speed
from humidity import print_all_humidity


def main() -> None:
    """Menu for entire project, options create matplotlib chart"""
    print(
        "\nWelcome to a database of San Francisco's"
        "pass weather history.\n"
        "Please type an integer to choose an option,"
        " else type 'q' to end program"
    )

    menu = (
        "\nOption 1: Temperature\n"
        "Option 2: Sea Level\n"
        "Option 3: Humidity\n"
        "Option 4: Wind Speed\n"
        "Type 'q' to end program"
    )

    flag = True
    while flag:
        print(menu)
        response = input("Type your response: ")
        if response == "q":
            print("Goodbye now.")
            flag = False
        elif response == "1":
            print_all_temperature()
        elif response == "2":
            print_all_sea_level()
        elif response == "3":
            print_all_humidity()
        elif response == "4":
            print_all_wind_speed()
        else:
            print("Your input did not match any of the options please" " try again.\n")


if __name__ == "__main__":
    main()
