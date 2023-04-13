import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.geeksforgeeks.org/gramin-bhandaran-yojana-or-rural-godown-scheme/")
soup = BeautifulSoup(html.text, "lxml")

with open("gby.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())

art = soup.findAll('div', class_='article-title')
print(art)
gby = soup.findAll('div', class_ = "text")
print(gby)