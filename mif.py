import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://govtschemes.in/micro-irrigation-fund#gsc.tab=0")
soup = BeautifulSoup(html.text, "lxml")

with open("mif.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())

mif = soup.findAll('div', class_ = "clearfix text-formatted field field--name-body field--type-text-with-summary field--label-hidden field__item")
print(mif)