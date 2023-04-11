import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.india.gov.in/spotlight/pradhan-mantri-krishi-sinchayee-yojana")
soup = BeautifulSoup(html.text, "lxml")

with open("pmksy.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


pmksy = soup.findAll('div', class_ = 'splightinner')
print(pmksy)