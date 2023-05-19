import requests

api_key='0c3c301de0f439c36660d7dad55bca94'

user_input=input("enter city: ")
#print(user_input)

weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod']=='404':
    print("No city found")
else:
    
    weather=weather_data.json()['weather'][0]['main']
    temp=weather_data.json()['main']['temp']
    final_temp=round((int(temp)-32)*(5/9))
    feels_like=weather_data.json()['main']['feels_like']
    final_feel=round((int(feels_like)-32)*(5/9))
    humidity=weather_data.json()['main']['humidity']
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is {final_temp} °C")
    print(f"Feels like {final_feel} °C")
    print(f"The humidity in {user_input} is: {humidity}")
#print(weather_data.status_code)
    #print(weather_data.json())