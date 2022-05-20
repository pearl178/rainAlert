from twilio.rest import Client
import requests
api_key = 'd918909b8a8fc8e7240fcc0184b2e460'
account_sid = 'AC5291353c75429cc516071c422886464f'
auth_token = '916c719fea9e68eed6bd8d0dca1bc415'

parameters = {
    'lat': 40.760780,
    'lon': -111.891045,
    'exclude': 'current,minutely,daily,alerts',
    'appid': api_key
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
future_12hours = [hour['weather'][0]["id"] for hour in weather_data['hourly'][:12]]
print(future_12hours)
will_not_rain = all(id > 700 for id in future_12hours)
if not will_not_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="It's going to rain today. Bring an umbrella 🌂",
                         from_='+14707858749',
                         to='receiver_phone_number'
                     )
print(message.status)
