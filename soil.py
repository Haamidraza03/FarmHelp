import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://agriculture.vic.gov.au/farm-management/soil/what-is-soil")
soup = BeautifulSoup(html.text, "lxml")

with open("soil.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


soil = soup.findAll('main', class_ = "")
print(soil)