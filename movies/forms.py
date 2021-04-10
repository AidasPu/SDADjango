from django.forms import ModelForm, ModelMultipleChoiceField
from movies.models import Movie, Actor


class ActorForm(ModelForm):
    class Meta():
        model = Actor

        fields = "__all__"


class MovieForm(ModelForm):
    class Meta():
        model = Movie
        fields = "__all__"


# Gedui paziureti json/ path suradima
{'coord':
     {'lon': 21.5333, 'lat': 56.2667},
 'weather': [
     {'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}],
 'base': 'stations',
 'main': {'temp': 3, 'feels_like': -2.1, 'temp_min': 3, 'temp_max': 3, 'pressure': 990, 'humidity': 100},
 'visibility': 10000,
 'wind': {'speed': 5.14, 'deg': 240},
 'clouds': {'all': 90}, 'dt': 1615727874,
 'sys': {'type': 1, 'id': 1875, 'country': 'LT', 'sunrise': 1615697518, 'sunset': 1615739657},
 'timezone': 7200,
 'id': 594488, 'name': 'Skuodas', 'cod': 200}

{
    "name": "projects/blnors74j0eqn2851920/devices/bhqgtnut96bg00813lsg",
    "type": "temperature",
    "labels": {
        "kit": "consumer-specific-data without-rock-yard",
        "name": "Temp2",
        "team": "team4"
    },
    "reported": {
        "networkStatus": {
            "signalStrength": 71,
            "updateTime": "2019-10-18T13:06:41.948000Z",
            "cloudConnectors": [
                {
                    "id": "biqq4rkc00017040aicg",
                    "signalStrength": 71
                }
            ],
            "transmissionMode": "LOW_POWER_STANDARD_MODE"
        },
        "batteryStatus": {
            "percentage": 100,
            "updateTime": "2019-10-17T14:58:14.119000Z"
        },
        "temperature": {
            "value": 23.55,
            "updateTime": "2019-10-18T13:06:41.948000Z"
        },
        "touch": {
            "updateTime": "2019-09-30T05:27:54.763911Z"
        }
    }
}
