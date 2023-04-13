import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://dahd.nic.in/related-links/livestock-insurance")
soup = BeautifulSoup(html.text, "lxml")

with open("lis.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())

lis = soup.findAll('div', class_ = 'field-item even')
print(lis)