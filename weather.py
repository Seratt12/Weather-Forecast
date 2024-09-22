import requests


from bs4 import BeautifulSoup

class Weather:
    """Класс Weather который включает в себя поля: температура, состояние погоды, ветер, влажность, дваление и облачность"""

    def __init__(self, temperature: str, weather_condition: str, wind: str, wetness: str, pressure: str, cloudiness: str):
        """Конструктор класса Weather"""
        self.temperature = temperature
        self.weather_condition = weather_condition
        self.wind = wind
        self.wetness = wetness
        self.pressure = pressure
        self.cloudiness = cloudiness
        self.err = 0   


    def __str__(self):
        """Вывод полей класса"""
        return(f"""
Сейчас:{self.temperature}{self.weather_condition}
Ветер: {self.wind}
Влажность: {self.wetness}
Давление: {self.pressure}
Облачность: {self.cloudiness}
            """)



def getWeather(city: str):
        """
        В параметре принимает название города (на русском). Возвращает класс,
        где хранятся поля градусов, состояние погоды, ветра, давления, влажности и облачности
        Если функция не сможет запарсить сайт, то вернёт список с одним элементов - строкой 
        "Ошибка! Не верное название города"
        """


        # Создание списка, с атрибутами погоды
        ListOfWeather = []

        # Получение кода сайта
        url = f'https://meteolabs.org/погода_{city}/'
        responce = requests.get(url)

        
        
        if responce.status_code == 200:
            soup = BeautifulSoup(responce.text , "html.parser")

            # Сколько сейчас градусов
            weatherNow = soup.find('p', class_="wthSBlock__commonWth")
            ListOfWeather.append(weatherNow.text)

            # Какая облачность
            statusNow = soup.find('p', class_="wthSBlock__condTxt")
            ListOfWeather.append(statusNow.text)
            # Ветер, Влажность, Давление, Облачность
            detailedInformation = soup.findAll('span', class_="wthSBlock__paramVal")
            for inf in detailedInformation:
                ListOfWeather.append(''.join(inf.get_text(strip = True)))

            weather = Weather(ListOfWeather[0], ListOfWeather[1], ListOfWeather[2], ListOfWeather[3], ListOfWeather[4], ListOfWeather[5])
        else:
            weather = Weather("0", "0", "0" , "0", "0", "0")
            weather.err = 1

        return weather