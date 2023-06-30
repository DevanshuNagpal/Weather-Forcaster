# Weather Forecaster

Weather Forecaster is a Python program that retrieves and speaks the weather forecast for a given city using the WeatherAPI and the win32com library for text-to-speech functionality.

## Requirements

- Python 3.x
- requests library (`pip install requests`)
- win32com library (`pip install pywin32`)

## Usage

1. Clone the repository or download the `weather_forecaster.py` file.
2. Install the required libraries by running the following commands:
3. Run the program using the following command:
4. The program will greet you and ask for the name of the city for which you want the weather forecast.
5. Enter the name of the city when prompted.
6. The program will fetch the weather information from the WeatherAPI and speak it out using the system's text-to-speech capabilities.

## Notes

- This program uses the WeatherAPI to retrieve the weather information. You will need to sign up and obtain an API key from WeatherAPI (https://www.weatherapi.com/) and replace the `key` parameter in the URL within the code with your own API key.
- The program uses the `requests` library to make HTTP requests and the `win32com` library to provide text-to-speech functionality. Ensure that these libraries are installed before running the program.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to modify and enhance the code according to your needs.


