import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.godigit.com/guides/government-schemes/weather-based-crop-insurance-scheme")
soup = BeautifulSoup(html.text, "lxml")

with open("wbcis.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


wbcis = soup.findAll('div')
print(wbcis)