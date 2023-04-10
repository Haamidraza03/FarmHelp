import requests
from bs4 import BeautifulSoup
import lxml
import re

html = requests.get("https://www.niehs.nih.gov/health/topics/agents/pesticides/index.cfm#:~:text=Pesticides%20kill%2C%20repel%2C%20or%20control,weeds%20and%20other%20unwanted%20vegetation.")
soup = BeautifulSoup(html.text, "lxml")

with open("pesti.txt", "w", encoding="utf-8") as output:
    output.write(soup.prettify())


pesti = soup.findAll('article')
print(pesti)