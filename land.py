import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://en.wikipedia.org/wiki/Agricultural_land#:~:text=Agricultural%20land%20is%20typically%20land,well%20as%20pasture%20or%20rangeland.")
soup = BeautifulSoup(html.text, "lxml")

with open("land.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


land = soup.findAll('div', class_ = "mw-parser-output")
print(land)