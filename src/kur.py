from bs4 import BeautifulSoup
import requests
import time
#----------------------------------------DOLAR-----------------
url1 = "https://www.google.com/finance/quote/USD-TRY?hl=tr"

sayfa = requests.get(url1)

html_sayfa = BeautifulSoup(sayfa.content,"html.parser")

dolar = html_sayfa.find("div",class_="YMlKec fxKbKc").getText()

roundeddolor = round(float(float(dolar.replace(",","."))),2)
#-----------------------------------------------EURO
url2 = "https://www.google.com/finance/quote/EUR-TRY?hl=tr"

sayfa2 = requests.get(url2)

html_sayfa2 = BeautifulSoup(sayfa2.content,"html.parser")

euro = html_sayfa2.find("div",class_="YMlKec fxKbKc").getText()

roundeeuro = round(float(float(euro.replace(",","."))),2)
#sterelin
url3 = "https://www.google.com/finance/quote/GBP-TRY?hl=tr"

sayfa3 = requests.get(url3)

html_sayfa3 = BeautifulSoup(sayfa3.content,"html.parser")

sterlin = html_sayfa3.find("div",class_="YMlKec fxKbKc").getText()

roundeeuro = round(float(float(sterlin.replace(",","."))),2)
#----------------------------------------------kripto---------------------------------
#bitcoin

url4 = "https://www.google.com/finance/quote/BTC-TRY?hl=tr"

sayfa4 = requests.get(url4)

html_sayfa4 = BeautifulSoup(sayfa4.content,"html.parser")

btc = html_sayfa4.find("div",class_="YMlKec fxKbKc").getText()
