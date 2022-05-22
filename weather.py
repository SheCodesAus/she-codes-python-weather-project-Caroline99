import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    return datetime.fromisoformat(iso_string).strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    return round((float(temp_in_farenheit) - 32) * 5 / 9, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    w = [float(x) for x in weather_data]
    return sum(w) / len(w)


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data_list = []
    with open(csv_file) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            if line:
                data_list.append(line)
    data_list.pop(0)
    for d in data_list:
        d[1] = int(d[1])
        d[2] = int(d[2])
    return data_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and its position in the list.
    """
    if not weather_data:
        return ()
    min_temp = min(weather_data)
    last_position = max(idx for idx, val in enumerate(weather_data) if val == min_temp)
    return (float(min_temp), last_position)  


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if not weather_data:
        return ()
    max_temp = max(weather_data)
    last_position = max(idx for idx, val in enumerate(weather_data) if val == max_temp)
    return (float(max_temp), last_position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    total_days = len(weather_data)
    dates = [x[0] for x in weather_data]
    min_temps = [x[1] for x in weather_data]
    max_temps = [x[2] for x in weather_data]

    lowest_temp  = format_temperature(convert_f_to_c(find_min(min_temps)[0]))
    highest_temp = format_temperature(convert_f_to_c(find_max(max_temps)[0]))
    lowest_date  = convert_date(dates[find_min(min_temps)[1]])
    highest_date = convert_date(dates[find_max(max_temps)[1]])
    av_low       = format_temperature(convert_f_to_c(calculate_mean(min_temps)))
    av_high      = format_temperature(convert_f_to_c(calculate_mean(max_temps)))

    return f'''{total_days} Day Overview
  The lowest temperature will be {lowest_temp}, and will occur on {lowest_date}.
  The highest temperature will be {highest_temp}, and will occur on {highest_date}.
  The average low this week is {av_low}.
  The average high this week is {av_high}.
'''


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    daily_summary = ''
    for day in weather_data:
        date  = f'---- {convert_date(day[0])} ----\n'
        min_t = f'  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}\n'
        max_t = f'  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}\n'
        daily_summary += date + min_t + max_t + '\n'
    return daily_summary

