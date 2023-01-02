import requests

API="734f075ec68072c87b588cff622658f0"
BASE_URL= "https://api.openweathermap.org/data/2.5/weather?"

URL=""



def a_b (COUNTRY):
    URL= BASE_URL + "appid=" + API + "&q=" + COUNTRY

    DATA = requests.get(URL)
    DATA_JSON = DATA.json()

    if (DATA_JSON["cod"] != "404") :
        temp = DATA_JSON["main"]["temp"]

        return temp

def a_c (COUNTRY):
    URL= BASE_URL + "appid=" + API + "&q=" + COUNTRY

    DATA = requests.get(URL)
    DATA_JSON = DATA.json()

    if (DATA_JSON["cod"] != "404") :
        
        description = DATA_JSON["weather"][0]["description"]

        return description


def a_d (COUNTRY):
    URL= BASE_URL + "appid=" + API + "&q=" + COUNTRY

    DATA = requests.get(URL)
    DATA_JSON = DATA.json()

    if (DATA_JSON["cod"] != "404") :
        
        pressure = DATA_JSON["main"]["pressure"]

        return pressure

def a_e (COUNTRY):
    URL= BASE_URL + "appid=" + API + "&q=" + COUNTRY

    DATA = requests.get(URL)
    DATA_JSON = DATA.json()

    if (DATA_JSON["cod"] != "404") :
        
        country = DATA_JSON["sys"]["country"]
        
        return country

