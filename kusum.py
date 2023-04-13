import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://pmkusum.mnre.gov.in/landing-about.html")
soup = BeautifulSoup(html.text, "lxml")

with open("ksm.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


ksm = soup.findAll('div', class_ = "bannercn")
print(ksm)