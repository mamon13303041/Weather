from django.shortcuts import render
import json
import urllib.request

from xarray import Coordinate

# Create your views here.

def home(request):
    if request.method == 'POST':
        city=request.POST['city']
        res_webapi=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=ce3a77f30f53dc1bfc3cec1809253686').read()
        json_data=json.loads(res_webapi)
        weather_data={
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' +
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
           
        }
    else:
        city=''
        weather_data={}
    return render(request,'home.html',{'city':city,'weather_data':weather_data})