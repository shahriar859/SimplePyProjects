import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.com/weather/today/l/Dhaka+Bangladesh+BGXX0003:1:BG')
soup = BeautifulSoup(page.content,'html.parser')
#print(soup)
#print(soup.find_all('a'))
w = soup.find(id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a')
#print(w)
#print(w.find_all('li'))
items = w.find_all(class_='_3K14X _74Gm9 _2yeqQ')
#print(items[0])
#print(items[0].find(class_='lfjoB'))
#print(items[0].find(class_='lfjoB').get_text())
#print(items[0].find(class_='_2v_go').get_text())
#print(items[0].find(class_='_2H5Iw').get_text())

name = [item.find(class_='lfjoB').get_text() for item in items]
#print(name)
temp = [item.find(class_='_2v_go').get_text() for item in items]
#print(temp)
report = [item.find(class_='_2H5Iw').get_text() for item in items]
#print(report)

weather_stuff = pd.DataFrame(
    {
        'Time' : name,
        'temparature' : temp,
        'Report' : report,
})

print(weather_stuff)
weather_stuff.to_csv('WebScraping.csv')