import datetime

from pyowm.owm import OWM
from pyowm.utils.formatting import to_date

SPB_LATITUDE = 59.894444
SPB_LONGITUDE = 30.264168
DEGREE_SIGN = u'\N{DEGREE SIGN}'


def get_data():
    owm = OWM('ad51858e01f05cf58349f151ccc6f7ed')
    mgr = owm.weather_manager()
    return mgr.one_call(lat=SPB_LATITUDE, lon=SPB_LONGITUDE)


def get_max_pressure_in_5days():
    daily_max_pressure = []
    for i in range(5):
        daily_max_pressure.append(weather_data.forecast_daily[i].pressure['press'])
    return max(daily_max_pressure)


def min_difference_night_morn_temp():
    temp_differences = []
    for i in range(8):
        temp_differences.append(abs(
            weather_data.forecast_daily[i].temperature('celsius')['night'] -
            weather_data.forecast_daily[i].temperature('celsius')['morn']))

    index_of_necessary_day = temp_differences.index(min(temp_differences))
    exact_date = to_date(weather_data.forecast_daily[index_of_necessary_day].ref_time)
    # date without hh:mm:ss+tz
    date = datetime.date(exact_date.year, exact_date.month, exact_date.day)

    return_data = {
        'date': date,
        'night_temp': weather_data.forecast_daily[index_of_necessary_day].temperature('celsius')['night'],
        'morn_temp': weather_data.forecast_daily[index_of_necessary_day].temperature('celsius')['morn']
    }
    return return_data


if __name__ == "__main__":
    weather_data = get_data()
    print(f'{get_max_pressure_in_5days()} hPa - maximum pressure for the next 5 days.')
    print(
        f'{min_difference_night_morn_temp()["date"]} - on this day there will be a minimum difference between '
        f'night ({min_difference_night_morn_temp()["night_temp"]}{DEGREE_SIGN}C) and '
        f'morning ({min_difference_night_morn_temp()["morn_temp"]}{DEGREE_SIGN}C) temperatures.')
