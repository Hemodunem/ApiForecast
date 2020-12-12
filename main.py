from requests import get
from json import dumps

token = '801db4d874c0fd13fadef4c681a48929'
end_point = 'https://api.openweathermap.org/data/2.5/onecall'
lan = input('Широта: ')
lon = input('Долгота: ')
exclude = 'currently,hourly,minutely,alerts'
day = 0

json = get(f'{end_point}?lat={lan}&lon={lon}&exclude={exclude}&appid={token}&units=metric').json()

daily = json['daily']
for forecast in daily:
    day += 1
    print('-'*44)
    print(f'Через {day} дней')
    temp = forecast['temp']
    temp_day = temp['day']
    temp_night = temp['night']
    temp_eve = temp['eve']
    temp_morn = temp['morn']
    print(f'Утро:{temp_morn} День:{temp_day} Вечер:{temp_eve} Ночь:{temp_night}')
print('-'*44)