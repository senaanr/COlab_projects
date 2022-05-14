from tkinter import*
from PIL import ImageTk,Image
import requests

url = 'http://api.openweathermap.org/data/2.5/weather'
api_key = '1b838af461fc572214228abb97dd7a0b'
iconUrl = 'http://openweathermap.org/img/wn/{}@2x.png'

app = Tk()
app.geometry('300x450')
app.title('KK Hava Durumu')

cityEntry = Entry(app,justify='center')
cityEntery.pack(fill=BOTH,ipady=10,padx=18,pady=5)
cityEntery.focus()

searchButton = Button(app, text='Arama', font=('Arial',15))
searchButton.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app, font=('Arial',40))
locationLabel.pack

tempLabel = Label(app,font=('Arial',50,"bold"))
tempLabel.pack()

conditionLabel = Label(app,font=('Arial',20))
conditionLabel.pack()

app.mainloop()
