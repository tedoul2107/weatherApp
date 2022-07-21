import urllib.request
from datetime import datetime

from django.shortcuts import render
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        if city == '':
            city = 'yaounde'

        # city = request.POST['city']
        source = urllib.request.urlopen(
                f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=98ade68b1fa0dbb204089ddc80f8c2c9').read()
        list_of_data = json.loads(source)

        data = {
                'country_code': str(list_of_data['sys']['country']),
                'coordinate': str(list_of_data['coord']['lon']) + ', '
                              + str(list_of_data['coord']['lat']),
                'temp': str(list_of_data['main']['temp']) + '° ',
                'pressure': str(list_of_data['main']['pressure']),
                'humidity': str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': str(list_of_data['weather'][0]['icon']),
                'name': str(list_of_data['name']),
                # 'timezone': datetime.fromtimestamp(int(str(list_of_data['timezone']))),
                'timezone': datetime.now(),
                'wind': str(list_of_data["wind"]["speed"]),
            }
        print(data)
    else:
        city = 'yaounde'
        source = urllib.request.urlopen(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=98ade68b1fa0dbb204089ddc80f8c2c9').read()
        list_of_data = json.loads(source)

        data = {
            'country_code': str(list_of_data['sys']['country']),
            'coordinate': str(list_of_data['coord']['lon']) + ', '
                          + str(list_of_data['coord']['lat']),
            'temp': str(list_of_data['main']['temp']) + '° ',
            'pressure': str(list_of_data['main']['pressure']),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data['weather'][0]['main']),
            'description': str(list_of_data['weather'][0]['description']),
            'icon': str(list_of_data['weather'][0]['icon']),
            'name': str(list_of_data['name']),
            # 'timezone': datetime.fromtimestamp(int(str(list_of_data['timezone']))),
            'timezone': datetime.now(),
            'wind': str(list_of_data["wind"]["speed"]),
        }

    return render(request, 'main/app.html', data)