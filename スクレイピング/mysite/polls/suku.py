from bottle import route, run, template, redirect
import requests
from bs4 import BeautifulSoup
@route("/")
def index():
    number1=g_number1()
    number2=g_number2()
    return template("index",out1=number1,out2=number2)


def g_number1():
    r1 = requests.get("https://weather.goo.ne.jp/amedas/83061/")
    soup1 = BeautifulSoup(r1.content, "html.parser")
    ser1 = soup1.find("div", id="NR-wrapper-in")
    ser2 = ser1.find_all("tr")
    for ser3 in ser2:
        out1=print(ser3.text)
    return out1

def g_number2():
    r2 = requests.get("https://weather.nifty.com/cs/catalog/weather_pinpoint/catalog_44209_1.htm")
    soup2 = BeautifulSoup(r2.content, "html.parser")
    ser4 = soup2.find("div", id="tomorrowWeather")
    res5 = ser4.find_all("tr")
    print("豊後高田市")
    for res6 in res5:
        out2=print(res6.text)
    return out2

run(host='localhost', port=8081, debug=True, reloader=True)
