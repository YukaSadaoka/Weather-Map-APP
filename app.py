from tkinter import Tk, Label, Button, Canvas, PhotoImage, Frame, Entry
import requests
from PIL import Image,  ImageTk
from io import BytesIO
from Config import fontConfig, backgroundColour, darkBlue, height, width
import Utility
import os

def getData(cityRequested=None, root=None):
    try:
        if cityRequested is not None and os.getenv('WEATHER_APIKEY') is not None:
            weatherResponse = Utility.getWeather(cityRequested)
            if weatherResponse.status_code is 200:
                weatherData = weatherResponse.json()
                mainLabel['text'] = Utility.format_response(weatherData)
                params = Utility.createLocationParam(response=weatherData)
                if isinstance(params, dict):
                    response_map = requests.get(os.getenv('MAP_ENDPOINT'), params=params)
                    if response_map.status_code is 200:
                        img = Image.open(BytesIO(response_map.content))
                        photo = ImageTk.PhotoImage(img)
                        map_frame.delete('all')
                        map_frame.create_image(10, 20, anchor='nw', image=photo)
                        map_frame.image = photo
            else:
                mainLabel['text'] = 'Unable to get data'
    except:
        print('error occuured in weather data')
        mainLabel['text'] = 'Error Occurred. Try again.'

root = Tk()
root.title('Weather APP')
canvas = Canvas(root, height=height, width=width)
canvas.pack()

# Create the background
background = PhotoImage(file='./static/background.png')
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the search box frame
frame = Frame(root, bg=backgroundColour, bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

# Create the search box entry
entry = Entry(frame, font=fontConfig)
entry.place(relx=0.35, relwidth=0.65, relheigh=1)

# Create the first output textbox
lower_frame = Frame(root, bg=backgroundColour, bd=10)
lower_frame.place(rely=0.25, relx=0.1, relwidth=0.8, relheigh=0.2)
mainLabel = Label(lower_frame, font=fontConfig)
mainLabel.place(relwidth=1, relheight=1)

# Create  the second output textbox
map_frame = Canvas(root, bd=10, bg='#ffffff')
map_frame.place(rely=0.5, relx=0.1, relwidth=0.8, relheight=0.5)

# Create the search button
button = Button(frame, font=fontConfig, text="Get Weather", bg=darkBlue,
                   command=lambda: getData(entry.get()))
button.place(relheight=1, relwidth=0.35)

root.mainloop()