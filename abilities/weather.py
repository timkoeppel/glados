from pyowm import OWM


def currentWeather(reg_ex):
    """gathers weather data with given regEx as city name (from comman)"""
    # noinspection PyBroadException
    try:
        result = ''
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM('ab0d5e80e8dafb2cb81fa9e82431c1fa')
            mgr = owm.weather_manager()
            obs = mgr.weather_at_place(city)
            w = obs.weather
            k = w.status
            x = w.temperature(unit='celsius')
            result = 'Current weather in %s: %s. The maximum temperature is %0.2f ' \
                  'and the minimum temperature is %0.2f degree celcius.' \
                  % (city, k, x['temp_max'], x['temp_min'])
    except Exception:
        result = 'The requested city ' + reg_ex.group(1) + ' does not exist. You may try again!'
    return result
