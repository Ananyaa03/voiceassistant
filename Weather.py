import requests

api_address="http://api.openweathermap.org/data/2.5/weather?q=Angul&appid=f895e5c66cd4155dd875e080e7514226"
json_data=requests.get(api_address).json()



def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description=json_data["weather"][0]["description"]
    return description

#print(temp())
#print(des())