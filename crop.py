import requests
from bs4 import BeautifulSoup
import lxml
import re

# html = requests.get("https://agriculture.vic.gov.au/farm-management/soil/what-is-soil")
html = requests.get("https://en.wikipedia.org/wiki/Crop")
soup  = BeautifulSoup(html.text, "lxml")

with open("crop.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


soil = soup.findAll('div' , class_ = 'mw-parser-output')
print(soil)