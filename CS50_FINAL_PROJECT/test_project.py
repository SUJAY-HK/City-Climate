from project import get_api, get_weather_data,format_weather_data

def test_get_api():
    assert get_api() == '6dd4c9cf8ca04055ae86bf099ede112e'

def test_get_weather_data():
    assert get_weather_data('London') is not None
    assert get_weather_data('Cairo') is not None

def test_format_weather_data():
    assert format_weather_data(get_weather_data('London'), 'London') is not None
    assert format_weather_data(get_weather_data('Cairo'), 'Cairo') is not None
