from keys import *
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkinter import *
from tkinter import messagebox


API_KEY = weather_api_key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?appid="+API_KEY+"&q="

def generate(city):
    if city.get()=="":
        messagebox.showerror("Error","Please enter the name of the city")
        return
    url = BASE_URL + city.get()
    response = requests.get(url)
    if response.status_code==200:
        data = response.json()
        temp.config(state="normal")
        temp.delete(0,END)
        temp.insert(0,str(round((data['main']['temp']-273.15),2))+"°C")
        temp.config(state="readonly")

        hum.config(state="normal")
        hum.delete(0,END)
        hum.insert(0,data['main']['humidity'])
        hum.config(state="readonly")

        wind.config(state="normal")
        wind.delete(0,END)
        wind.insert(0,data['wind']['speed'])
        wind.config(state="readonly")

        desc.config(state="normal")
        desc.delete(0,END)
        desc.insert(0,data['weather'][0]['description'])
        desc.config(state="readonly")

        city.delete(0,END)
        city.insert(0,data['name'])
    else:
        messagebox.showerror("Error","City not found")
        return

root = Tk()
root.title("Weather Forecast")
root.resizable(False, False)

Label(root, text="Weather Forecast appliction",font=("Helvetica",20,"bold underline"),fg="darkblue").grid(row=0, column=0, columnspan=2, padx=10, pady=10)
Label(root, text="Enter the city name: ",font=("Helvetica",15,"bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
city = Entry(root, font=("Helvetica",15), borderwidth=3, width=20)
city.grid(row=1, column=1, padx=10, pady=10, sticky="w")
Button(root, text="Generate weather details", font=("Helvetica",15,"bold"), bg="blue", fg="white", command=lambda:generate(city)).grid(row=2, column=0, columnspan=2, padx=10, pady=10)
Label(root, text="Temperature: ",font=("Helvetica",15,"bold")).grid(row=3, column=0, padx=10, pady=10, sticky="e")
temp = Entry(root, text="", font=("Helvetica",15), width=20, borderwidth=5, state="readonly")
temp.grid(row=3, column=1, padx=10, pady=10, sticky="w")
Label(root, text="Humidity: ",font=("Helvetica",15,"bold")).grid(row=4, column=0, padx=10, pady=10, sticky="e")
hum = Entry(root, text="", font=("Helvetica",15), width=20, borderwidth=5, state="readonly")
hum.grid(row=4, column=1, padx=10, pady=10, sticky="w")
Label(root, text="Wind Speed: ",font=("Helvetica",15,"bold")).grid(row=5, column=0, padx=10, pady=10, sticky="e")
wind = Entry(root, text="", font=("Helvetica",15), width=20, borderwidth=5, state="readonly")
wind.grid(row=5, column=1, padx=10, pady=10, sticky="w")
Label(root, text="Weather Condition: ",font=("Helvetica",15,"bold")).grid(row=6, column=0, padx=10, pady=10, sticky="e")
desc = Entry(root, text="", font=("Helvetica",15), width=20, borderwidth=5, state="readonly")
desc.grid(row=6, column=1, padx=10, pady=10, sticky="w")

root.mainloop()





