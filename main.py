# Import Required Library
import requests
from tkinter import *
from PIL import Image, ImageTk

# Create Object
root = Tk()

# Set title
root.title('Weather App')

# Set geometry
root.geometry('560x400')

# Set max and min size
root.maxsize(560,400)
root.minsize(560,300)

# weather app text
weather_app = Label(root, text="WEATHER APP", font=("Consolas", "24", "bold italic"), bg='#000fff000',pady = 5)
weather_app.pack()


# downloading weather condition image
def get_image(url_img, image_name):
    global weather_img
    url = requests.get(f'http:{url_img}')
    with open(image_name, 'wb') as f:
        f.write(url.content)
    f.close()
    weather_img = ImageTk.PhotoImage(Image.open(image_name))


# request of weather
def weather_request(location):
    url = requests.get(
        f'http://api.weatherapi.com/v1/forecast.json?key=b5e01861b575475ca2f34339211003&q={location}&days=7')
    data = url.json()
    return (data['location']['name'],
            data['location']['region'],
            data['current']['temp_c'],
            data['current']['condition']['text'],
            data['current']['wind_kph'],
            data['current']['pressure_mb'],
            data['current']['humidity'],
            data['current']['condition']['icon'])


# get location text
def weather_information(event):
    name, region, temp_c, condtion, wind_kph, pressure_mb, humd, today_weather_img = weather_request(
        location_text.get())

    # get image of weather
    get_image(today_weather_img, 'weather.png')

    # set the label text
    weather_condition_image.config(image=weather_img)
    location.config(text=f'{name},{region}')
    weather_condition.config(text=condtion)
    temperature.config(text=int(temp_c))
    degree_celcius.config(text="°C")
    pressure.config(text=f'Pressure: {int(pressure_mb)}hpa')
    humidity.config(text=f'Humidity: {humd}%')
    wind.config(text=f'Wind: {int(wind_kph)} km/h')
    location_text.delete(0, END)


# location entry box
location_text = Entry(root, font=("Arial", "20"), width=30, borderwidth=2)
location_text.bind('<Return>', weather_information)
location_text.place(x=50, y=50)

# location
location = Label(root, text="", font=("Times new roman", "20", "bold italic"), bg='#ffd343')
location.place(x=10, y=100)

# weather condition
weather_condition = Label(root, text="", font=("Consolas", "14", "bold italic"), bg='#ffd343')
weather_condition.place(x=10, y=160)


# weather condition image
weather_condition_image = Label(root, bg='#ffd343')  # '#87ceeb'
weather_condition_image.place(x=20, y=185)

# temperature
temperature = Label(root, text="", font=("Times new roman", "40", "bold italic"), bg='#ffd343')
temperature.place(x=100, y=185)

# degree_celcius
degree_celcius = Label(root, text="", font=("Times", "14", "bold italic"), bg='#ffd343')
degree_celcius.place(x=160, y=190)

# pressure
pressure = Label(root, text="", font=("Times", "14", "bold italic"), bg='#ffd343')
pressure.place(x=350, y=180)

# humidity
humidity = Label(root, text="", font=("Times", "14", "bold italic"), bg='#ffd343')
humidity.place(x=350, y=207)

# wind
wind = Label(root, text="", font=("Times", "14", "bold italic"), bg='#ffd343')
wind.place(x=350, y=234)

# loop ends
root.configure(bg='#ffd343')

# Execute Tkinter
root.mainloop()