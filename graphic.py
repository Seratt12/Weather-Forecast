from tkinter import *
from tkinter import ttk 
from weather import getWeather

def window():


    def search():
        city = str.lower(entry.get())
        print(city)
        weather = getWeather(city)

        if weather.err != 1:
            result["text"] = weather
        else:
            result["text"] = "Ошибка! Не верное название города"
        


    def finish():
        root.destroy() # Ручное закрытие файла
        print("Закрытие приложения")


    root = Tk() # Главное окно
    root.geometry("600x300+600+300") # Размер окна
    root.resizable(False, False) # Запрет растягивать окно
    root.title("Погода") # Название окна
    root.iconbitmap("img/logo.ico") # Иконка окна

    root.protocol("WM_DELETE_WINDOW", finish)

    label = ttk.Label(text="Введите название города:")
    label.pack(anchor=N, padx=5, pady=15)

    entry = ttk.Entry()
    entry.pack(fill=X, padx=[30, 30])

    button = ttk.Button(text="Узнать погоду", command=search)
    button.pack(anchor=NE, padx=[200, 20], pady=20,  ipadx=10, ipady=10)

    result = ttk.Label()
    result.pack()



    root.mainloop() # Цикл обработки событий окна