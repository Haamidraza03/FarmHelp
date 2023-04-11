import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://nationalinsurance.nic.co.in/en/pradhan-mantri-fasal-bima-yojana-pmfby")
soup = BeautifulSoup(html.text, "lxml")

with open("pmfby.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


pmfby = soup.findAll('div', class_ = 'field-items')
print(pmfby)