import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.myscheme.gov.in/schemes/acandabc")
soup = BeautifulSoup(html.text, "lxml")

with open("acabc.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


acabc = soup.findAll('div', class_ = "pt-10")
print(acabc)