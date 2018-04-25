# _*_ coding:utf-8 _*_
import requests
import json


# def get_weather():
url = 'http://www.weather.com.cn/data/cityinfo/101210101.html'
response = requests.get(url)
resHtml = response.content
weather = json.loads(resHtml)
weather_info = weather["weatherinfo"]
city = weather_info['city']
temp1 = weather_info['temp1']
temp2 = weather_info['temp2']
img1 = weather_info['img1']
img2 = weather_info['img2']
	# return city, temp1, temp2, img1, img2

