import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.britannica.com/topic/fertilizer")
soup = BeautifulSoup(html.text, "lxml")

with open("ferti.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


ferti = soup.findAll('div', class_ = 'topic-content pt-15')
print(ferti)