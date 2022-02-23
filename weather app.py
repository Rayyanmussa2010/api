from tkinter import*
import requests
import json
root = Tk()
root.geometry("300x300")
citylabel=Label(root, text="City Name", font=("Helvetica", 18,'bold'),bg="white")
citylabel.place(relx=0.5, rely=0.1, anchor=CENTER)
cityentry=Entry(root)
cityentry.place(relx=0.5, rely=0.2, anchor=CENTER)
weather=Label(root)
weather.place(relx=0.5, rely=0.1, anchor=CENTER)
humidity=Label(root)
humidity.place(relx=0.5, rely=0.2, anchor=CENTER)

def city_name():
    api_request=requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + cityentry.get() + "&appid="+ "21cab08deb7b27f4c2b55f3e2df28ea4")
    api_output_json=json.loads(api_request.content)
    weather_info=api_output_json['weather'][0]["main"]
    humidity_info=api_output_json['main']['humidity']
    weather["text"]="Weather: "+str(weather_info)
    humidity["text"]="humidity: "+str(humidity_info)
    citylabel["text"]=cityentry.get()
    cityentry.destroy()
    search_button.destroy()

search_button=Button(root, text="Search Weather", command=city_name)
search_button.place(relx=0.5, rely=0.3, anchor=CENTER)
root.mainloop()